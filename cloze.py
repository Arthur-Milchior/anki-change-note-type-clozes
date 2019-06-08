from anki.consts import *
from anki.models import ModelManager
from anki.utils import ids2str
from aqt import mw
import re

def getClozeNumberFromNids(nids):
    """Given a list of nids, return the set of cloze number in the fields
    of notes with one of those nids.

    """
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


def getTemplateList(self, model):
    """The list of template
    
    For a normal template, it's actually the list of template.
    Otherwise, it is, in increasing order, the list of clozes used in self.nid
    """
    if model['type'] == MODEL_STD:
        return model["tmpls"]
    else:
        return [{"name":f"Cloze {n}", "ord":n-1} for n in sorted(getClozeNumber(self))]
