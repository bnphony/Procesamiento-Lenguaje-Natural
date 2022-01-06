# Formas sustantivos
sustantivos_compuestos = [
    {
        "RIGHT_ID": "sustantivo",
        "RIGHT_ATTRS": {"POS": "NOUN"}
    },
    {
        "LEFT_ID": "sustantivo",
        "REL_OP": ">",
        "RIGHT_ID": "nmod_sus",
        "RIGHT_ATTRS": {"DEP": {"IN": ["nmod", "amod", "det"]}}, # Se aumento amod y det
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
        "RIGHT_ATTRS": {"DEP": "nmod"},
    },
    {
        "LEFT_ID": "noun_dos",
        "REL_OP": ">",
        "RIGHT_ID": "adjectivo_tres",
        "RIGHT_ATTRS": {"DEP": "amod"},
    }
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
    }
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
        "RIGHT_ATTRS": {"LOWER": {"IN": ["el", "la"]}}
    },
    {
        "LEFT_ID": "el",
        "REL_OP": ".",
        "RIGHT_ID": "con_el_fin",
        "RIGHT_ATTRS": {"LOWER": {"IN": ["fin", "objetivo", "objeto"]}},
    },
    {
        "LEFT_ID": "con_el_fin",
        "REL_OP": ".",
        "RIGHT_ID": "con_el_fin_de",
        "RIGHT_ATTRS": {"POS": "ADP", "LOWER": "de"},
    },

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
        "RIGHT_ATTRS": {"DEP": "obj", "POS": {"NOT_IN": ["PRON"]}},
    }
]

pattern3 = [
    {
        "RIGHT_ID": "verbos_seguidos",
        "RIGHT_ATTRS": {"POS": "VERB", "LEMMA": {"NOT_IN": ["querer", "necesitar", "desear", "permitir"]}}
    },
    {
        "LEFT_ID": "verbos_seguidos",
        "REL_OP": ">",
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
    }
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
        "REL_OP": ">>",
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
        "REL_OP": ">",
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
        "REL_OP": ">",
        "RIGHT_ID": "objeto_xcomp",
        "RIGHT_ATTRS": {"DEP": {"IN": ["advcl", "acl", "xcomp"]}, "POS": {"IN": ["NOUN", "VERB"]}},
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
        "RIGHT_ATTRS": {"POS": "VERB"}
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
        "RIGHT_ATTRS": {"POS": "VERB"}
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
        "RIGHT_ATTRS": {"DEP": "obl"},
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
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "verbo_noun",
        "REL_OP": ">>",
        "RIGHT_ID": "objeto_noun",
        "RIGHT_ATTRS": {"DEP": "nsubj"},
    }
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
    }
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
        "RIGHT_ATTRS": {"DEP": "obl"},
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
        "RIGHT_ATTRS": {"POS": "VERB"}
    },
    {
        "LEFT_ID": "verbo_xcomp_obj_acl",
        "REL_OP": ">",
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
    }
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
        "RIGHT_ATTRS": {"DEP": "advcl"},
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
    }
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
        "RIGHT_ATTRS": {"DEP": "obj"},
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
    }
]

# Reglas de Estructura
verbo_sus_adp_verb_noun = [
    {"POS": "VERB"},
    {"POS": {"IN": ["ADP", "DET"]}, "OP": "*"},
    {"POS": "ADJ", "OP": "?"},
    {"POS": {"IN": ["NOUN", "VERB"]}},
    {"POS": "ADJ", "OP": "?"},
    {"POS": "NOUN", "LOWER": {"NOT_IN": ["con el fin", "con la finalidad", "con el objetivo", "con el objeto"]}, "OP": "?"}, # Se agrego el LOWER
    {"POS": {"IN": ["ADP", "DET"]}, "LOWER": {"IN": ["con"]},"OP": "?"}, # Se agrego ultimo
    {"POS": {"IN": ["NOUN"]}, "OP": "?"}, # Se agrego ultimo
    {"POS": {"IN": ["ADP", "DET"]}, "LOWER": {"NOT_IN": ["los", "la", "el", "ellos"]}, "OP": "+"},
    {"POS": {"IN": ["VERB", "NOUN", "AUX"]}},
    {"POS": {"IN": ["ADP", "DET"]}, "OP": "?"},
    {"POS": "SCONJ", "OP": "?"}, # Opcional
    {"POS": {"IN": ["NOUN", "VERB", "ADJ"]}, "OP": "?"},
    {"POS": {"IN": ["NOUN"]}, "OP": "?"}, # Opcional  # Se quito el VERB
    {"POS": {"IN": ["NOUN"]}, "OP": "?"} # Opcional
]

verbo_obj = [
    {"POS": "VERB"},
    {"POS": {"IN": ["ADP", "DET"]}, "OP": "*"},
    {"POS": "ADJ", "OP": "?"} ,
    {"POS": {"IN": ["NOUN", "VERB", "ADJ"]}}, # Se agrego el ADJ
    {"POS": "ADJ", "OP": "?"},
    {"POS": "NOUN", "OP": "?"},
    {"LOWER": {"NOT_IN": ["para", "de"]}, "POS": {"NOT_IN": ["VERB", "PROPN", "ADV"]}, "OP": "*"} # Este se agrego ultimo, puede generar problemas OJO
]
