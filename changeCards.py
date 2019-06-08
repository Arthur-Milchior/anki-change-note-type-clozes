from anki.utils import ids2str, intTime
from anki.models import ModelManager

#removed the special case of MODEL_CLOZE
def _changeCards(self, nids, oldModel, newModel, map):
    """Change the note whose ids are nid to the model newModel, reorder
    fields according to map. Write the change in the database
    Remove the cards mapped to nothing
    If the source is a cloze, it is (currently?) mapped to the
    card of same order in newModel, independtly of map.
    keyword arguments:
    nids -- the list of id of notes to change
    oldModel -- the soruce model of the notes
    newmodel -- the model of destination of the notes
    map -- the dictionnary sending to each card 'ord of the old model a card'ord of the new model or to None
    """
    d = []
    deleted = []
    for (cid, ord) in self.col.db.execute(
        "select id, ord from cards where nid in "+ids2str(nids)):
        new = map[ord]
        if new is not None:
            d.append(dict(
                cid=cid,new=new,u=self.col.usn(),m=intTime()))
        else:
            deleted.append(cid)
    self.col.db.executemany(
        "update cards set ord=:new,usn=:u,mod=:m where id=:cid",
        d)
    self.col.remCards(deleted)
ModelManager._changeCards = _changeCards
