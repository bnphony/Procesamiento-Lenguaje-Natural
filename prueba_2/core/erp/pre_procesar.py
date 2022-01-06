import spacy
from spacy.matcher import Matcher, DependencyMatcher, PhraseMatcher
from spacy.lang.es.stop_words import STOP_WORDS
from core.erp.patterns import * 


from spacy.tokens import Doc, Span, Token
import string

nlp = spacy.load("es_core_news_md")

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



def encontrar_sustantivos(doc):
    matcher_sustantivos = DependencyMatcher(nlp.vocab)

    matcher_sustantivos.add("CON_EL_FIN_DE", [con_el_fin_de])
    matcher_sustantivos.add("CON_EL_FIN", [con_la_finalidad_de])
    matcher_sustantivos.add("SUSTANTIVOS_COMPUESTOS", [sustantivos_compuestos])
    matcher_sustantivos.add("SUS2", [sustantivos_compuestos_2])

    matches = matcher_sustantivos(doc)

    for index, span in enumerate(matches):
        match = matcher_sustantivos(doc)
        if (len(match) != 0):
            start = min(match[0][1])
            end = max(match[0][-1]) + 1
            act = Span(doc, start, end, label="JUNTAR_OPCIONALES")
            with doc.retokenize() as retokenizer:
                retokenizer.merge(act)

def aplicar_dependencias(doc):
    matcher_dependencia = DependencyMatcher(nlp.vocab)
    matcher_dependencia.add("OBJECTO_COMPUESTO", [pattern6])
    matcher_dependencia.add("CASO_IR", [pattern8])
    matcher_dependencia.add("CASO_SIMILAR_AL_IR", [pattern9])
    matcher_dependencia.add("VERBO_OBJ_ACL_OBJ", [pattern13])
    matcher_dependencia.add("VERBO_XCOMP_OBJ_ACL", [pattern19])
    matcher_dependencia.add("VERB_OBJ_ACL", [pattern10])
    matcher_dependencia.add("VERB_OBL_ACL", [pattern18])
    matcher_dependencia.add("VERBO_OBJ_SEGUIDO_ACL", [pattern12])
    matcher_dependencia.add("VERBO_OBJ_OBL_ACL_OBL", [pattern14])
    matcher_dependencia.add("VERBO_OBJ_OBL_ACL", [pattern17])
    matcher_dependencia.add("OBJ_ADVCL_CCOMP_OBJ", [pattern15])
    matcher_dependencia.add("VERBO_OBJ_ADVCL", [pattern20])
    matcher_dependencia.add("VERBO_CCOMP_ADVCL", [pattern21])
    matcher_dependencia.add("VERBO_XCOMP_ADP_VERBO", [pattern22])
    matcher_dependencia.add("VERBO_OBJ_ADP_CASE", [pattern24])
    matcher_dependencia.add("CONSULTAR", [pattern1])
    matcher_dependencia.add("VERBO_OBJETO", [pattern2])
    matcher_dependencia.add("VERBOS_SEGUIDOS", [pattern3])
    matcher_dependencia.add("VERBO_OBL_ADVCL", [pattern11])
    matcher_dependencia.add("VERBO_OBL", [pattern7])
    matcher_dependencia.add("VERBO_NSUBJ", [pattern16])

    matches = matcher_dependencia(doc)

    matches_erroneos = []
    for match_limpiar in matches:
        if nlp.vocab.strings[match_limpiar[0]] in ("VERBO_NSUBJ"):
            if (max(match_limpiar[1]) - min(match_limpiar[1])) > 4 or (match_limpiar[1][0] > match_limpiar[1][-1]):
                matches_erroneos.append(match_limpiar)  # No se borra directamente porque la lista recorreo uno y se salta el proximo valor
        if nlp.vocab.strings[match_limpiar[0]] in ("VERBO_OBL"):
            if (max(match_limpiar[1]) - min(match_limpiar[1])) > 7 or (match_limpiar[1][0] > match_limpiar[1][-1]):
                matches_erroneos.append(match_limpiar)


    # Se borra los matches erroneas asegurando que no se salten los valores
    for match in matches_erroneos:
        matches.remove(match)

    tokens_ids = [token for _, token in matches]
    preview = []
    for index, i in enumerate(tokens_ids):
        preview = i
        for n, oracion in enumerate(tokens_ids[tokens_ids.index(preview) + 1:] + tokens_ids[:tokens_ids.index(preview)]):
            if not set(oracion).isdisjoint(preview):
                valor = list(set(oracion + preview))
                tokens_ids[tokens_ids.index(preview)] = valor
                if oracion in tokens_ids:
                    tokens_ids.remove(oracion)
                preview = valor
                if (doc[preview[0]-1].dep_ == "mark" and index != 0):
                    for n, oracion in enumerate(tokens_ids):
                        if ((min(preview) - max(oracion)) in [0, 1, 2]):
                            valor = list(set(oracion + preview))
                            tokens_ids[tokens_ids.index(preview)] = valor
                            tokens_ids.remove(oracion)
            if (min(oracion) > min(preview) and max(oracion) < max(preview)):
                valor = list(set(oracion + preview))
                tokens_ids[tokens_ids.index(preview)] = valor
                if (oracion in tokens_ids):
                    tokens_ids.remove(oracion)
                preview = valor

    return tokens_ids


def revisar_oraciones(matcher, revision):
    oraciones_revision = []
    lista = [lista.text for lista in revision]
    a = " ".join(lista)
    doc = nlp(a)

    # Buscar y unir sustantivos
    encontrar_sustantivos(doc)

    matches = matcher(doc)
    matches.sort(key = lambda x: x[1])
    for index, match in enumerate(matches):
        oracion = doc[match[1]:match[2]]
        oraciones_revision.append(oracion)

    return oraciones_revision




def procesar(usuario, texto):
    
    doc = nlp(texto)
    
    encontrar_sustantivos(doc)

    tokens_ids = aplicar_dependencias(doc)

    matcher = Matcher(nlp.vocab)
    matcher.add("COMPLEJO", [verbo_sus_adp_verb_noun, verbo_obj], greedy='LONGEST')

    acciones = []

    for indices in tokens_ids:
        revision = Span(doc, min(indices), max(indices)+1, label="ORACION")
        oraciones_encontradas = revisar_oraciones(matcher, revision)
        oracion_busqueda = doc[min(indices):max(indices)+1]

        if len(oraciones_encontradas) > 1:
            for oracion in oraciones_encontradas:
                acciones.append(oracion)
        else:
            if oracion_busqueda[0].pos_ != "VERB":
                for oracion in oraciones_encontradas:
                    acciones.append(oracion)
            else:
                if len(oraciones_encontradas) != 0:
                    acciones.append(oracion_busqueda)


    oraciones = []
    con = ["para", "con la finalidad", "con la finalidad de", "con el fin", "con el fin de", "con el objetivo de",
        "con el objetivo",
        "con el objeto",
        "con el objeto de"
    ]
    for index in range(len(acciones)):
        partes = []
        for token in acciones[index]:
            if token.text in con:
                partes = acciones[index].text.split(token.text)

        if len(partes) > 0:
            oraciones.append({"usuario": usuario, "que": partes[0], "para_que": partes[1]})
        else:
            oraciones.append({"usuario": usuario, "que": acciones[index], "para_que": "sin_proposito"})
    print("oraciones encontradas: ", len(oraciones))
    return oraciones
