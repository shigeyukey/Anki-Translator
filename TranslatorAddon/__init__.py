import os
from os.path import dirname, abspath, realpath
from aqt.utils import showInfo
from anki.hooks import addHook
from . import TranslatorDialog as td
from aqt.editor import Editor

defaultSourceLanguage = ""
defaultTargetLanguage = ""
defaultLoadGrammarInfos = ""
currentDirName=dirname(abspath(realpath(__file__)))



# This function gets executed when the button in the editor is pressed
def onGetTranslation(editor:Editor):
    dialog = td.TranslatorDialog(editor.note.fields[0], defaultSourceLanguage, defaultTargetLanguage, defaultLoadGrammarInfos)
    # if dialog.exec_():
    if dialog.exec():
        vocabs = [vocab[0] for vocab in dialog.translations]
        vocabs = set(vocabs)
        for vocab in vocabs:
            if editor.note.fields[0]:
                editor.note.fields[0] += ",\n"
            editor.note.fields[0] += vocab

        translations = [translation[1] for translation in dialog.translations]
        for translation in translations:
            if editor.note.fields[1]:
                editor.note.fields[1] += ",\n"
            editor.note.fields[1] += translation

        editor.loadNote()


# Definition of the new button
def addTranslationButton(buttons, editor:Editor):
	editor._links['translate'] = onGetTranslation    
	buttons += [editor._addButton(os.path.join(dirname(currentDirName),"Resources/TranslateIcon.png"), "translate","Translate Text")]
	return buttons 

def __init__():
    addHook("setupEditorButtons",addTranslationButton)

