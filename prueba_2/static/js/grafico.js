var svg = d3.select('svg');

var width = svg.attr('width');
var height = svg.attr('height');


var altura_max = 500;
var altura_min = 100;

var color = d3.scaleOrdinal(d3.schemeCategory10);

var rw = 195;
var rh = 195;

const x = d3.scaleBand()
    .rangeRound([0, width])
    .padding(0.1);

const y = d3.scaleLinear()
    .range([height, 0]);


var padding = 20;
var columnas = 4;





function imprimir(datos) {
    x.domain(datos[0].map((d) => d.id));
    y.domain([0, d3.max(datos[0], d => d.usuario) + 7]);

    var data = []
    var filas = (datos[0].length % columnas == 0) ? Math.floor(datos[0].length / columnas) : Math.floor(datos[0].length/columnas) + 1;


    var c = (datos[0].length % columnas == 0 ) ? columnas : datos[0].length % columnas;
    for (var i = 0; i < filas; i += 1) {
        if (i < filas - 1) {
            data.push(d3.range(columnas))
        } else {
            data.push(d3.range(c))
        }
    }


    var contenedor = svg
        .selectAll('g')
        .data(data)
        .enter()
        .append('g')
        .attr('transform', (d, i) => {
            return 'translate('+ padding +','+ (rh + padding) * i + ')';
        });

    contador = -1;
    id = 0;

    contenedor.selectAll('rect')
        .data(function(d) { return d; })
        .enter()
        .append('rect')
            .attr('x', function(d, i) {
                return (rw + padding) * i;
            })
            .attr('width', rw)
            .attr('height', rh)
            .attr('id', function(d) {
                id += 1;
                return "h" + id;
            })
            .attr('fill', '#fff')
            .attr('stroke', function(d, i) {
                contador += 1;
                return color(contador);
            })
            .attr('stroke-width', '5px')
            .attr('rx', '50');

    contador = 0;
    id = -1;
    var microservicio = contenedor
        .selectAll('text')
        .data(function(d) { return d; })
        .enter()
        .append('text')
            .text(function(d, i) {
                contador += 1
                return 'Microservicio ' + (contador);
            })
            .attr('y', function(d, i) {
                return 37;
            })
            .attr('x', function(d, i) {
                return (rw + padding) * i + (rw / 2);
            })
            .attr('text-anchor', 'middle');

    var flecha = svg
        .append('svg:defs')
        .selectAll('market')
        .data(["end"])
        .enter()
        .append('svg:marker')
        .attr('id', String)
        .attr('viewBox', '0 -5 10 10')
        .attr('refX', 15)
        .attr('refY', 0.5)
        .attr('markerWidth', 2)
        .attr('markerHeight', 2)
        .attr('orient', 'auto')
        .attr('fill', 'purple')
        .append('svg:path')
        .attr('d', 'M0,-5L10,0L0,5');

    var link = svg
        .append('g')
        .selectAll('line')
        .data(datos[1])
        .enter()
        .append('svg:line')
        .attr('stroke-width', function(d) {
            return 10;
        })
        .style('stroke', function(d, i) {
            return color(i);
        })
        .attr('marker-end', "url(#end)");

    var n_rh = 1;
    var id = 0;
    var simulation = d3
    .forceSimulation()
        .nodes(d3.values(datos[0]))
        .force('x', d3.forceX().x(function(d) {
            id += 1;
            const x = d3.select('#h' + id).attr('x')

            n = parseInt(x);
            n = n + (rw / 2) + padding;

            return n;
        }).strength(0.5))
        .force('y', d3.forceY().y(function(d, i) {

        var altura = 0;

        if (i % columnas == 0 && i != 0) {
            n_rh += 1;
        }
        if ( n_rh == 1) {
            altura = ((rh * n_rh) / 2) + padding + 15;
        }
        if ( n_rh > 1) {
            altura = ((rh * n_rh) - (rh / 2)) + padding + 15;
        }
        return altura;
        }).strength(0.5))
        .force("link", d3.forceLink()
            .links(datos[1])
            .id(function(d) {
                return d.id;
            }).strength(0)
        )
        .on("tick", ticked);

    function ticked() {

        contenedores
            .attr('transform', function(d) {
                // console.log(d)
                return 'translate(' + d.x + ',' + d.y + ')';
            })

        link
            .attr('x1', function(d) {
                return d.source.x;
            })
            .attr('y1', function(d) {
                return d.source.y;
            })
            .attr('x2', function(d) {
                return d.target.x;
            })
            .attr('y2', function(d) {
                return d.target.y;
            });
    }

    function dragstarted(d) {
    simulation.alphaTarget(0.3).restart();

    d.fx = d3.event.x;
    d.fy = d3.event.y;

}

    function dragged(d) {

    d.fx = d3.event.x;
    d.fy = d3.event.y;

}

    function dragended(d) {
    simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}

    var drag = d3
        .drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended);

    var contenedores = svg
        .append('g')
        .selectAll('g')
        .data(datos[0])
        .enter()
        .append('g')
        .call(drag)
        .on("click", function(d) {
            mostrarInformacion(d);
        });


    var circulos = contenedores
        .append('circle')
        .attr('r', 12)
        .attr('fill', function(d,  i) {
            return color(i);
        }).style('cursor', 'hand');


    var texts = contenedores
        .append('text')
        .text((d) => d.nombre)
        .attr('text-anchor', 'middle')
        .style('cursor', 'hand');
    console.log('solo son pensamientos')

    let nombre = document.getElementById('name');
    const aux = d3.select('#dependencias');

    function mostrarInformacion(a) {
    $('#myModalClient').modal('show');
    source = a;
    console.log(source);
    var cont = 0;
    const dependencias = aux.selectAll('li')
        .data(datos[1].filter(function(d) {
                console.log(d);
                return d.source == source || d.target == source;
            }));
        dependencias
        .enter()
            .append('li')
            .style('color', 'purple')

        .merge(dependencias)
            .transition().duration(1000)
            .text(function(d, i) {
                console.log(d, i);
                cont += 1;
                return d.source.nombre + ' > ' + d.target.nombre;
            })
            .style('color', 'green');

        d3.select('#dependencias').selectAll('li')
            .data(datos[1].filter(function(d) {
                return d.source == source || d.target == source;
            }))
            .exit()
            .remove();

    nombre.innerHTML = 'ID historia de usuario: ' + a.id;
    if (cont == 0) {
        d3.select('#descripcion')
            .select('span')
            .style('display', 'block');
    } else {
        d3.select('#descripcion')
            .select('span')
            .style('display', 'none');
    }

}
}









datos = {
    nodes: [
        { name: "h1", value: 12 },
        { name: "h2", value: 12 },
        { name: "h3", value: 12 },
        { name: "h4", value: 12 },
        { name: "h5", value: 12 },
        { name: "h6", value: 12 },
        { name: "h7", value: 12 },
        { name: "h8", value: 12 },
        { name: "h9", value: 12 },
        { name: "h10", value: 12 }



    ],
    links: [
        { source: "h1", target: "h2" },
        { source: "h2", target: "h3" },
        { source: "h3", target: "h1" },
        { source: "h3", target: "h4" },
        { source: "h3", target: "h5" },
        { source: "h1", target: "h6" },
        { source: "h2", target: "h10"},


    ]
}







$(function() {
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {
            'action': 'searchdata'
        },
        dataType: 'json',
    }).done(function(data) {
        imprimir(data);

    }).fail(function(jqXHR, textStatus, errorThrown) {
        alert(textStatus + ': ' + errorThrown);
    }).always(function(data) {

    });


    $('#myModalClient').on('hidden.bs.modal', function(e) {
        $('#frmAccion').trigger('reset');
    });

    $('#frmAccion').on('submit', function(e) {
        e.preventDefault();
        $('#myModalClient').modal('hide');
    });
})



