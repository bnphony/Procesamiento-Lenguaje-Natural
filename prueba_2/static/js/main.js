$(function () {



    $('.btnTxt').on('click', function() {
        console.log('Subir un Archivo');


    });

    $('#subirAudio').on('change', function() {

        console.log('Subir un Archivo de voz');
        var data = new FormData(document.getElementById('formUsuario'));
        data.append("action", "subir_aud");
        console.log(data.get('subirAudio'));

        var x = document.getElementById('id_relatoUsuario');

        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: data,
            dataType: 'json',
            processData: false,
            contentType: false,
            cache: false,
        }).done(function (data) {
            if (!data.hasOwnProperty('error')){
                //x.innerHTML = data['audio'];
                x.value = data['audio'];
            }
        }).fail(function (jqXHR, textStatus, errorThrown) {
            alert(textStatus + ': ' + errorThrown);
        }).always(function (data) {

        });
    });

    $('#btn_limpiar').on('click', function() {
        var x = document.getElementById('id_relatoUsuario');
        x.value = "";
    });


    $('#formUsuario').on('submit', function(e) {
        e.preventDefault();
        window.localStorage.removeItem('lista-accion');
        window.localStorage.removeItem('lista-backlog');
        console.log('FUnciona el submit')
        var data = new FormData(document.getElementById('formUsuario'));
        data.append("action", 'pre_procesar');
        console.log(data.get("relatoUsuario"));
        console.log(data.get("nombreUsuario"));
        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: data,
            dataType: 'json',
            processData: false,
            contentType: false,
            cache: false,
        }).done(function (data) {
            if(!data.hasOwnProperty('error')){
               window.location.href = data['url'];
            }
            console.log(data);
        }).fail(function (jqYHR, textStatus, errorThrown) {
            alert(textStatus + ': ' + errorThrown);
        }).always(function (data) {

        });
    });

    document.getElementById('subirTxt')
    .addEventListener('change', subir, false);

});

function subir(e){
    var archivo = e.target.files[0];
    if(!archivo) {
        return;
    }

    var lector = new FileReader();
    lector.onload = function(e) {
        var contenido = e.target.result;
        mostrarContenido(contenido);
    };
    lector.readAsText(archivo);
}

function mostrarContenido(contenido) {
    var elemento = document.getElementById('id_relatoUsuario');
    //elemento.innerHTML = contenido;
    elemento.value = contenido;
}








