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

function imprimir(data){
//    $.each(this.data, console.log(data.relatoUsuario));
    for (i = 0; i < data.length; i++){
        var nuevo = '<div class="accion" id="'+data[i].posicion+'" data-id="'+data[i].posicion+'"> ' +
        '<div class="div_numero"><p class="numero">'+(i+1)+'</p></div>' +
        '<div><p class="relato"><em class="relato1"> COMO: </em>'+data[i].usuario+'</p>' +
        '<p class="que"><em class="q"> NECESITO QUE EL SISTEMA ME PERMITA: </em>'+data[i].que+'</p>' +
        '<p class="para_que"><em class="para_que1"> CON LA FINALIDAD DE: </em>'+data[i].para_que+'</p>' +
        '</div>' +
        '</div>';
        $("#lista-acciones").append(nuevo);
    }
    console.log($("#lista-acciones").find('.relato'));
}
function ordenar(){
    const lista = document.getElementById('lista-acciones');

    Sortable.create(lista, {
        animation: 150,
        chosenClass: "seleccionado",
        dragClass: "drag",
        filter: ".filtrado",


        onChoose: function (e) {
            console.log(e.oldIndex);
        },
        onEnd: (e) => {
            console.log('Se inserto un elemento');
            var item = e.item;
//            console.log($('#' +item.id+ ' .relato')[0].innerHTML);
//            $('#' +item.id+ ' .numero')[0].innerHTML = e.newIndex;
        },

        group: "lista-accion",
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