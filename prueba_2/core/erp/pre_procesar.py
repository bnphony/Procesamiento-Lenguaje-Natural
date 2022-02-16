import spacy
from spacy.matcher import Matcher, DependencyMatcher, PhraseMatcher
from spacy.lang.es.stop_words import STOP_WORDS
from core.erp.patterns import *

from spacy.tokens import Doc, Span, Token
import string

import numpy as np

nlp = spacy.load("es_core_news_md")

usuario = "usuario"
que = ""
para_que = ""

text = ""


puntuacion = string.punctuation + '!¿'
stopwords_spacy = list(STOP_WORDS)

stop_words = ['cual', 'este', 'luego']
separadores = ("ademas", "tambien", "asimismo", "conjuntamente", "adicionalmente",
               "encima", "igualmente", "asi mismo", "por añadidura", "de la misma manera",
               "del mismo modo", "de igual forma", "por otra parte", "de la misma forma", "de igual modo",
               "de igual manera")

# Componentes para quitar las tildes
a, b = "áíúéóÁÍÚÉÓ", "aiueoAIUEO"
trans = str.maketrans(a, b)


def text_data_cleaning(oracion):
    # Quitar las tildes
    oracion = oracion.lower()  # Transformar todo a minisculas
    oracion = oracion.translate(trans)

    doc = nlp(oracion)
    encontrar_separadores(doc)
    tokens = []
    for token in doc:
        if token.lemma_ in ("quiero", "querer", "necesitar", "desear", "permitir"):
            aux = "."
        elif token.text in separadores:
            aux = token.text.strip().lower()
            tokens.append(".")

        else:
            aux = token.text.strip().lower()
        tokens.append(aux)
    clean_tokens = []
    for token in tokens:
        if token not in stop_words and token not in puntuacion and token not in (
                "querer", "necesitar", "desear", "permitir"):
            clean_tokens.append(token)
        if token in ("$", "."):
            clean_tokens.append(token)
    return clean_tokens


def text_limpio(oracion):
    tokens = []

    for token in oracion:
        if (not isinstance(token, spacy.tokens.token.Token)):
            aux = token.strip().lower()
            tokens.append(aux)
            continue
        if (token.lemma_ in ("querer", "necesitar", "desear", "permitir")):
            aux = token.lemma_.strip().lower()
        else:
            aux = token.text.strip().lower()
        tokens.append(aux)

    tokens_limpios = []
    for token in tokens:
        if token not in puntuacion and token not in (
                "querer", "necesitar", "desear", "permitir") and token not in stop_words:
            tokens_limpios.append(token)
        if token in ("$"):
            tokens_limpios.append(token)

    return tokens_limpios


def encontrar_separadores(doc):
    matcher_separadores = PhraseMatcher(nlp.vocab, validate=True)
    separadores = ("asi mismo", "por añadidura", "de la misma manera",
                   "del mismo modo", "por otra parte", "de igual forma", "de la misma forma", "de igual modo",
                   "de igual manera")
    patterns = [nlp.make_doc(text) for text in separadores]
    matcher_separadores.add("SEPARADORES", patterns)

    matches = matcher_separadores(doc)
    tokens_ids = [(start, end) for _, start, end in matches]

    resultado = 0
    l = tokens_ids
    l = sorted(l)

    for index, span in enumerate(tokens_ids):
        match = [(np.array(match1) - resultado) for match1 in l]
        comienzo = len(doc)
        if len(match) != 0:
            start = min(match[0])
            end = max(match[0])
            act = Span(doc, start, end, label="SEPARADORES")
            with doc.retokenize() as retokenizer:
                retokenizer.merge(act)
        final = len(doc)
        resultado = (comienzo - final)
        match.remove(match[0])
        l = match


def limpiar_encontrar_sustantivos(matches, doc):
    matches_erroneos = []
    for match in matches:
        if (max(match[1]) - min(match[1])) > 6:
            matches_erroneos.append(match)
        verbos = [token.text for token in doc[min(match[1]):max(match[1])] if token.pos_ == "VERB"]
        if len(verbos) > 0:
            matches_erroneos.append(match)

    for eliminar in matches_erroneos:
        if eliminar in matches:
            matches.remove(eliminar)

    preview = []
    tokens_ids = [token for _, token in matches]
    for index, i in enumerate(tokens_ids):
        preview = i
        for oracion in (tokens_ids[tokens_ids.index(preview) + 1:] + tokens_ids[:tokens_ids.index(preview)]):
            if not set(oracion).isdisjoint(preview):
                valor = list(set(oracion + preview))
                tokens_ids[tokens_ids.index(preview)] = valor
                if oracion in tokens_ids:
                    tokens_ids.remove(oracion)
                preview = valor
            if (min(oracion) > min(preview) and max(oracion) < max(preview)):
                valor = list(set(oracion + preview))
                tokens_ids[tokens_ids.index(preview)] = valor
                if (oracion in tokens_ids):
                    tokens_ids.remove(oracion)
                preview = valor

    return tokens_ids


def encontrar_sustantivos(doc, patterns):
    matcher_sustantivos = DependencyMatcher(nlp.vocab)

    matcher_sustantivos.add("CON_EL_FIN_DE", [con_el_fin_de])
    matcher_sustantivos.add("CON_EL_FIN", [con_la_finalidad_de])
    matcher_sustantivos.add("PROPN_NUMMOD", [propn_nummod])
    matcher_sustantivos.add("SUSTANTIVOS_COMPUESTOS", [sustantivos_compuestos])
    matcher_sustantivos.add("SUS2", [sustantivos_compuestos_2, sustantivos_compuestos_3])

    if len(patterns) > 0:
        matcher_sustantivos.add("NOUN_CONJ", [pattern38])
        matcher_sustantivos.add("NOUN_NMOD_ACL", [pattern34])
        matcher_sustantivos.add("NOUN_AMOD_NMOD_ACL", [pattern35])
        matcher_sustantivos.add("NOUN_NMOD_NUMMOD", [pattern36])
        matcher_sustantivos.add("NOUN_NUMMOD", [pattern37])

    matches = matcher_sustantivos(doc)
    matches = limpiar_encontrar_sustantivos(matches, doc)


    resultado = 0
    l = matches
    l = sorted(l)
    for index, span in enumerate(matches):
        match = [(np.array(match1) - resultado) for match1 in l]
        comienzo = len(doc)
        if (len(match) != 0):
            start = min(match[0])
            end = max(match[0]) + 1
            act = Span(doc, start, end, label="JUNTAR_OPCIONALES")
            # print(act)
            with doc.retokenize() as retokenizer:
                retokenizer.merge(act)
        final = len(doc)
        resultado = (comienzo - final)
        match.remove(match[0])
        l = match


def aplicar_dependencias(doc):
    matcher_dependencia = DependencyMatcher(nlp.vocab, validate=True)
    matcher_dependencia.add("OBJECTO_COMPUESTO", [pattern6])
    matcher_dependencia.add("CASO_IR", [pattern8])
    matcher_dependencia.add("CASO_SIMILAR_AL_IR", [pattern9])
    matcher_dependencia.add("VERBO_OBJ_ACL_OBJ", [pattern13])
    matcher_dependencia.add("VERBO_XCOMP_OBJ_ACL", [pattern19])
    matcher_dependencia.add("VERB_OBJACL", [pattern10])
    matcher_dependencia.add("VERB_OBJ_ACL_ACL", [pattern28])
    matcher_dependencia.add("VERB_OBL_ACL", [pattern18])
    matcher_dependencia.add("VERBO_OBJ_SEGUIDO_ACL", [pattern12])
    matcher_dependencia.add("VERBO_OBJ_OBL_ACL_OBL", [pattern14])
    matcher_dependencia.add("VERBO_OBJOBLADVMOD", [pattern39])
    matcher_dependencia.add("VERBO_OBJ_ACL_ADVCL_OBJ", [pattern25])
    matcher_dependencia.add("VERBO_NSUBJ_ACL_OBJ_OBJ", [pattern26])
    matcher_dependencia.add("VERBO_OBJ_NMOD_ACL_CCOMP", [pattern27])
    matcher_dependencia.add("VERBO_OBJ_OBL_ACL", [pattern17])
    matcher_dependencia.add("OBJ_ADVCL_CCOMP_OBJ", [pattern15])
    matcher_dependencia.add("VERBO_OBJ_ADVCL", [pattern20]) # OBJ = ["OBJ", "OBL"]
    matcher_dependencia.add("VERBO_ADVCL_OBJ", [pattern30])
    matcher_dependencia.add("VERBO_OBJ_NMOD_ACL", [pattern44])
    matcher_dependencia.add("VERBO_CCOMP_ADVCL", [pattern21])
    matcher_dependencia.add("VERBO_CCOMP_CONJ", [pattern29])  # CONJ = ["conj", "acl"]
    matcher_dependencia.add("VERBO_CONJ_OBJ", [pattern31])
    matcher_dependencia.add("VERBO_XCOMP_ADP_VERBO", [pattern22])
    matcher_dependencia.add("VERBO_CCOMP_NSUBJ_ACL", [pattern40])
    matcher_dependencia.add("VERBO_OBJ_ADP_CASE", [pattern24])
    matcher_dependencia.add("CONSULTAR", [pattern1])
    matcher_dependencia.add("VERBO_OBJETO", [pattern2])
    matcher_dependencia.add("VERBOS_SEGUIDOS", [pattern3])
    matcher_dependencia.add("VERBO_OBL_ADVCL", [pattern11])
    matcher_dependencia.add("VERBO_OBL", [pattern7])
    matcher_dependencia.add("VERBO_NSUBJ", [pattern16])
    matcher_dependencia.add("VERBO_NSUBJ_APPOS_COMPOUND", [pattern45])
    matcher_dependencia.add("VERBO_CCOMP", [pattern41])
    matcher_dependencia.add("NOUN_CCONJ_NOUN", [pattern32])
    matcher_dependencia.add("NOUN_AMOD_ACL", [pattern33])
    matcher_dependencia.add("NOUN_NMOD_ACL", [pattern34])
    matcher_dependencia.add("NOUN_APPOS_CONJ_OBJ", [pattern42])
    matcher_dependencia.add("NOUN_AMOD_NMOD_ACL", [pattern35])
    matcher_dependencia.add("NOUN_NMOD_NUMMOD", [pattern36])
    matcher_dependencia.add("NOUN_NUMMOD", [pattern37])
    matcher_dependencia.add("ADJ_NSUBJ_NMOD_ACL", [pattern43])
    matcher_dependencia.add("COMPVERB_ADVMOD_FIXED", [pattern46])

    matches = matcher_dependencia(doc)

    matches_erroneos = []
    for match_limpiar in matches:
        if nlp.vocab.strings[match_limpiar[0]] in ("VERBO_NSUBJ"):
            if (max(match_limpiar[1]) - min(match_limpiar[1])) > 4 or (match_limpiar[1][0] > match_limpiar[1][-1]):
                matches_erroneos.append(
                    match_limpiar)  # No se borra directamente porque la lista recorreo uno y se salta el proximo valor
        if nlp.vocab.strings[match_limpiar[0]] in ("VERBO_OBL", "VERBO_OBJETO", "VERBO_CCOMP"):
            if (max(match_limpiar[1]) - min(match_limpiar[1])) > 7 or (match_limpiar[1][0] > match_limpiar[1][-1]):
                matches_erroneos.append(match_limpiar)
        if nlp.vocab.strings[match_limpiar[0]] in ("VERBO_CCOMP_ADVCL"):  # Se agrego ultimo
            if (match_limpiar[1][1] - min(match_limpiar[1]) > 3):
                matches_erroneos.append(match_limpiar)
        if nlp.vocab.strings[match_limpiar[0]] in ("VERBO_NSUBJ_ACL_OBJ_OBJ"):  # Se agrego ultimo
            if (max(match_limpiar[1][:2]) - min(match_limpiar[1][:2]) > 3):
                matches_erroneos.append(match_limpiar)
        if nlp.vocab.strings[match_limpiar[0]] in ("VERBO_ADVCL_OBJ"):
            if (match_limpiar[1][1] - min(match_limpiar[1]) > 5):
                matches_erroneos.append(match_limpiar)
        if nlp.vocab.strings[match_limpiar[0]] in ("VERBO_OBJ_ADVCL"):
            if (max(match_limpiar[1]) - min(match_limpiar[1]) > 7):
                matches_erroneos.append(match_limpiar)
        if nlp.vocab.strings[match_limpiar[0]] in ("CONSULTAR"):
            if (match_limpiar[1][2] - min(match_limpiar[1]) > 7):
                matches_erroneos.append(match_limpiar)

    # Se borra los matches erroneas asegurando que no se salten los valores
    for match in matches_erroneos:
        if match in matches:
            matches.remove(match)

    # # OJO -----------------------------
    # # Funcion para escoger solo la primera busqueda del mismo matcher
    # preview = []
    # matches_erroneos = []
    for oracion in matches:
        preview = oracion
        for index, i in enumerate(matches[matches.index(preview) + 1:] + matches[:matches.index(preview)]):
            if (not set(i[1]).isdisjoint(preview[1])) and nlp.vocab.strings[i[0]] == nlp.vocab.strings[preview[0]]:
                matches.remove(i)

    # OJO ---------
    # Funcion para eliminar las busquedas que no esten en orden
    matches_erroneos = []
    for match_limpiar in matches:
        if (match_limpiar[1] != sorted(match_limpiar[1])):
            # print("MATCHER DESORDENADO:", match_limpiar[1])
            # print("MATCHER ORDENADO: ", sorted(match_limpiar[1]))
            matches_erroneos.append(match_limpiar)

    # Eliminar los match erroneos que se se encontraron
    for match in matches_erroneos:
        matches.remove(match)

    tokens_ids = [token for _, token in matches]
    preview = []
    for index, i in enumerate(tokens_ids):
        preview = i
        for n, oracion in enumerate(
                tokens_ids[tokens_ids.index(preview) + 1:] + tokens_ids[:tokens_ids.index(preview)]):
            if not set(oracion).isdisjoint(preview):
                valor = list(set(oracion + preview))
                if preview in tokens_ids:
                    tokens_ids[tokens_ids.index(preview)] = valor
                if oracion in tokens_ids:
                    tokens_ids.remove(oracion)
                preview = valor

            if (min(oracion) > min(preview) and max(oracion) < max(preview)):
                valor = list(set(oracion + preview))
                tokens_ids[tokens_ids.index(preview)] = valor
                if (oracion in tokens_ids):
                    tokens_ids.remove(oracion)
                preview = valor

    # Segunda comprobacion si todavia existe valores
    preview = []
    for index, i in enumerate(tokens_ids):
        preview = i
        for n, oracion in enumerate(
                tokens_ids[tokens_ids.index(preview) + 1:] + tokens_ids[:tokens_ids.index(preview)]):
            if (not set(oracion).isdisjoint(preview)):
                valor = list(set(oracion + preview))
                if preview in tokens_ids:
                    tokens_ids[tokens_ids.index(preview)] = valor
                if (oracion in tokens_ids):
                    tokens_ids.remove(oracion)
                preview = valor

            if (min(oracion) > min(preview) and max(oracion) < max(preview)):
                valor = list(set(oracion + preview))
                tokens_ids[tokens_ids.index(preview)] = valor
                if (oracion in tokens_ids):
                    tokens_ids.remove(oracion)
                preview = valor



    return tokens_ids


def revisar_oraciones(doc):
    oraciones_encontradas = []
    matcher_reglas = Matcher(nlp.vocab)
    matcher_reglas.add("COMPLEJO", [verbo_sus_adp_verb_noun], greedy='LONGEST')
    matcher_reglas.add("VERBO_PARA_QUE", [verbo_para_que], greedy='LONGEST')
    matcher_reglas.add("VERBO_OBJ", [verbo_obj], greedy='LONGEST')
    matcher_reglas.add("ORACION_SIMPLE_2", [oracion_simple_2], greedy='LONGEST')
    matcher_reglas.add("VERBO_A_VERBO", [verbo_a_verbo], greedy='LONGEST')
    matcher_reglas.add("ADJ_DET_NOUN_VERB", [adj_det_noun_verbo], greedy='LONGEST')
    matcher_reglas.add("VERBO_ADP_VERBO", [verbo_adp_verbo], greedy='LONGEST')
    matcher_reglas.add("VERBO_CON_QUE", [verbo_con_que], greedy='LONGEST')
    matcher_reglas.add("VERBO_OBJ_CAUSA", [verbo_obj_causa], greedy='LONGEST')
    matcher_reglas.add("VERBO_N", [verbo_n], greedy='LONGEST')
    matcher_reglas.add("VERBO_O_VERBO", [verbo_o_verbo], greedy='LONGEST')

    matches = matcher_reglas(doc)

    matches_erroneos = []
    for match in matches:
        if (match[2] - match[1]) > 10:
            matches_erroneos.append(match)

    for match in matches_erroneos:
        matches.remove(match)

    matches.sort(key=lambda x: x[1])
    preview = []
    tokens_ids = [[start, end] for _, start, end in matches]
    # print(tokens_ids)
    for index, i in enumerate(tokens_ids):
        preview = i
        for oracion in (tokens_ids[tokens_ids.index(preview) + 1:] + tokens_ids[:tokens_ids.index(preview)]):
            if oracion[0] == preview[0] or oracion[0] > preview[0] and oracion[0] < preview[1]:
                valor = list(set(oracion + preview))
                tokens_ids[tokens_ids.index(preview)] = [min(valor), max(valor)]
                if oracion in tokens_ids:
                    tokens_ids.remove(oracion)
                preview = [min(valor), max(valor)]

    for match in tokens_ids:
        oracion = doc[match[0]:match[1]]
        limpiar = oracion[-2:]
        if limpiar[0].text in ("que") and limpiar[1].pos_ == "NOUN":
            oracion = doc[match[0]:match[1] - 2]
        if limpiar[1].pos_ in ("ADP", "AUX") and limpiar[1].lemma_ not in ("poder"):
            oracion = doc[match[0]:match[1] + 1]
        if limpiar[1].lemma_ in ("poder") and limpiar[1].pos_ in ("ADP", "AUX"):
            oracion = doc[match[0]:match[1] - 1]
        oraciones_encontradas.append(oracion)
    # print("ORACIONES ENCONTRADAS:")
    # print(oraciones_encontradas)
    return oraciones_encontradas


con = ["para", "con la finalidad", "con la finalidad de", "con el fin", "con el fin de", "con el objetivo de",
       "con el objetivo",
       "con el objeto",
       "con el objeto de"
       ]


def revisar(usuario, oracion_que, oracion_para_que):
    oraciones_encontradas = []
    doc1 = nlp(oracion_que)
    doc2 = nlp(oracion_para_que)
    patterns = [pattern32, pattern33, pattern34, pattern35, pattern36, pattern37]
    encontrar_sustantivos(doc1, patterns)
    encontrar_sustantivos(doc2, patterns)
    oraciones1 = revisar_oraciones(doc1)
    oraciones2 = revisar_oraciones(doc2)

    if (len(oraciones1) > 1):
        for index, i in enumerate(oraciones1):
            if index > 0:
                if oraciones1[index][0].head.text == oraciones1[index - 1][-1].text or oraciones1[index][0].head.text == \
                        oraciones1[index - 1][0].text:
                    oraciones1[index - 1] = doc1[oraciones1[index - 1][0].i:oraciones1[index][-1].i + 1]
                    oraciones1.remove(i)

    if (len(oraciones1) == 1 and len(oraciones2) == 1):
        return None

    if (len(oraciones1) == 0) and (len(oraciones2) == 0):
        return None

    if (len(oraciones1) == 1 and len(oraciones2) == 0):
        return None



    for index, i in enumerate(oraciones1):
        if (index == len(oraciones1) - 1 and len(oraciones2) > 0):
            oraciones_encontradas.append({"usuario": usuario, "que": oraciones1[index], "para_que": oraciones2[0]})
            continue
        if (index < len(oraciones1)):
            oraciones_encontradas.append({"usuario": usuario, "que": oraciones1[index], "para_que": "sin_proposito"})

    if (len(oraciones2) > 2):
        for index, i in enumerate(oraciones2):
            if index > 1:
                if oraciones2[index][0].head.text == oraciones2[index - 1][-1].text or oraciones2[index][0].head.text == \
                        oraciones2[index - 1][0].text or oraciones2[index][0].head.text == oraciones2[index - 1][
                    -1].head.text:
                    oraciones2[index - 1] = doc2[oraciones2[index - 1][0].i:oraciones2[index][-1].i + 1]
                    oraciones2.remove(i)

    for index in range(len(oraciones2)):
        partes = []
        if index > 0:
            for token in oraciones2[index]:
                if token.text in con:
                    partes = oraciones2[index].text.split(token.text)

            if len(partes) > 0:
                oraciones_encontradas.append({"usuario": usuario, "que": partes[0], "para_que": partes[1]})
            else:
                oraciones_encontradas.append(
                    {"usuario": usuario, "que": oraciones2[index], "para_que": "sin_proposito"})

    return oraciones_encontradas


def pre_procesar_oraciones(usuario, oracion):
    que = []
    para_que = []
    para = 0
    con_que = (
    "para", "con la finalidad", "con el finalidad", "con el objetivo", "con el objeto", "con el fin", "poder")
    for token in oracion.as_doc():
        if (token.pos_ == "VERB" and para == 0):
            para += 1
            for parte in oracion[token.i:]:
                if parte.lemma_ not in con_que:
                    que.append(parte)
                else:
                    para += 1
                    break
        if (token.lemma_ in con_que):
            para_que.append(token)
            for parte in oracion[token.i + 1:]:
                if parte.lemma_ not in con_que:
                    para_que.append(parte)
                else:
                    break

    oracion_que = " ".join(text_limpio(que))
    oracion_para_que = " ".join(text_limpio(para_que))
    oraciones = revisar(usuario, oracion_que, oracion_para_que)
    if oraciones is None:

        oraciones = []
        partes = []
        for i in oracion:
            if i.text in con_el_objeto:
                partes = oracion.text.split(" " + i.text + " ")
        if len(partes) > 0:
            oraciones.append({"usuario": usuario, "que": partes[0], "para_que": partes[1]})
        else:
            oraciones.append({"usuario": usuario, "que": oracion, "para_que": "sin_proposito"})
    return oraciones


def procesar(usuario, texto):
    text = text_data_cleaning(texto)
    texto = " ".join(text)
    doc = nlp(texto)
    patterns = [pattern32, pattern33, pattern34, pattern35, pattern36, pattern37]

    encontrar_sustantivos(doc, patterns)

    tokens_ids = aplicar_dependencias(doc)
    print(tokens_ids)
    oraciones_sin_limpiar = []
    for index, indices in enumerate(tokens_ids):
        oracion_busqueda = doc[min(indices):max(indices) + 1]
        if index > 0:
            if (oracion_busqueda[0].head.text in con_el_objeto):
                oraciones_sin_limpiar[index - 1] = doc[min(tokens_ids[index - 1]):max(indices) + 1]
                continue
        oraciones_sin_limpiar.append(oracion_busqueda)
        print("SENTENCE:", oracion_busqueda)


    # Encontrar los grupos de los sustantivos relacionados
    resultado = 0
    contador = 0
    grupos = []
    sustantivos = [token for token in doc if token.pos_ == "NOUN"]
    # print(sustantivos)
    for index, token in enumerate(sustantivos):
        if token.pos_ == "NOUN":
            for i in sustantivos[index + 1:]:
                resultado = token.similarity(i)
                # print(f"el sustantivo < {token} > es similar a < {i} > con < {resultado} >")
                if (resultado > 0.75):
                    grupos.append([token, i])
                    contador += 1

    # print(grupos)
    preview = []
    for index, grupo in enumerate(grupos):
        preview = grupo
        for sus in (grupos[:grupos.index(preview)] + grupos[grupos.index(preview) + 1:]):
            if not set(sus).isdisjoint(preview):
                valor = list(set(preview + sus))
                if sus in grupos:
                    grupos.remove(sus)
                grupos[grupos.index(preview)] = valor
                preview = valor
    print(grupos)

    oraciones = []
    for oracion in oraciones_sin_limpiar:
        oraciones1 = pre_procesar_oraciones(usuario, oracion)
        for i in oraciones1:
            oraciones.append(i)
            # print(i)

    for index, oracion in enumerate(oraciones):
        oracion['grupo'] = 0
        oracion['nombre'] = 'H' + str(index + 1)

    for oracion in oraciones:
        if not isinstance(oracion['que'], spacy.tokens.span.Span) and not isinstance(oracion['que'], spacy.tokens.doc.Doc):
            oracion['que'] = nlp(oracion['que'])
            encontrar_sustantivos(oracion['que'], patterns)
            oracion['que'] = oracion['que'][:]

    resultado = 0

    for index, oracion in enumerate(oraciones):
        sustantivo = [token for token in oracion['que'] if token.pos_ == "NOUN"]

        for n, i in enumerate(grupos):
            if len(sustantivo) > 0:
                for palabra in i:
                    for aux in sustantivo:
                        resultado = aux.similarity(palabra)
                        if (resultado > 0.85):
                            oracion['grupo'] = n + 1
                            break

    print("oraciones encontradas: ", len(oraciones))


    return oraciones
