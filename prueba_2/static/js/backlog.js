$(function () {
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {
            'action': 'searchdata'

        },
        dataType: 'json',
    //    beforeSend: Espera,
    //    processData: false,
    //    contentType: false,
    //    success: function(resp) {
    //        $("#ID").html(resp);
    //    }
      }).done(function (data) {
        imprimir(data);
        ordenar();
    //    console.log(data);
      }).fail(function (jqXHR, textStatus, errorThrown) {
        alert(textStatus + ': ' + errorThrown);
      }).always(function (data) {

      });

});

function hslToRgb(h, s, l) {
    var r, g, b;

    if (s == 0) {
        r = g = b = l;
    } else {
        var hue2rgb = function hue2rgb(p, q, t) {
            if (t < 0) t += 1;
            if (t > 1) t -= 1;
            if (t < 1/6) return p + (q - p) * 6 * t;
            if (t < 1/2) return q;
            if (t < 2/3) return p + (q - p) * (2/3 - t) * 6;
            return p;
        }

        var q = l < 0.5 ? l * (1 + s) : l + s - l * s;
        var p = 2 * l - 1;
        r = hue2rgb(p, 1, h + 1/3);
        g = hue2rgb(p, 1, h);
        b = hue2rgb(p, q, h - 1/3);
    }

    return [Math.round(r * 255), Math.round(g * 255), Math.round(b * 255)];
}

var numero_colores = 0;

function generar_color(numeros){
    color = []
    rojo = []
    verde = []
    azul = []

    for (i = 0; i < numeros; i++){
        color_rojo = 255 - (255 * (i  / numeros))
        color_verde = 255 * (i / numeros)
        color_azul = 0
        color.push('rgb(' + color_rojo + ', '+ color_verde +', '+ color_azul +')')
//        console.log(color[i])
    }
//    var ratio = i;
//    if (min > 0 || max < 1) {
//        if (i < min) {
//            ratio = 0;
//        } else if (i > max) {
//            ratio = 1;
//        } else {
//            var range = max - min;
//            ratio = (i - min) / range;
//        }
//    }
//    var hue = ratio * 1.2 / 3.60;
//    var rgb = hslToRgb(hue, 1, 0.5);
//    return 'rgb('+ rgb[0] +', '+ rgb[1] +', '+ rgb[2] +')';

    return color
}


function colocar_c (color) {
    var numeros = document.getElementsByClassName('div_numero')
    for (i = 0; i < numeros.length; i ++) {
        numeros[i].style.backgroundColor = color[i];
    }

}

var ids = []

function imprimir(data){
//    $.each(this.data, console.log(data.relatoUsuario));
    color = generar_color(data.length);
    numero_colores = color;
    for (i = 0; i < data.length; i++){

        var nuevo = '<div class="accion" id="'+data[i].id+'" data-id="'+(i + 1)+'"> ' +
        '<div class="div_numero" id="numero'+data[i].id+'"><p class="numero"> HU '+(i+1)+'</p></div>' +
        '<div><p class="relato"><em class="relato1"> Como </em>'+data[i].usuario +
        '<em class="relato1"> necesito que el sistema me permita </em>' + data[i].que;
        if (data[i].para_que != 'sin_proposito'){
            nuevo += '<em class="relato1"> con la finalidad de </em> ' + data[i].para_que;
        }
        nuevo += '</p>' +
        '</div>' +
        '</div>';
        $("#lista-acciones").append(nuevo);

        ids[i] = data[i].id;
    }

    colocar_c(color);
    console.log($("#lista-acciones").find('.relato'));
}



function guardarOrden(orden) {
    console.log(orden);
    console.log(ids);
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {
            'action': 'orden_posicion',
            'orden': JSON.stringify(orden),
            'ids': JSON.stringify(ids)
        },

        dataType: 'json',
//        processData: false,
//        contentType: false,
//        cache: false,
    }).done(function(data) {
        if(!data.hasOwnProperty('error')) {
            console.log('se guardo el registro de orden')
        }
    }).fail(function(jqXHR, textStatus, errorThrown) {
        alert(textStatus + ': ' + errorThrown);
    }).always(function(data) {

    });
}


function ordenar(){
    const lista = document.getElementById('lista-acciones');

    Sortable.create(lista, {
        animation: 150,
        chosenClass: "seleccionado",
        dragClass: "drag",

        onChoose: function (e) {
            console.log(e.oldIndex);
        },
        onEnd: (e) => {

            var item = e.item;
//            console.log($('#' +item.id+ ' .relato')[0].innerHTML);
//            $('#' +item.id+ ' .numero')[0].innerHTML = e.newIndex;
//            console.log(numero_colores);
            colocar_c(numero_colores);
        },

        group: "lista-backlog",
        store: {
            // Guardamos el orden
            set: (sortable) => {
                const orden = sortable.toArray();
                localStorage.setItem(sortable.options.group.name, orden.join('-'));
                console.log('se guardo el orden', sortable)
                guardarOrden(orden);
            },
            //Obtener el orden sdfdf
            get: (sortable) => {
                const orden = localStorage.getItem(sortable.options.group.name);
                return orden ? orden.split('-') : [];
            }
        }
    });
    colocar_c(numero_colores);
}

//function Espera() {
//    $('#ID').text("Procesando");
//
//}