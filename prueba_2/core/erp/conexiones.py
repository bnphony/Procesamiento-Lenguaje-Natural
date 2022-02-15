

def crearDependencia(oraciones):

    datos = []
    links = []

    conexiones = [oracion for oracion in oraciones if oracion.grupo != 0]
    print([conexion.grupo for conexion in oraciones])

    for oracion in conexiones:
        preview = oracion
        for n in (conexiones[:conexiones.index(preview)] + conexiones[conexiones.index(preview) + 1:]):
            if preview.grupo == n.grupo:
                links.append([preview.id, n.id])


    review = [sorted(link) for link in links]
    nueva_review = []
    [nueva_review.append(x) for x in review if x not in nueva_review]


    conexiones = []
    for link in nueva_review:
        conexiones.append({'source': link[0], 'target': link[1]})

    return conexiones
