# Change note type, even for clozed note
## Rationale
Currently, anki has a limitation when you want to change a card type
from or to a clozed note type.

Without this add-on, if you want to change a standard note to a clozed
note type, you can move a single card, and it will move to cloze 1.

If you want to change a clozed note type to a standard type, only
cloze 1 will be changed.

With this add-on, you'll be able to change any card type to any cloze
number and reciprocally. The only restriction is that you need to have
the cloze number in the fields before changing TO a clozed note
type. Because this add-on will only allow you to choose one of the
cloze number appearing in a field.

## Warning
This add-on was created 3rd of June 2019. It is still new, and may
have unfound bugs. So please, before using it, make a back-up, check
whether the note type change went allright, and let me know either if
it worked or if you had a bug

## Internal
It changes methods:
* `aqt.browser.ChangeModel.rebuildTemplateMap`
* `aqt.browser.ChangeModel.rebuildFieldMap`
* `aqt.browser.ChangeModel.getTemplateMap`
* `aqt.browser.ChangeModel.getFieldMap`
* `anki.models.ModelManager._changeCards`


## Version 2.0
None


## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
License     | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-change-note-type-clozes.git
Addon number| [513858554](https://ankiweb.net/shared/info/513858554)
Support me on| [![Ko-fi](https://ko-fi.com/img/Kofi_Logo_Blue.svg)](Ko-fi.com/arthurmilchior) or [![Patreon](http://www.milchior.fr/patreon.png)](https://www.patreon.com/bePatron?u=146206)
