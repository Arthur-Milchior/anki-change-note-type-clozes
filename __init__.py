import re
from anki.utils import ids2str, intTime
from aqt import mw
from anki.consts import *
from aqt.browser import ChangeModel
from aqt.qt import *
from anki.models import ModelManager
from anki.lang import _

def rebuildTemplateMap(self):
    src = getTemplateList(self, self.oldModel)
    dst = getTemplateList(self, self.targetModel)
    return _rebuildMap(self, "t", src, dst)

ChangeModel.rebuildTemplateMap = rebuildTemplateMap

def rebuildFieldMap(self):
    src = self.oldModel["flds"]
    dst = self.targetModel["flds"]
    return _rebuildMap(self, "f", src, dst)
ChangeModel.rebuildFieldMap = rebuildFieldMap

def getTemplateList(self, model):
    if model['type'] == MODEL_STD:
        return model["tmpls"]
    else:
        return [{"name":f"Cloze {n}", "ord":n-1} for n in sorted(getClozeNumber(self))]


def getClozeNumberFromNids(nids):
    """Given a list of nids, return the set of cloze number in the fields
    of notes with one of those nids."""
    s = set()
    for flds in mw.col.db.list(f"""select flds from notes where id in {ids2str(nids)} """):
        getClozeNumberFromFields(flds, s)
    return s

def getClozeNumber(changeModelWindow):
    """The list of cloze number contained in the fields of some notes
    whose nid belongs to ChangeModel window.

    """
    return list(getClozeNumberFromNids(changeModelWindow.nids))

#from anki.models.ModelManager._availClozeOrds
clozeFinder = re.compile(r"(?s){{c(?P<number>\d+)::.+?}}")
def getClozeNumberFromFields(flds, s):
    """Add to the set s the cloze number of flds.

    """
    for match in clozeFinder.finditer(flds):
        number = match.group("number")
        s.add(int(number))
    return s


def _rebuildMap(self, key, src, dst):
    map = getattr(self, key + "widg")
    lay = getattr(self, key + "layout")
    if map:
        lay.removeWidget(map)
        map.deleteLater()
        setattr(self, key + "MapWidget", None)
    map = QWidget()
    l = QGridLayout()
    combos = []
    targets = [template['name'] for template in dst] + [_("Nothing")]
    indices = {}
    for i, template in enumerate(src):
        l.addWidget(QLabel(_("Change %s to:") % template['name']), i, 0)
        cb = QComboBox()
        cb.addItems(targets)
        idx = min(i, len(targets)-1)
        cb.setCurrentIndex(idx)
        indices[cb] = idx
        cb.currentIndexChanged.connect(
            lambda i, cb=cb, key=key: self.onComboChanged(i, cb, key))
        combos.append(cb)
        l.addWidget(cb, i, 1)
    map.setLayout(l)
    lay.addWidget(map)
    setattr(self, key + "widg", map)
    setattr(self, key + "layout", lay)
    setattr(self, key + "combos", combos)
    setattr(self, key + "indices", indices)


def _getMap(self, old=None, combos=None, new=None):
    """A map from template's ord of the old model to template's ord of the new
    model. Or None if no template
     Contrary to what this name indicates, the method may be used
    without templates. In getFieldMap it is used for fields
     keywords parameter:
    old -- the list of templates of the old model
    combos -- the python list of gui's list of template
    new -- the list of templates of the new model
    If old is not given, the other two arguments are not used.
    """
    map = {}
    for i, f in enumerate(old):
        idx = combos[i].currentIndex()
        if idx == len(new):
            # ignore. len(new) corresponds "Nothing" in the list
            map[f['ord']] = None
        else:
            f2 = new[idx]
            map[f['ord']] = f2['ord']
    return map

def getFieldMap(self):
    """Associating to each field's ord of the source model a field's
    ord (or None) of the new model."""
    return _getMap(self,
        self.oldModel['flds'],
        self.fcombos,
        self.targetModel['flds'])

def getTemplateMap(self):
    return _getMap(self,
                   getTemplateList(self, self.oldModel),
                   self.tcombos,
                   getTemplateList(self, self.targetModel))
ChangeModel.getTemplateMap = getTemplateMap
ChangeModel.getFieldMap = getFieldMap


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
