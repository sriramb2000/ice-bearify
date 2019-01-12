import spacy

def ice_bearify(text):
    nlp = spacy.load('en')
    doc = nlp(unicode(text, "utf-8"))
    #find subjects in text
    sub_toks = [tok for tok in doc if (tok.dep_ == "nsubj")]
    for tok in sub_toks:
        text = text.replace(str(tok),"Ice Bear")
    return text

print(ice_bearify("In searching for the ship Robert was unsuccessful."))
