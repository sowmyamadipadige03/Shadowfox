from spellchecker import SpellChecker

spell = SpellChecker()

def autocorrect_text(text):
    words = text.split()
    corrected = []
    for word in words:
        if word in spell:
            corrected.append(word)
        else:
            corrected_word = spell.correction(word)
            corrected.append(corrected_word if corrected_word else word)
    return ' '.join(corrected)

