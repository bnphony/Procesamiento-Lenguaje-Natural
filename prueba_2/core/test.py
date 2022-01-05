import spacy
from spacy.lang.es import Spanish
from spacy.matcher import Matcher
from spacy.lang.es.stop_words import STOP_WORDS
from spacy. pipeline import EntityRuler
from spacy.language import Language
from spacy.util import filter_spans
from spacy.tokens import Doc, Span, Token
import re
import string


# import speech_recognition as sr
# import time

# #
# # r = sr.Recognizer()
# #
# #
# # with sr.Microphone() as source:
# #     print("Habla ... ")
# #     audio = r.listen(source)
# #
# #     try:
# #         text = r.recognize_google(audio, language='es-ES')
# #         print("Texto reconocido : {} ".format(text))
# #
# #     except:
# #         print("Perdon, pero no entiendo!")
# #
# #
# # lista = text.split()
# # print(lista)
#
#
#
# r = sr.Recognizer()
#
# with sr.AudioFile('prueba_5.wav') as source:
#     audio = r.listen(source)
#
#     try:
#         print("Readion audio file. Please, wait a moment... ")
#         text = r.recognize_google(audio, language='es-ES')
#         #time.sleep(1.5)
#         print(text)
#     except:
#         print("I am sorry I can not understand!")

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

text = "El proceso inicia cuando cualquier empleado presenta una solicitud de vacaciones. Una vez recibida por el supervisor inmediato, quien debe aprobarla o rechazarla, la solicitud se somete a revision final por parte del Departamento de Recursos Humanos y se actualiza automaticamente el sistema de nomina. "
# text = "Hola, quiero ser feliz, para cumplir mis metas."
# text = "Como usuario quiero consultar la lista de pedidos para generar reportes"


puntuacion = string.punctuation + '¡¿'

stopwords_spacy = list(STOP_WORDS)

matcher = Matcher(nlp.vocab)


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
        if token not in stopwords_spacy and token not in puntuacion:
            clean_tokens.append(token)
    # if token not in puntuacion:
    # 	clean_tokens.append(token)

    return clean_tokens


text = text_data_cleaning(text)

text = " ".join(text)

doc = nlp(text)

print(spacy.explain('ADP'))

pattern1 = [
    {"POS": "PROPN", "OP": "?"},
    {"POS": "NOUN", "OP": "?"},
    {"IS_ALPHA": True, "OP": "?"},
    {"POS": "VERB", "OP": "?"},
    {"IS_ALPHA": True, "OP": "?"},
    {"POS": "PROPN", "OP": "*"},
    {"POS": "NOUN", "OP": "*"},
    {"IS_ALPHA": True, "OP": "?"}
]

pattern2 = [
    {"POS": "PROPN", "OP": "?"},
    {"POS": "NOUN", "OP": "?"},
    {"IS_ALPHA": True, "OP": "?"},
    {"POS": "VERB", "OP": "?"},
    {"IS_ALPHA": True, "OP": "?"},
    {"POS": "PROPN", "OP": "?"},
]

pattern3 = [
    {"IS_ALPHA": True, "OP": "?"},
    {"POS": "VERB", "OP": "?"},
    {"IS_ALPHA": True, "OP": "?"}
]

matcher.add("PROPER_NOUNS", [pattern1], greedy='LONGEST')
matches = matcher(doc)
matches.sort(key=lambda x: x[1])


# ruler = nlp.add_pipe("entity_ruler")

@Language.component("agregar_ents")
def agregar_ents(doc):
    original_ents = list(doc.ents)
    for token in doc:
        if token.pos_ in ("NOUN", "PROPN"):
            start, end, name = token.i, token.i + 1, token.text
            per_ent = Span(doc, start, end, label="USER")
            original_ents.append(per_ent)
        # Para colocar la lista de las entidades adicionales
        if token.text.lower() in ("empleado"):
            start, end, name = token.i, token.i + 1, token.text
            per_ent = Span(doc, start, end, label="USER")
            original_ents.append(per_ent)
    fiiltered = filter_spans(original_ents)
    doc.ents = fiiltered
    return (doc)


nlp.add_pipe("agregar_ents")

print(len(matches))

usuarios = []

patterns = []

doc = nlp(text)

preguntas = []

for match in matches:
    span = Span(doc, match[1], match[2], label="ORACION")
    preguntas.append(span)
    print(match, doc[match[1]:match[2]])

# for x in preguntas:
# 	for token in x.ents:
# 		print(token, end=" ")
# 	print()


# WoW pero mira esos pensamientos


# for token in doc:
# 	print(f'{token.text:{10}} {token.pos_:{7}} {token.dep_:{7}} {spacy.explain(token.dep_)}')

for ent in doc.ents:
    print(ent.text, ent.label_)

for token in doc:
    print(token.text, token.dep_, token.head, token.pos_)





