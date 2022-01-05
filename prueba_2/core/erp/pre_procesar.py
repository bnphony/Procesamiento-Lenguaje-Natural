import spacy
from spacy.lang.es import Spanish
from spacy.matcher import Matcher
from spacy.lang.es.stop_words import STOP_WORDS
from spacy.pipeline import EntityRuler

from spacy.language import Language
from spacy.util import filter_spans

from spacy.tokens import Doc, Span, Token
import re
import string

nlp = spacy.load("es_core_news_sm")

usuario = ""
que = ""
para_que = ""

text = ""

puntuacion = string.punctuation + '!¿'
stopwords_spacy = list(STOP_WORDS)




def text_data_cleaning(oracion):
    doc = nlp(oracion)
    tokens = []

    for token in doc:
        if token.lemma_ != "-PRON-":
            temp = token.text.strip()
        else:
            temp = token

        tokens.append(temp)

    clean_tokens = []
    for token in tokens:
        if token in ('para', 'para.', 'para,', 'para_', 'con', 'ir', 'realizar'):
            clean_tokens.append(token)
        if token not in stopwords_spacy and token not in puntuacion and token not in ('o'):
            clean_tokens.append(token)

    return clean_tokens

def text_limpio(oracion):
    doc = nlp(oracion)
    tokens = []

    for token in doc:
        if (token.lemma_) in ("querer", "necesitar", "desear"):
            aux = token.lemma_.strip().lower()
        else:
            aux = token.text.strip().lower()
        tokens.append(aux)

    tokens_limpios = []
    for token in tokens:
        if token not in puntuacion and token not in ("querer", "necesitar", "desear", "poder"):
            tokens_limpios.append(token)

    return tokens_limpios



pattern1 = [
    {"POS": {"IN": ["VERB"]}, "OP": "+"},
    {"POS": {"NOT_IN": ["VERB"]}, "OP": "+"}
]


pattern2 = [
    {"POS": {"IN": ["VERB", "ADJ"]}, "OP": "+"},
    {"IS_ALPHA": True, "OP": "?"},
    {"POS": "PROPN", "OP": "?"},
    {"POS": "NOUN", "OP": "?"},
    {"POS": {"NOT_IN": ["VERB"]}, "OP": "+"},
    {"LOWER": {"IN": ["para", "con la finalidad", "con la finalidad de", "con el fin", "con el fin de"]}, "OP": "+"},
    {"POS": "VERB", "OP": "+"},
    {"POS": {"NOT_IN": ["VERB", "ADV"]}, "OP": "+"}
]
verbos_opcionales = [
    {"POS": "VERB"},
    {"LOWER": {"IN": ["o", "y"]}},
    {"POS": "VERB"}
]

con_el_fin = [
    {"LOWER": "con"},
    {"LOWER": {"IN": ["el", "la"]}, "OP": "?"},
    {"LOWER": {"IN": ["fin", "finalidad"]}},
    {"LOWER": "de", "OP": "+"}
]





def procesar(usuario, texto):
    text = text_limpio(texto)
    text = " ".join(text)

    matcher = Matcher(nlp.vocab)

    doc = nlp(text)
    matcher.add("VERBOS_OPCIONALES", [verbos_opcionales])
    matcher.add("CON_EL_FIN", [con_el_fin])


    matches = matcher(doc)


    juntar_opcionales = []
    for match in matches:
        span = Span(doc, match[1], match[2], label="JUNTAR_OPCIONALES")
        juntar_opcionales.append(span)

    matcher.remove("VERBOS_OPCIONALES")
    matcher.remove("CON_EL_FIN")

    matcher.add("ACCIONES", [pattern2, pattern1], greedy='LONGEST')
    for span in juntar_opcionales:
        with doc.retokenize() as retokenizer:
            retokenizer.merge(span)

    matches = matcher(doc)
    matches.sort(key=lambda x: x[1])
    preguntas = []
    acciones = []



    for match in matches:
        span = Span(doc, match[1], match[2], label="ACCION")
        preguntas.append(span)

    for token in range(len(preguntas)):
        partes = []
        for i in preguntas[token]:
            if i.text in ("para", "con la finalidad", "con la finalidad de", "con el fin", "con el fin de"):
                partes = preguntas[token].text.split(i.text)

        if len(partes) > 0:
            acciones.append({"usuario": usuario, "que": partes[0], "para_que": partes[1]})
        else:
            acciones.append({"usuario": usuario, "que": preguntas[token].text, "para_que": "sin_proposito"})

    return acciones
