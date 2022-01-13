import spacy
from spacy.matcher import Matcher, DependencyMatcher, PhraseMatcher
from spacy.lang.es.stop_words import STOP_WORDS
from core.erp.patterns import *

from spacy.tokens import Doc, Span, Token
import string

nlp = spacy.load("es_core_news_md")

usuario = "usuario"
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


stop_words = ['la', 'cual', 'se', 'este']
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
        if token not in puntuacion and token not in ("querer", "necesitar", "desear", "permitir") and token not in stop_words:
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
            if len(act) > 5:
                continue
            with doc.retokenize() as retokenizer:
                retokenizer.merge(act)


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
    matcher_dependencia.add("VERBO_OBJ_ACL_ADVCL_OBJ", [pattern25])
    matcher_dependencia.add("VERBO_NSUBJ_ACL_OBJ_OBJ", [pattern26])
    matcher_dependencia.add("VERBO_OBJ_NMOD_ACL_CCOMP", [pattern27])
    matcher_dependencia.add("VERBO_OBJ_OBL_ACL", [pattern17])
    matcher_dependencia.add("OBJ_ADVCL_CCOMP_OBJ", [pattern15])
    matcher_dependencia.add("VERBO_OBJ_ADVCL", [pattern20])
    matcher_dependencia.add("VERBO_ADVCL_OBJ", [pattern30])
    matcher_dependencia.add("VERBO_CCOMP_ADVCL", [pattern21])
    matcher_dependencia.add("VERBO_CCOMP_CONJ", [pattern29])
    matcher_dependencia.add("VERBO_XCOMP_ADP_VERBO", [pattern22])
    matcher_dependencia.add("VERBO_OBJ_ADP_CASE", [pattern24])
    matcher_dependencia.add("CONSULTAR", [pattern1])
    matcher_dependencia.add("VERBO_OBJETO", [pattern2])
    matcher_dependencia.add("VERBOS_SEGUIDOS", [pattern3])
    matcher_dependencia.add("VERBO_OBL_ADVCL", [pattern11])
    matcher_dependencia.add("VERBO_OBL", [pattern7])
    matcher_dependencia.add("VERBO_NSUBJ", [pattern16])

    matches = matcher_dependencia(doc)
    print([(nlp.vocab.strings[match_id], tokens_ids) for match_id, tokens_ids in matches])
    # OJO -----------------------------
    # Funcion para escoger solo la primera busqueda del mismo matcher
    preview = []
    for oracion in matches:
        preview = oracion
        for index, i in enumerate(matches[matches.index(preview) + 1:] + matches[:matches.index(preview)]):
            if (not set(i[1]).isdisjoint(preview[1])) and nlp.vocab.strings[i[0]] == nlp.vocab.strings[preview[0]] and nlp.vocab.strings[i[0]] in ("VERBO_OBJETO", "VERBO_OBL", "VERBO_NSUBJ"):
                matches.remove(i)

    # OJO ---------
    # Funcion para eliminar las busquedas que no esten en orden
    # matches_erroneos = []
    # for match_limpiar in matches:
    #     if (match_limpiar[1] != sorted(match_limpiar[1])):
    #         # print("MATCHER DESORDENADO:", match_limpiar[1])
    #         # print("MATCHER ORDENADO: ", sorted(match_limpiar[1]))
    #         matches_erroneos.append(match_limpiar)

    # Eliminar los match erroneos que se se encontraron
    # for match in matches_erroneos:
    #     matches.remove(match)

    matches_erroneos = []
    for match_limpiar in matches:
        if nlp.vocab.strings[match_limpiar[0]] in ("VERBO_NSUBJ"):
            if (max(match_limpiar[1]) - min(match_limpiar[1])) > 4 or (match_limpiar[1][0] > match_limpiar[1][-1]):
                matches_erroneos.append(match_limpiar)  # No se borra directamente porque la lista recorreo uno y se salta el proximo valor
        if nlp.vocab.strings[match_limpiar[0]] in ("VERBO_OBL", "VERBO_OBJETO"):
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
                # print("ORACION: ", oracion)
                # print("PREVIEW: ", preview)
                valor = list(set(oracion + preview))
                tokens_ids[tokens_ids.index(preview)] = valor
                if oracion in tokens_ids:
                    tokens_ids.remove(oracion)
                # print("nuevo valor creado: ", tokens_ids)
                preview = valor
                if (doc[preview[0] - 1].dep_ == "mark" and index != 0):
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

    # Segunda comprobacion si todavia existe valores
    preview = []
    for index, i in enumerate(tokens_ids):
        preview = i
        for n, oracion in enumerate(tokens_ids[tokens_ids.index(preview) + 1:] + tokens_ids[:tokens_ids.index(preview)]):
            if (not set(oracion).isdisjoint(preview)):
                valor = list(set(oracion + preview))
                tokens_ids[tokens_ids.index(preview)] = valor
                if (oracion in tokens_ids):
                    tokens_ids.remove(oracion)
                preview = valor
                if (doc[preview[0] - 1].dep_ == "mark" and index != 0):
                    for n, oracion in enumerate(tokens_ids):
                        if ((min(preview) - max(oracion)) in [0, 1, 2]):
                            print("Entro para ver")
                            valor = list(set(oracion + preview))
                            tokens_ids[index] = valor
                            # tokens_ids_sin_corregir.remove(preview)
                            tokens_ids.remove(oracion)
            if (min(oracion) > min(preview) and max(oracion) < max(preview)):
                valor = list(set(oracion + preview))
                tokens_ids[tokens_ids.index(preview)] = valor
                if (oracion in tokens_ids):
                    tokens_ids.remove(oracion)
                preview = valor
    print("LUEGO DE CORREGIR")
    print([(nlp.vocab.strings[match_id], tokens_ids) for match_id, tokens_ids in matches])
    print([(token.i, token, token.pos_) for token in doc])

    return tokens_ids


def revisar_oraciones(doc):
    oraciones_encontradas = []
    matcher_reglas = Matcher(nlp.vocab)
    matcher_reglas.add("COMPLEJO", [verbo_sus_adp_verb_noun, verbo_obj, oracion_simple_2, verbo_a_verbo, verbo_adp_verbo, verbo_con_que, verbo], greedy='LONGEST')

    matches = matcher_reglas(doc)
    matches.sort(key=lambda x: x[1])
    for index, match in enumerate(matches):
        oracion = doc[match[1]:match[2]]
        oraciones_encontradas.append(oracion)

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
    print(doc1)
    print(doc2)
    encontrar_sustantivos(doc1)
    encontrar_sustantivos(doc2)
    oraciones1 = revisar_oraciones(doc1)
    oraciones2 = revisar_oraciones(doc2)

    if (len(oraciones1) > 1):
        for index, i in enumerate(oraciones1):
            if index > 0:
                if oraciones1[index][0].head.text == oraciones1[index - 1][-1].text:
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


    for index in range(len(oraciones2)):
        partes = []
        if index > 0:
            for token in oraciones2[index]:
                if token.text in con:
                    partes = oraciones2[index].text.split(token.text)

            if len(partes) > 0:
                oraciones_encontradas.append({"usuario": usuario, "que": partes[0], "para_que": partes[1]})
            else:
                oraciones_encontradas.append({"usuario": usuario, "que": oraciones2[index], "para_que": "sin_proposito"})

    return oraciones_encontradas


def pre_procesar_oraciones(usuario, oracion):
    que = []
    para_que = []
    para = 0
    con_que = ("para", "con la finalidad", "con el finalidad", "con el objetivo", "con el objeto", "con el fin", "poder")
    for token in oracion.as_doc():
        if (token.pos_ == "VERB" and para == 0):
            para += 1
            for parte in oracion[token.i:]:
                if parte.lemma_ not in con_que:
                    que.append(parte)
                else:
                    para += 1
                    break
        # print(token.lemma_)
        if (token.lemma_ in con_que):
            para_que.append(token)
            for parte in oracion[token.i + 1:]:
                if parte.lemma_ not in con_que:
                    para_que.append(parte)
                else:
                    # para_que.append("y")
                    break

    oracion_que = " ".join(text_limpio(que))
    oracion_para_que = " ".join(text_limpio(para_que))
    oraciones = revisar(usuario, oracion_que, oracion_para_que)
    con_el_objeto = ["con la finalidad", "para", "con el objeto", "con el objetivo", "con el fin"]
    if oraciones is None:
        oraciones = []
        partes = []
        for i in oracion:
            if i.text in con_el_objeto:
                partes = oracion.text.split(i.text)
        if len(partes) > 0:
            oraciones.append({"usuario": usuario, "que": partes[0], "para_que": partes[1]})
        else:
            oraciones.append({"usuario": usuario, "que": oracion, "para_que": "sin_proposito"})
    return oraciones


def procesar(usuario, texto):
    doc = nlp(texto)


    encontrar_sustantivos(doc)

    tokens_ids = aplicar_dependencias(doc)

    oraciones_sin_limpiar = []
    for indices in tokens_ids:
        oracion_busqueda = doc[min(indices):max(indices) + 1]
        oraciones_sin_limpiar.append(oracion_busqueda)
        print("SENTENCE: ", oracion_busqueda)

    oraciones = []
    for oracion in oraciones_sin_limpiar:
        oraciones1 = pre_procesar_oraciones(usuario, oracion)
        for i in oraciones1:
            oraciones.append(i)
            print(i)

    print("oraciones encontradas: ", len(oraciones))
    return oraciones


text = "El sistema debe permitirme consultar los reportes de base de datos con el fin de ver la situacion de la empresa registrar las ventas para generar informes actualizar los nombres de usuario con el objetivo de mantener actualizado el sistema y eliminar los datos con el objeto de ahorrar dinero"
procesar(usuario, text)