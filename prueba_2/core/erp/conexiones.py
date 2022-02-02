

def crearDependencia(oraciones):
    print("INgeso a la funcion")
    datos = []
    links = []

    conexiones = [oracion for oracion in oraciones if oracion.grupo != 0]

    print(type(conexiones))
    for oracion in conexiones:
        preview = oracion
        print('ingeso a l for')
        print(conexiones[:conexiones.index(preview)] + conexiones[conexiones.index(preview) + 1:])
        for n in (conexiones[:conexiones.index(preview)] + conexiones[conexiones.index(preview) + 1:]):
            # valor = list(set(preview + n))
            links.append([preview.id, n.id])


    print('Paso los links')
    for link in links:
        preview = link
        for n in links[:links.index(preview)] + links[links.index(preview) + 1:]:
            if not set(n).isdisjoint(preview):
                valor = list(set(preview + n))
                if n in links:
                    links.remove(n)
                links[links.index(preview)] = valor
                preview = valor

    print(links)
    conexiones = []
    for link in links:
        conexiones.append({'source': link[0], 'target': link[1]})

    return conexiones
