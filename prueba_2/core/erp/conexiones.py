

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


    # print(links)
    # review = [sorted(link) for link in links]
    # print(review)
    nueva_review = []
    # [nueva_review.append(x) for x in links if x not in nueva_review]
    nueva_suma = []
    for x in links:
        if sum(x) not in nueva_suma:
            nueva_review.append(x)
            nueva_suma.append(sum(x))
    # [nueva_review.append(x) for x in links if x not in nueva_review]
    print(nueva_review)

    conexiones = []
    for link in nueva_review:
        conexiones.append({'source': link[1], 'target': link[0]})

    # importancia: {[key: number]: int} = {}
    # dependencia = []
    # for conexion in conexiones:
    #
    #     importancia.append(conexion['source'])
    #     print(importancia)
    #     if importancia[conexion['source']] in importancia:
    #         # importancia[conexion['source']] += 1
    #         pass
    #     else:
    #         importancia.append({conexion['source']: 1})

        # if dependencia[conexion['target']] in dependencia:
        #     dependencia[conexion['target']] += 1
        # else:
        #     dependencia[conexion['target']] = 1

        # print(conexion['source'])
    #
    # print('importancia', importancia)
    # print('dependencia', dependencia)

    return conexiones
