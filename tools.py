import language_check
from client import Paraphraser

def paraphrase(text, level=1):
    # Spell Language Check
    tool = language_check.LanguageTool('en-US')
    matches = tool.check(text)
    corrected_text = language_check.correct(text, matches)
    paraphraser = Paraphraser()
    for i in range(level):
        paraphrased = paraphraser.paraphrase(corrected_text, dest='fr').text
        re_paraphrased = paraphraser.paraphrase(paraphrased).text
        corrected_text = re_paraphrased
    return corrected_text
