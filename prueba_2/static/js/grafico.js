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

x.domain(datos.nodes.map((d) => d.name));
y.domain([0, d3.max(datos.nodes, d => d.value) + 7]);


var columnas = 4;

var data = []
var filas = (datos.nodes.length % columnas == 0) ? Math.floor(datos.nodes.length / columnas) : Math.floor(datos.nodes.length/columnas) + 1;


var c = (datos.nodes.length % columnas == 0 ) ? columnas : datos.nodes.length % columnas;
for (var i = 0; i < filas; i += 1) {
    if (i < filas - 1) {
        data.push(d3.range(columnas))
    } else {
        data.push(d3.range(c))
    }

}




var drag = d3
    .drag()
    .on("start", dragstarted)
    .on("drag", dragged)
    .on("end", dragended);

var padding = 20;

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
    .data(datos.links)
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

var simulation = d3
    .forceSimulation()
    .nodes(d3.values(datos.nodes))
    .force('x', d3.forceX().x(function(d) {
        const x = d3.select('#' + d.name).attr('x')

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
            .links(datos.links)
            .id(function(d) {
                return d.name;
            }).strength(0)

        )

        .on("tick", ticked);



var contenedores = svg
    .append('g')
    .selectAll('g')
    .data(datos.nodes)
    .enter()
    .append('g')
    .call(drag)
    .on("click", function(d) {
        mostrarInformacion(d);
    });


let nombre = document.getElementById('name');

const aux = d3.select('#dependencias');







function mostrarInformacion(a) {
    $('#myModalClient').modal('show');
    source = a;
    var cont = 0;
    const dependencias = aux.selectAll('li')
        .data(datos.links.filter(function(d) {
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
                return d.source.name + ' > ' + d.target.name;
            })
            .style('color', 'green');

        d3.select('#dependencias').selectAll('li')
            .data(datos.links.filter(function(d) {
                return d.source == source || d.target == source;
            }))
            .exit()
            .remove();

    nombre.innerHTML = 'ID historia de usuario: ' + a.name;
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

var circulos = contenedores
    .append('circle')
    .attr('r', d => d.value)
    .attr('fill', function(d,  i) {
        return color(i);
    }).style('cursor', 'hand');


var texts = contenedores

    .append('text')
    .text((d) => d.name)
    .attr('text-anchor', 'middle')
    .style('cursor', 'hand');

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

$(function() {
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {
            'action': 'searchdata'
        },
        dataType: 'json',
    }).done(function(data) {
//        imprimir(data);
        console.log(data);
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



