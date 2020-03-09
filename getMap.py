from aqt.browser import ChangeModel

from .cloze import getTemplateList


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
