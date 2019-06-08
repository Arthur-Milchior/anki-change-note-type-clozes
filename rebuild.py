from anki.lang import _
from .cloze import getTemplateList
from .twoLists import eltToPos
from aqt.browser import ChangeModel
from .config import getUserOption
from aqt.qt import QGridLayout, QWidget, QComboBox, QLabel

def rebuildTemplateMap(self):
    self.tsrc = getTemplateList(self, self.oldModel)
    self.tdst = getTemplateList(self, self.targetModel)
    return _rebuildMap(self, "t")

ChangeModel.rebuildTemplateMap = rebuildTemplateMap

def rebuildFieldMap(self):
    self.fsrc = self.oldModel["flds"]
    self.fdst = self.targetModel["flds"]
    return _rebuildMap(self, "f")
ChangeModel.rebuildFieldMap = rebuildFieldMap


def _rebuildMap(self, key):
    """
    key -- either "t" or "f", for template or fields. What to edit.
   
    """
    map = getattr(self, key + "widg")
    lay = getattr(self, key + "layout")
    if map:
        lay.removeWidget(map)
        map.deleteLater()
        setattr(self, key + "MapWidget", None)
    map = QWidget()
    l = QGridLayout()
    combos = []
    targets = [template['name'] for template in getattr(self, key+"dst")]
    indices = {}
    sources = getattr(self,key+"src")
    sourcesNames = [template["name"] for template in sources]
    if getUserOption("Associate to same name"):
        assoc = eltToPos(sourcesNames, targets)
    else:
        assoc = enumerate(sourcesNames)
    for i, templateName in assoc:
        l.addWidget(QLabel(_("Change %s to:") % templateName), i, 0)
        cb = QComboBox()
        cb.addItems(targets + [_("Nothing")])
        idx = min(i, len(targets))
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

