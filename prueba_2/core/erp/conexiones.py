

def crearDependencia(oraciones):

    datos = []
    links = []

    conexiones = [oracion for oracion in oraciones if oracion.grupo != 0]


    for oracion in conexiones:
        preview = oracion
        for n in (conexiones[:conexiones.index(preview)] + conexiones[conexiones.index(preview) + 1:]):
            links.append([preview.id, n.id])

    for link in links:
        preview = link
        for n in links[:links.index(preview)] + links[links.index(preview) + 1:]:
            if not set(n).isdisjoint(preview):
                valor = list(set(preview + n))
                if n in links:
                    links.remove(n)
                links[links.index(preview)] = valor
                preview = valor

    conexiones = []
    for link in links:
        conexiones.append({'source': link[0], 'target': link[1]})

    return conexiones
