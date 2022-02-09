# Formas sustantivos
con_el_objeto = ["con la finalidad", "para", "con el objeto", "con el objetivo", "con el fin"]
sustantivos_compuestos = [
    {
        "RIGHT_ID": "sustantivo",
        "RIGHT_ATTRS": {"POS": "NOUN"}
    },
    {
        "LEFT_ID": "sustantivo",
        "REL_OP": ">",
        "RIGHT_ID": "nmod_sus",
        "RIGHT_ATTRS": {"DEP": {"IN": ["nmod", "amod", "det"]}, "POS": {"IN": ["NOUN", "DET", "ADJ", "PROPN"]}, "LOWER": {"NOT_IN": con_el_objeto}}, # Se aumento amod y det y el POS NOUN
    }
]

sustantivos_compuestos_2 = [
    {
        "RIGHT_ID": "noun_uno",
        "RIGHT_ATTRS": {"POS": "NOUN"},
    },
    {
        "LEFT_ID": "noun_uno",
        "REL_OP": ">",
        "RIGHT_ID": "noun_dos",
        "RIGHT_ATTRS": {"DEP": "nmod", "POS": {"IN": ["NOUN", "DET"]}},
    },
    {
        "LEFT_ID": "noun_dos",
        "REL_OP": ">",
        "RIGHT_ID": "adjectivo_tres",
        "RIGHT_ATTRS": {"DEP": "amod", "POS": {"IN": ["NOUN", "DET"]}},
    }
]

sustantivos_compuestos_3 = [
    {
        "RIGHT_ID": "noun_adjappos",
        "RIGHT_ATTRS": {"POS": "NOUN"}
    },
    {
        "LEFT_ID": "noun_adjappos",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_adj",
        "RIGHT_ATTRS": {"DEP": "amod"},
    },
    {
        "LEFT_ID": "noun_adjappos",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_appos",
        "RIGHT_ATTRS": {"DEP": "appos"},
    },
]

propn_nummod = [
    {
        "RIGHT_ID": "propn_nummod",
        "RIGHT_ATTRS": {"POS": "PROPN"}
    },
    {
        "LEFT_ID": "propn_nummod",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_nummod",
        "RIGHT_ATTRS": {"DEP": "nummod"},
    },
]


con_la_finalidad_de = [
    {
        "RIGHT_ID": "fin",
        "RIGHT_ATTRS": {"POS": "NOUN", "LOWER": {"IN": ["finalidad", "objetivo"]}}
    },
    {
        "LEFT_ID": "fin",
        "REL_OP": ">",
        "RIGHT_ID": "con_el_fin",
        "RIGHT_ATTRS": {"DEP": "case", "LOWER": "con"},
    },
]

con_el_fin_de = [

    {
        "RIGHT_ID": "con",
        "RIGHT_ATTRS": {"POS": "ADP", "LOWER": {"IN": ["con"]}}
    },
    {
        "LEFT_ID": "con",
        "REL_OP": ".",
        "RIGHT_ID": "el",
        "RIGHT_ATTRS": {"LOWER": {"IN": ["el", "la"]}},
    },
    {
        "LEFT_ID": "el",
        "REL_OP": ".",
        "RIGHT_ID": "con_el_fin",
        "RIGHT_ATTRS": {"LOWER": {"IN": ["fin", "finalidad", "objetivo", "objeto"]}}
    }
]


# Patterns de Dependencia
pattern1 = [
    {
        "RIGHT_ID": "anchor_founded",
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "anchor_founded",
        "REL_OP": ">", # Aqui hay cambios para unas oraciones y para otras
        "RIGHT_ID": "founded_subject",
        "RIGHT_ATTRS": {"DEP": "obj"},
    },
    {
        "LEFT_ID": "anchor_founded",
        "REL_OP": ">",
        "RIGHT_ID": "founded_object",
        "RIGHT_ATTRS": {"DEP": "advcl"},
    },
    {
        "LEFT_ID": "founded_object",
        "REL_OP": ">",
        "RIGHT_ID": "object_subject",
        "RIGHT_ATTRS": {"DEP": {"IN": ["obj", "obl", "ccomp"]}}, # El ultimo agregado es ccomp OJO
    }
]

pattern2 = [
    {
        "RIGHT_ID": "verbo_objecto",
        "RIGHT_ATTRS": {"POS": "VERB", "LEMMA": {"NOT_IN": ["desear", "necesitar", "querer", "permitir"]}}
    },
    {
        "LEFT_ID": "verbo_objecto",
        "REL_OP": ">",
        "RIGHT_ID": "objecto_verbo",
        "RIGHT_ATTRS": {"DEP": "obj", "POS": {"NOT_IN": [""]}}, # Se quito el PRON en la exclusion
    }
]

pattern3 = [
    {
        "RIGHT_ID": "verbos_seguidos",
        "RIGHT_ATTRS": {"POS": "VERB", "LEMMA": {"NOT_IN": ["querer", "necesitar", "desear", "permitir"]}}
    },
    {
        "LEFT_ID": "verbos_seguidos",
        "REL_OP": "<", # Se cambio el . por <
        "RIGHT_ID": "verbo_objetivo",
        "RIGHT_ATTRS": {"DEP": "xcomp"},
    }
]

pattern5 = [
    {
        "RIGHT_ID": "verbo_uno",
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "verbo_uno",
        "REL_OP": ">",
        "RIGHT_ID": "verbo_dos",
        "RIGHT_ATTRS": {"DEP": "nsubj", "POS": "NOUN"},
    },
]

pattern6 = [
    {
        "RIGHT_ID": "oracion_compuesta",
        "RIGHT_ATTRS": {"POS": "VERB", "LEMMA": {"NOT_IN": ["desear", "permitir", "necesitar", "querer"]}}
    },
    {
        "LEFT_ID": "oracion_compuesta",
        "REL_OP": ">",
        "RIGHT_ID": "objecto_obl",
        "RIGHT_ATTRS": {"DEP": "obl"},
    },
    {
        "LEFT_ID": "oracion_compuesta",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_advcl",
        "RIGHT_ATTRS": {"DEP": "advcl"},
    },
    {
        "LEFT_ID": "objeto_advcl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obj",
        "RIGHT_ATTRS": {"DEP": "obj"},
    }
]

pattern7 = [
    {
        "RIGHT_ID": "verbo_obl",
        "RIGHT_ATTRS": {"POS": "VERB", "LEMMA": {"NOT_IN": ["desear", "necesitar", "querer", "permitir"]}}
    },
    {
        "LEFT_ID": "verbo_obl",
        "REL_OP": ">", # Se cambio el >> por >
        "RIGHT_ID": "objeto_obl",
        "RIGHT_ATTRS": {"DEP": "obl"},
    }
]

# Caso especial cuando comienza por ir
pattern8 = [
    {
        "RIGHT_ID": "caso_ir",
        "RIGHT_ATTRS": {"POS": "VERB", "LOWER": "ir"}
    },
    {
        "LEFT_ID": "caso_ir",
        "REL_OP": "<",
        "RIGHT_ID": "objeto_obl",
        "RIGHT_ATTRS": {"DEP": "obl"},
    },
    {
        "LEFT_ID": "caso_ir",
        "REL_OP": ">",
        "RIGHT_ID": "objecto_obl",
        "RIGHT_ATTRS": {"DEP": "obl", "POS": "NOUN"},
    },
    {
        "LEFT_ID": "objecto_obl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_acl",
        "RIGHT_ATTRS": {"DEP": "acl"},
    },
    {
        "LEFT_ID": "objeto_acl",
        "REL_OP": ">",
        "RIGHT_ID": "objecto_advcl",
        "RIGHT_ATTRS": {"DEP": "obj"},
    }
]

# Caso similar al ir
pattern9 = [
    {
        "RIGHT_ID": "compuesto_verbo",
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "compuesto_verbo",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obl",
        "RIGHT_ATTRS": {"DEP": "obl"},
    },
    {
        "LEFT_ID": "objeto_obl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_acl",
        "RIGHT_ATTRS": {"DEP": "acl", "POS": "VERB"},
    },
    {
        "LEFT_ID": "objeto_acl",
        "REL_OP": ">",
        "RIGHT_ID": "objecto_ob",
        "RIGHT_ATTRS": {"DEP": "obj", "POS": "NOUN"},
    }
]

pattern10 = [
    {
        "RIGHT_ID": "verb_obj_acl",
        "RIGHT_ATTRS": {"POS": "VERB", "LEMMA": {"NOT_IN": ["desear", "querer", "necesitar", "permitir"]}}
    },
    {
        "LEFT_ID": "verb_obj_acl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obj",
        "RIGHT_ATTRS": {"DEP": "obj"},
    },
    {
        "LEFT_ID": "verb_obj_acl",
        "REL_OP": ">", # Se cambio el >> por .
        "RIGHT_ID": "objeto_xcomp",
        "RIGHT_ATTRS": {"DEP": {"IN": ["acl"]}, "POS": {"IN": ["NOUN", "VERB"]}},
    }
]

pattern11 = [
    {
        "RIGHT_ID": "verbo_obl_advcl",
        "RIGHT_ATTRS": {"POS": "VERB", "LEMMA": {"NOT_IN": ["desear", "necesitar", "querer", "permitir"]}},
    },
    {
        "LEFT_ID": "verbo_obl_advcl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obl",
        "RIGHT_ATTRS": {"DEP": "obl"},
    },
    {
        "LEFT_ID": "verbo_obl_advcl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_advcl",
        "RIGHT_ATTRS": {"DEP": "advcl"}, # Se aumento acl
    }
]

pattern12 = [
    {
        "RIGHT_ID": "verbo_obj_seguido_acl",
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "verbo_obj_seguido_acl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obj",
        "RIGHT_ATTRS": {"DEP": "obj"},
    },
    {
        "LEFT_ID": "objeto_obj",
        "REL_OP": "<", # Se cambio > por < OJO
        "RIGHT_ID": "objeto_acl",
        "RIGHT_ATTRS": {"DEP": "acl"},
    }
]

pattern13 = [
    {
        "RIGHT_ID": "verbo_obj_acl_obj",
        "RIGHT_ATTRS": {"POS": "VERB", "LEMMA": {"NOT_IN": ["querer", "nesecitar", "desear", "permitir"]}},
    },
    {
        "LEFT_ID": "verbo_obj_acl_obj",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obj",
        "RIGHT_ATTRS": {"DEP": "obj"},
    },
    {
        "LEFT_ID": "objeto_obj",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_acl",
        "RIGHT_ATTRS": {"DEP": "acl"},
    },
    {
        "LEFT_ID": "objeto_acl",
        "REL_OP": ">",
        "RIGHT_ID": "seg_obj",
        "RIGHT_ATTRS": {"DEP": "obj"},
    }
]

pattern14 = [
    {
        "RIGHT_ID": "verbo_obj_obl_acl_obl",
        "RIGHT_ATTRS": {"POS": "VERB", "LEMMA": {"NOT_IN": ["nesecitar", "querer", "desear", "permitir"]}}
    },
    {
        "LEFT_ID": "verbo_obj_obl_acl_obl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obj",
        "RIGHT_ATTRS": {"DEP": "obj"},
    },
    {
        "LEFT_ID": "verbo_obj_obl_acl_obl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obl",
        "RIGHT_ATTRS": {"DEP": "obl"},
    },
    {
        "LEFT_ID": "objeto_obl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_acl",
        "RIGHT_ATTRS": {"DEP": "acl"},
    },
    {
        "LEFT_ID": "objeto_acl",
        "REL_OP": ">",
        "RIGHT_ID": "o_obl",
        "RIGHT_ATTRS": {"DEP": {"IN": ["obl", "obj"]}},
    }
]

pattern15 = [
    {
        "RIGHT_ID": "obj_advcl_ccomp_obj",
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "obj_advcl_ccomp_obj",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obj",
        "RIGHT_ATTRS": {"DEP": "obj"}
    },
    {
        "LEFT_ID": "obj_advcl_ccomp_obj",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_advcl",
        "RIGHT_ATTRS": {"DEP": "advcl"},
    },
    {
        "LEFT_ID": "objeto_advcl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_ccomp",
        "RIGHT_ATTRS": {"DEP": "ccomp"},
    },
    {
        "LEFT_ID": "objeto_ccomp",
        "REL_OP": ">",
        "RIGHT_ID": "obj_obj",
        "RIGHT_ATTRS": {"DEP": "obj"},
    }
]

pattern16 = [
    {
        "RIGHT_ID": "verbo_noun",
        "RIGHT_ATTRS": {"POS": "VERB", "LEMMA": {"NOT_IN": ["necesitar", "desear", "querer", "permitir"]}}
    },
    {
        "LEFT_ID": "verbo_noun",
        "REL_OP": ".", # Se cambio el >> por .
        "RIGHT_ID": "objeto_noun",
        "RIGHT_ATTRS": {"DEP": "nsubj"},
    },
]

# Se parece al pattern1 solo cambia al final con la dependencia CCOMP
pattern17 = [
    {
        "RIGHT_ID": "verbo_obj_obl_acl",
        "RIGHT_ATTRS": {"POS": "VERB", "LEMMA": {"NOT_IN": ["querer", "permitir", "necesitar", "desear"]}}
    },
    {
        "LEFT_ID": "verbo_obj_obl_acl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obj",
        "RIGHT_ATTRS": {"DEP": "obj"},
    },
    {
        "LEFT_ID": "verbo_obj_obl_acl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obl",
        "RIGHT_ATTRS": {"DEP": "obl"},
    },
    {
        "LEFT_ID": "objeto_obl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_acl",
        "RIGHT_ATTRS": {"DEP": "acl"},
    },
]

pattern18 = [
    {
        "RIGHT_ID": "verbo_obl_acl",
        "RIGHT_ATTRS": {"POS": "VERB", "LOWER": {"NOT_IN": ["querer", "desear", "necesitar", "permitir"]}}
    },
    {
        "LEFT_ID": "verbo_obl_acl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obl",
        "RIGHT_ATTRS": {"DEP": {"IN": ["obl", "obj"]}},
    },
    {
        "LEFT_ID": "objeto_obl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_acl",
        "RIGHT_ATTRS": {"DEP": "acl"},
    },
]

pattern19 = [
    {
        "RIGHT_ID": "verbo_xcomp_obj_acl",
        "RIGHT_ATTRS": {"POS": "VERB", "LEMMA": {"NOT_IN": ["querer", "necesitar", "desear", "permitir"]}}
    },
    {
        "LEFT_ID": "verbo_xcomp_obj_acl",
        "REL_OP": ".",  # Se cambio el > por .
        "RIGHT_ID": "objeto_xcomp",
        "RIGHT_ATTRS": {"DEP": "xcomp"},
    },
    {
        "LEFT_ID": "objeto_xcomp",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obj",
        "RIGHT_ATTRS": {"DEP": "obj"},
    },
    {
        "LEFT_ID": "objeto_obj",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_acl",
        "RIGHT_ATTRS": {"DEP": "acl"},
    },
]

# Similar al pattern 15
pattern20 = [
    {
        "RIGHT_ID": "verbo_obj_advcl",
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "verbo_obj_advcl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obj",
        "RIGHT_ATTRS": {"DEP": "obj"}
    },
    {
        "LEFT_ID": "verbo_obj_advcl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_advcl",
        "RIGHT_ATTRS": {"DEP": "advcl"},
    }
]

# Similar al pattern 19
pattern21 = [
    {
        "RIGHT_ID": "verbo_xcomp_advcl",
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "verbo_xcomp_advcl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_xcomp",
        "RIGHT_ATTRS": {"DEP": "xcomp"},
    },
    {
        "LEFT_ID": "objeto_xcomp",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_advcl",
        "RIGHT_ATTRS": {"DEP": {"IN": ["advcl"]}},
    }
]

# Caso especial con el para
pattern22 = [
    {
        "RIGHT_ID": "verbo_xcomp_adp_verbo",
        "RIGHT_ATTRS": {"POS": "VERB", "LEMMA": {"NOT_IN": ["desear", "querer", "necesitar", "permitir"]}}
    },
    {
        "LEFT_ID": "verbo_xcomp_adp_verbo",
        "REL_OP": ".",
        "RIGHT_ID": "objeto_xcomp",
        "RIGHT_ATTRS": {"DEP": "xcomp"},
    },
    {
        "LEFT_ID": "objeto_xcomp",
        "REL_OP": ".",
        "RIGHT_ID": "objeto_adp",
        "RIGHT_ATTRS": {"POS": "ADP"},
    },
    {
        "LEFT_ID": "objeto_adp",
        "REL_OP": ".",
        "RIGHT_ID": "objeto_verbo",
        "RIGHT_ATTRS": {"POS": {"IN": ["NOUN", "VERB"]}},
    },
]

# Caso especial para el
pattern23 = [
    {
        "RIGHT_ID": "verbo_xcomp_adp_verbo",
        "RIGHT_ATTRS": {"POS": "VERB", "LEMMA": {"NOT_IN": ["desear", "querer", "necesitar", "permitir"]}}
    },
    {
        "LEFT_ID": "verbo_xcomp_adp_verbo",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_xcomp",
        "RIGHT_ATTRS": {"DEP": "xcomp"},
    },
    {
        "LEFT_ID": "objeto_xcomp",
        "REL_OP": ".",
        "RIGHT_ID": "objeto_adp",
        "RIGHT_ATTRS": {"POS": "ADP"},
    },
    {
        "LEFT_ID": "objeto_adp",
        "REL_OP": ".",
        "RIGHT_ID": "objeto_verbo",
        "RIGHT_ATTRS": {"POS": {"IN": ["NOUN", "VERB"]}},
    },
]

# Caso especial para el con el objetivo de
pattern24 = [
    {
        "RIGHT_ID": "verbo_obj_adp_case",
        "RIGHT_ATTRS": {"POS": "VERB", "LEMMA": {"NOT_IN": ["desear", "querer", "necesitar", "permitir"]}}
    },
    {
        "LEFT_ID": "verbo_obj_adp_case",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obj",
        "RIGHT_ATTRS": {"DEP": {"IN": ["obj", "obl"]}}, # Se aumento OBL
    },
    {
        "LEFT_ID": "objeto_obj",
        "REL_OP": ".",
        "RIGHT_ID": "objeto_adp",
        "RIGHT_ATTRS": {"POS": "ADP"},
    },
    {
        "LEFT_ID": "objeto_adp",
        "REL_OP": "<",
        "RIGHT_ID": "objeto_case",
        "RIGHT_ATTRS": {"POS": {"IN": ["NOUN", "VERB", "ADJ"]}}, # Si no estas seguro de la relacion no poner
    },
]

pattern25 = [
    {
        "RIGHT_ID": "verbo_obj_acl_advcl_obj",
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "verbo_obj_acl_advcl_obj",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obj",
        "RIGHT_ATTRS": {"DEP": "obj"},
    },
    {
        "LEFT_ID": "objeto_obj",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_acl",
        "RIGHT_ATTRS": {"DEP": "acl"},
    },
    {
        "LEFT_ID": "objeto_acl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_advcl",
        "RIGHT_ATTRS": {"DEP": "advcl"},
    },
    {
        "LEFT_ID": "objeto_advcl",
        "REL_OP": ">",
        "RIGHT_ID": "obj_obj",
        "RIGHT_ATTRS": {"DEP": "obj"},
    },
]

pattern26 = [
    {
        "RIGHT_ID": "verbo_nsubj_acl_obj_obj",
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "verbo_nsubj_acl_obj_obj",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_nsubj",
        "RIGHT_ATTRS": {"DEP": "nsubj"},
    },
    {
        "LEFT_ID": "objeto_nsubj",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_acl",
        "RIGHT_ATTRS": {"DEP": "acl"},
    },
    {
        "LEFT_ID": "objeto_acl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obj",
        "RIGHT_ATTRS": {"DEP": "obj"},
    },
    {
        "LEFT_ID": "objeto_acl",
        "REL_OP": ">",
        "RIGHT_ID": "obj_obj",
        "RIGHT_ATTRS": {"DEP": "obj"},
    }
]

pattern27 = [
    {
        "RIGHT_ID": "verbo_obj_nmod_acl_ccomp",
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "verbo_obj_nmod_acl_ccomp",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obj",
        "RIGHT_ATTRS": {"DEP": "obj"},
    },
    {
        "LEFT_ID": "objeto_obj",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_nmod",
        "RIGHT_ATTRS": {"DEP": "nmod"},
    },
    {
        "LEFT_ID": "objeto_nmod",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_acl",
        "RIGHT_ATTRS": {"DEP": "acl"},
    },
    {
        "LEFT_ID": "objeto_acl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_ccomp",
        "RIGHT_ATTRS": {"DEP": "ccomp"},
    },
]

pattern28 = [
    {
        "RIGHT_ID": "verbo_obj_acl_acl",
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "verbo_obj_acl_acl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obj",
        "RIGHT_ATTRS": {"DEP": "obj"},
    },
    {
        "LEFT_ID": "objeto_obj",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_acl",
        "RIGHT_ATTRS": {"DEP": {"IN": ["advcl", "acl"]}},
    },
    {
        "LEFT_ID": "objeto_acl",
        "REL_OP": ">",
        "RIGHT_ID": "obj_acl",
        "RIGHT_ATTRS": {"DEP": {"IN": ["advcl", "acl"]}},
    },
]

pattern29 = [
    {
        "RIGHT_ID": "verbo_ccomp_conj",
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "verbo_ccomp_conj",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_ccomp",
        "RIGHT_ATTRS": {"DEP": "ccomp"},
    },
    {
        "LEFT_ID": "objeto_ccomp",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_conj",
        "RIGHT_ATTRS": {"DEP": {"IN": ["conj", "acl"]}},
    },
]

pattern30 = [
    {
        "RIGHT_ID": "verbo_advcl_obj",
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "verbo_advcl_obj",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_advcl",
        "RIGHT_ATTRS": {"DEP": "advcl"},
    },
    {
        "LEFT_ID": "objeto_advcl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obj",
        "RIGHT_ATTRS": {"DEP": "obj"},
    },
]
pattern31 = [
    {
        "RIGHT_ID": "verbo_sconj_verbo_obj",
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "verbo_sconj_verbo_obj",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_verbo",
        "RIGHT_ATTRS": {"DEP": "conj"}
    },
    {
        "LEFT_ID": "objeto_verbo",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obj",
        "RIGHT_ATTRS": {"DEP": "obj"},
    },
]

# Cuando hay varias opciones de sujetos
pattern32 = [
    {
        "RIGHT_ID": "noun_cconj_noun",
        "RIGHT_ATTRS": {"POS": {"IN": ["NOUN", "VERB"]}}
    },
    {
        "LEFT_ID": "noun_cconj_noun",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_noun",
        "RIGHT_ATTRS": {"DEP": "conj"},
    },
]

# Cuando se refiere a un sujeto
pattern33 = [
    {
        "RIGHT_ID": "noun_adj_acl",
        "RIGHT_ATTRS": {"POS": "NOUN"}
    },
    {
        "LEFT_ID": "noun_adj_acl",
        "REL_OP": ">",
        "RIGHT_ID": "obj_adj",
        "RIGHT_ATTRS": {"DEP": "amod"}
    },
    {
        "LEFT_ID": "obj_adj",
        "REL_OP": ".",
        "RIGHT_ID": "objeto_adp",
        "RIGHT_ATTRS": {"POS": "ADP", "LOWER": "para"},
    },
    {
        "LEFT_ID": "objeto_adp",
        "REL_OP": "<",
        "RIGHT_ID": "objeto_mark",
        "RIGHT_ATTRS": {}
    }
]

pattern34 = [
    {
        "RIGHT_ID": "noun_nmod_acl",
        "RIGHT_ATTRS": {"POS": "NOUN"}
    },
    {
        "LEFT_ID": "noun_nmod_acl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_nmod",
        "RIGHT_ATTRS": {"DEP": "nmod"},
    },
    {
        "LEFT_ID": "objeto_nmod",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_acl",
        "RIGHT_ATTRS": {"DEP": "acl", "POS": {"NOT_IN": ["VERB"]}},
    },
]
# Similar al pattern 34 la diferencia es el amod
pattern35 = [
    {
        "RIGHT_ID": "noun_amod_nmod_acl",
        "RIGHT_ATTRS": {"POS": "NOUN"}
    },
    {
        "LEFT_ID": "noun_amod_nmod_acl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_amod",
        "RIGHT_ATTRS": {"DEP": "amod"},
    },
    {
        "LEFT_ID": "objeto_amod",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_nmod",
        "RIGHT_ATTRS": {"DEP": "nmod"},
    },
    {
        "LEFT_ID": "objeto_nmod",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_acl",
        "RIGHT_ATTRS": {"DEP": "acl"},
    },
]

pattern36 = [
    {
        "RIGHT_ID": "noun_nmod_nummod",
        "RIGHT_ATTRS": {"POS": "NOUN"}
    },
    {
        "LEFT_ID": "noun_nmod_nummod",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_nmod",
        "RIGHT_ATTRS": {"DEP": "nmod"},
    },
    {
        "LEFT_ID": "objeto_nmod",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_nummod",
        "RIGHT_ATTRS": {"DEP": "nummod"},
    },
]

# Similar al pattern 36
pattern37 = [
    {
        "RIGHT_ID": "noun_nummod",
        "RIGHT_ATTRS": {"POS": "NOUN"}
    },
    {
        "LEFT_ID": "noun_nummod",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_nummod",
        "RIGHT_ATTRS": {"DEP": {"IN": ["nummod", "compound"]}},
    },
]


pattern38 = [
    {
        "RIGHT_ID": "noun_conj",
        "RIGHT_ATTRS": {"POS": "NOUN"}
    },
    {
        "LEFT_ID": "noun_conj",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_conj",
        "RIGHT_ATTRS": {"DEP": "conj"}
    }
]


# Cuando hay advervios modificadores al final
pattern39 = [
    {
        "RIGHT_ID": "verbo_obj_obl_advmod",
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "verbo_obj_obl_advmod",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obj",
        "RIGHT_ATTRS": {"DEP": "obj"},
    },
    {
        "LEFT_ID": "verbo_obj_obl_advmod",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obl",
        "RIGHT_ATTRS": {"DEP": "obl"},
    },
    {
        "LEFT_ID": "verbo_obj_obl_advmod",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_advmod",
        "RIGHT_ATTRS": {"DEP": "advmod"},
    },
]

# Similar al pattern 29
pattern40 = [
    {
        "RIGHT_ID": "verbo_ccomp_nsubj_acl",
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "verbo_ccomp_nsubj_acl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_ccomp",
        "RIGHT_ATTRS": {"DEP": "ccomp"},
    },
    {
        "LEFT_ID": "objeto_ccomp",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_nsubj",
        "RIGHT_ATTRS": {"DEP": "nsubj"},
    },
    {
        "LEFT_ID": "objeto_nsubj",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_acl",
        "RIGHT_ATTRS": {"DEP": "acl"},
    },
]

pattern41 = [
    {
        "RIGHT_ID": "verbo_ccomp",
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "verbo_ccomp",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_ccomp",
        "RIGHT_ATTRS": {"DEP": "ccomp"}
    }
]

# descubrir material luego del para que
pattern42 = [
    {
        "RIGHT_ID": "noun_appos_conj_obj",
        "RIGHT_ATTRS": {"POS": "NOUN", "LOWER": {"IN": con_el_objeto}}
    },
    {
        "LEFT_ID": "noun_appos_conj_obj",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_appos",
        "RIGHT_ATTRS": {"DEP": "appos"},
    },
    {
        "LEFT_ID": "objeto_appos",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_conj",
        "RIGHT_ATTRS": {"DEP": "conj"},
    },
    {
        "LEFT_ID": "objeto_conj",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obj",
        "RIGHT_ATTRS": {"DEP": "obj"},
    },
]

# NO FUNCIONALES
pattern43 = [
    {
        "RIGHT_ID": "adj_nsubj_nmod_acl",
        "RIGHT_ATTRS": {"POS": "ADJ"}
    },
    {
        "LEFT_ID": "adj_nsubj_nmod_acl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_nsubj",
        "RIGHT_ATTRS": {"DEP": "nsubj"},
    },
    {
        "LEFT_ID": "objeto_nsubj",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_nmod",
        "RIGHT_ATTRS": {"DEP": "nmod"},
    },
    {
        "LEFT_ID": "objeto_nmod",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_acl",
        "RIGHT_ATTRS": {"DEP": "acl"},
    },
]

pattern44 = [
    {
        "RIGHT_ID": "verbo_obj_nmod_acl",
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "verbo_obj_nmod_acl",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_obj",
        "RIGHT_ATTRS": {"DEP": "obj"},
    },
    {
        "LEFT_ID": "objeto_obj",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_nmod",
        "RIGHT_ATTRS": {"DEP": "nmod"},
    },
    {
        "LEFT_ID": "objeto_nmod",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_acl",
        "RIGHT_ATTRS": {"DEP": "acl"},
    },
]

pattern45 = [
    {
        "RIGHT_ID": "verbo_nsubj_appos_compound",
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "verbo_nsubj_appos_compound",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_nsubj",
        "RIGHT_ATTRS": {"DEP": "nsubj"},
    },
    {
        "LEFT_ID": "objeto_nsubj",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_appos",
        "RIGHT_ATTRS": {"DEP": "appos"},
    },
    {
        "LEFT_ID": "objeto_appos",
        "REL_OP": ">",
        "RIGHT_ID": "objeto_compound",
        "RIGHT_ATTRS": {"DEP": "compound"},
    },
]

pattern46 = [
    {
        "RIGHT_ID": "complemento_verbo_advmod_fixed",
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "complemento_verbo_advmod_fixed",
        "REL_OP": ".",
        "RIGHT_ID": "objeto_advmod",
        "RIGHT_ATTRS": {"DEP": "advmod"}
    },
    {
        "LEFT_ID": "objeto_advmod",
        "REL_OP": ".",
        "RIGHT_ID": "objeto_fixed",
        "RIGHT_ATTRS": {"DEP": "fixed"}
    }
]

# Reglas de Estructura
verbo_sus_adp_verb_noun = [
    {"POS": "VERB"},
    {"POS": {"IN": ["ADP", "DET"]}, "OP": "*"},
    {"POS": "ADJ", "OP": "?"},
    {"POS": {"IN": ["NOUN", "VERB"]}},
    {"POS": "ADJ", "OP": "?"},
    {"POS": "NOUN", "LOWER": {"NOT_IN": ["con el fin de", "con la finalidad", "con el objetivo", "con el objeto"]}, "OP": "?"}, # Se agrego el LOWER
    {"POS": {"IN": ["ADP", "DET"]}, "LOWER": {"IN": ["con"]},"OP": "?"}, # Se agrego ultimo
    {"POS": {"IN": ["NOUN", "ADP"]}, "OP": "?"}, # Se agrego ultimo
    {"POS": {"IN": ["ADP", "DET", "AUX"]}, "LOWER": {"IN": ["de", "para", "puede", "poder"]}, "OP": "+"},
    {"POS": {"IN": ["VERB", "NOUN", "AUX"]}},
    {"POS": {"IN": ["ADP", "DET", "ADJ"]}, "OP": "?"},
    {"POS": "SCONJ", "OP": "?"}, # Opcional
    {"POS": {"IN": ["NOUN", "VERB"]}, "OP": "?"},
    {"POS": {"IN": ["NOUN", "ADJ", "AUX"]}, "OP": "?"}, # Opcional  # Se quito el VERB
    {"POS": {"IN": ["NOUN"]}, "OP": "?"}, # Opcional
    {"POS": {"NOT_IN": ["CCONJ", "VERB"]}}
]
verbo_para_que = [
    {"POS": "VERB"},
    {"POS": {"NOT_IN": ["VERB"]}, "LOWER": {"NOT_IN": ["para", "de"]}, "OP": "*"},
    {"LOWER": {"IN": con_el_objeto}},
    {"POS": {"IN": ["ADP"]}, "LOWER": {"IN": ["para", "de"]}},
    {"POS": {"IN": ["NOUN", "VERB"]}}
]

verbo_obj = [
    {"POS": "VERB"},
    {"POS": {"IN": ["ADP", "DET", "SCONJ", "PROPN"]}, "OP": "*"},
    {"POS": "ADJ", "OP": "?"} ,
    {"POS": {"IN": ["NOUN", "ADJ"]}}, # Se agrego el ADJ y el VERB
    {"POS": "ADJ", "OP": "?"},
    {"POS": "NOUN", "OP": "?"},
    {"LOWER": {"NOT_IN": ["para", "de"]}, "POS": {"NOT_IN": ["VERB", "PROPN", "ADV", "CCONJ", "SCONJ"]}, "OP": "*"}, # Este se agrego ultimo, puede generar problemas OJO
    {"POS": {"IN": ["PROPN", "ADJ", "CCONJ", "ADP", "NOUN"]}, "OP": "*"}, # Este se agrego
    {"POS": "AUX", "OP": "?"},
    {"POS": {"IN": ["PROPN", "ADJ", "NOUN", "ADP"]},  "OP": "*"} # Este se agrego al ultimo
]

verbo_n = [
    {"POS": "VERB"},
    {"POS": {"IN": ["PRON", "AUX"]}, "OP": "*"},
    {"POS": "NOUN"}
]

adp_adv_noun = [
    {"POS": "ADP"},
    {"POS": {"IN": ["ADV", "ADP"]}, "OP": "*"},
    {"POS": "NOUN"}
]

adj_det_noun_verbo = [
    {"POS": "ADJ"},
    {"POS": {"IN": ["DET", "SYM", "ADP"]}, "OP": "+"},
    {"POS": {"IN": ["NOUN", "PRON"]}, "OP": "+"},
    {"POS": "VERB"}
]

verbo_obj_causa = [
    {"POS": "VERB"},
    {"POS": {"IN": ["ADP", "DET", "SCONJ", "PROPN"]}, "OP": "*"},
    {"POS": "ADJ", "OP": "?"},
    {"POS": {"IN": ["NOUN", "ADJ"]}},
    {"POS": "ADJ", "OP": "?"},
    {"POS": {"IN": ["ADP", "DET"]}, "OP": "*"},
    {"POS": {"IN": ["NOUN", "ADJ"]}},
    {"POS": {"IN": ["SCONJ"]}, "LOWER": "cuando"},
    {"POS": {"IN": ["AUX", "DET"]}, "OP": "*"},
    {"POS": "VERB"},
]

oracion_simple_2 = [
    {"POS": "VERB"},
    {"POS": {"IN": ["ADP", "DET", "PRON", "AUX"]}, "OP": "*"},
    {"POS": "ADJ", "OP": "?"},
    {"POS": {"IN": ["NOUN", "ADJ"]}},
    {"POS": "ADJ", "OP": "?"},
    {"POS": "NOUN", "OP": "?"},
    {"LOWER": {"NOT_IN": ["para", "de", "que"]}, "POS": {"NOT_IN": ["VERB", "PROPN", "ADV"]}, "OP": "*"},
    {"POS": {"IN": ["PRON", "SCONJ"]}, "LOWER": "que"},
    {"POS": {"NOT_IN": ["VERB"]}, "OP": "*"},
    {"POS": {"IN": ["NOUN", "VERB"]}, "DEP": {"NOT_IN": ["flat"]}, "OP": "?"},
    {"POS": {"NOT_IN": ["CCONJ"]}, "OP": "*"}
]

verbo_a_verbo = [
    {"POS": "VERB"},
    {"POS": {"IN": ["ADP", "SCONJ"]}, "OP": "?"},
    {"POS": "VERB", "DEP": "xcomp"},
]


verbo_o_verbo = [
    {"POS": "VERB"},
    {"POS": "CCONJ", "LOWER": "o"},
    {"POS": "VERB"},
]

verbo_adp_verbo = [
    {"POS": "VERB"},
    {"POS": {"IN": ["NOUN", "ADJ", "PROPN"]}, "OP": "?"},
    {"POS": {"IN": ["ADP", "NOUN"]}, "LOWER": {"IN": con_el_objeto}},
    {"POS": {"IN": ["DET", "ADP"]}, "LOWER": "de", "OP": "?"},
    {"POS": {"IN": ["NOUN", "VERB", "AUX"]}},
    {"POS": "ADJ", "OP": "?"},
]

aux_adj = [
    {"POS": "AUX"},
    {"POS": {"IN": ["ADJ", "VERB", "NOUN"]}},
    {"POS": "PRON", "OP": "?"},
    {"POS": "DET", "OP": "?"},
]

verbo_con_que = [
    {"POS": "VERB"},
    {"POS": "ADP"},
    {"POS": "SCONJ"},
    {"POS": "NOUN"},
    {"POS": "VERB"},
    {"POS": "NOUN"},
]

verbo = [
    {"POS": "VERB"},
]