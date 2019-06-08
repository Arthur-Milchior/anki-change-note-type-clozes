# Improving: Change note type
This add-on improves «Change note type» in two related ways. 
## Rationale
### clozed note
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

### Considering when fields and card types have the same name
When I use anki, I may multiple note types having a card types named
«definition», for example. When I change the note type of a card, I
then want, by default, the card «definition» to be mapped to the card
«definition», even if they are not in the same position in the list of
card type. 

This add-on does that. It ensures that, by default, when source and
target note types have a card types/fields which have the same name,
then by default, they map to each other. 

This can be deactivated in the configuration.

## Warning
This add-on was created 3rd of June 2019. It is still new, and may
have unfound bugs. So please, before using it, make a back-up, check
whether the note type change went allright, and let me know either if
it worked or if you had a bug

## Configuration
There is a single configuration option. If you set "Associate to same
name" to `true`, the add-ons will set the default option of each card
types/fields to be the card types/fields with the same
name. Otherwise, if it is set to `false`, the add-on will keep the
default way.

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
