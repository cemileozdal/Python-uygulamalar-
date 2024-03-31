import spacy
from colorama import Fore

nlp = spacy.load("tr_core_web_sm")

text = "Bu rapor, Türkiye'nin Erzurum şehrinde 2024 yılı Şubat ayında hava durumunu analiz ediyor."

doc = nlp(text)

for token in doc:
    if token.is_stop or token.is_punct:
        continue
    
    color = Fore.WHITE
    if token.pos_ == "NOUN":
        color = Fore.RED
    elif token.pos_ == "VERB":
        color = Fore.BLUE
    
    print(color + token.text + Fore.WHITE, end=" ")
