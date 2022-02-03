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

    $('.accion').on('click', function() {
        console.log('a');
    });
});

var n_datos = 0;

function imprimir(data){
//    $.each(this.data, console.log(data.relatoUsuario));
    n_datos = data.length;
    for (i = 0; i < data.length; i++){
        var nuevo = '<div class="accion" id="'+data[i].id+'" data-id="'+(i + 1)+'"> ' +
        '<div class="div_numero"><p class="numero">'+(i+1)+'</p></div>' +
        '<div><p class="relato"><em class="relato1"> COMO: </em>'+data[i].usuario+'</p>' +
        '<p class="que"><em class="q"> NECESITO QUE EL SISTEMA ME PERMITA: </em>'+data[i].que+'</p>' +
        '<p class="para_que"><em class="para_que1"> CON LA FINALIDAD DE: </em>'+data[i].para_que+'</p>' +
        '</div>' +
        '<div><p class="eliminar">X</p></div>'
        '</div>';
        $("#lista-acciones").append(nuevo);
    }
    console.log($("#lista-acciones").find('.relato'));
}

function enumerar() {
    var numeros = document.getElementsByClassName('numero');
    for (i = 0; i < numeros.length; i ++) {
        numeros[i].innerHTML = i + 1;
    }
}

function eliminarElemento(item) {
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {
            'action': 'eliminar_data',
            'id': item
        },
        dataType: 'json',
    }).done(function(data) {
        if(!data.hasOwnProperty('error')) {
            console.log('Se elimino el elemento');
        }
    }).fail(function(jqXHR, textStatus, errorThrown) {
        alert(textStatus + ': ' + errorThrown);
    }).always(function(data) {

    });
}

function ordenar(){
    const lista = document.getElementById('lista-acciones');

    const listaAuxiliar = Sortable.create(lista, {
        animation: 150,
        chosenClass: "seleccionado",
        dragClass: "drag",
        filter: ".filtrado",
        handle: ['.div_numero', '.eliminar'],
        // Se puede escoger el identifi fcfffador


        onChoose: function (e) {
            console.log(e.oldIndex);
            const item = e.item;
            console.log(item.id);
//            item.find('.eliminar').on('click', function() {
//                console.log('eliminado');
//            })
            contador = 0;
            console.log('afuera', contador);
            if (contador == 0) {
                $('#' + item.id + ' .eliminar').one('click', function() {
                    contador += 1;
                    console.log(contador);
                    alert_action('Notificacion', 'Esta seguro de eliminar esto', function() {
                        eliminarElemento(item.id);
                        item.parentNode.removeChild(item);
                        enumerar();
                    }, function() {

                    });

                });

            }

//            console.log($('#' + item.id + ' .relato')[0].innerHTML)
        },
        onEnd: (e) => {
            console.log('Se inserto un elemento');

            var item = e.item;
//            console.log($('#' +item.id+ ' .relato')[0].innerHTML);
//            $('#' +item.id+ ' .numero')[0].innerHTML = e.newIndex;
        },

        group: {
            name: 'lista-accion',
            pull: true

        },
        onRemove: (e) => {
            console.log('xxxx')
        },
        store: {
            // Guardamos el orden
            set: (sortable) => {
                const orden = sortable.toArray();
                localStorage.setItem(sortable.options.group.name, orden.join('-'));
            },
            //Obtener el orden sdfdf
            get: (sortable) => {
                const orden = localStorage.getItem(sortable.options.group.name);
                return orden ? orden.split('-') : [];
            }
        }
    });
}

//function Espera() {
//    $('#ID').text("Procesando");
//
//}