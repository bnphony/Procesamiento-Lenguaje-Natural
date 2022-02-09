

def crearDependencia(oraciones):

    datos = []
    links = []

    conexiones = [oracion for oracion in oraciones if oracion.grupo != 0]
    print([conexion.grupo for conexion in oraciones])

    for oracion in conexiones:
        preview = oracion
        for n in (conexiones[:conexiones.index(preview)] + conexiones[conexiones.index(preview) + 1:]):
            links.append([preview.id, n.id])

    review = [sorted(link) for link in links]

    for link in review:
        preview = link
        for n in review[:review.index(preview)] + review[review.index(preview) + 1:]:
            if not set(n).isdisjoint(preview):
                if preview == n:
                    if n in review:
                        review.remove(n)

    conexiones = []
    for link in review:
        conexiones.append({'source': link[0], 'target': link[1]})

    return conexiones
