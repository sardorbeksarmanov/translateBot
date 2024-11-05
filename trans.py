from googletrans import Translator

def tarjimon(xabar):
    tarjimonbek = Translator()
    til = tarjimonbek.detect(xabar).lang
    if til == "uz":
        return tarjimonbek.translate(xabar, "en").text
    elif til == "en":
        return tarjimonbek.translate(xabar, "uz").text

