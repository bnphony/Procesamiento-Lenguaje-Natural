$(function () {

    const estado = document.getElementById('estado');
    var a_id = null;
    let contador = 3;

     var cont = function() {
        if (contador > 0) {
            estado.innerHTML = contador;
            contador--;
        } else {
            estado.innerHTML = 'Habla...';
            estado.style.color = 'green';
            clearInterval(a_id);
        }
     }

    $('.btnVoz').on('click', function() {
        navigator.mediaDevices.getUserMedia({ audio: true })
            .then((stream) => {
                var audio = document.getElementById('id_relatoUsuario');
//                audio.innerHTML = 'Habla...'
                var btn_x = document.getElementById('estado');

//                btn_x.innerHTML = 'Habla...';
                contador = 3;

                a_id = setInterval(cont, 300);


                var btn = document.getElementById('btnVoz');
                btn.innerHTML = 'Grabando';

                $.ajax({
                    url: window.location.pathname,
                    type: 'POST',
                    data: {
                        "action": 'voz',
                    },
                    dataType: 'json',
                }).done(function (data) {
                    if(!data.hasOwnProperty('error')){
//                        btn.className = 'btn btn-danger btnVoz';
                        btn.innerHTML = 'Ingreso por Voz';
                        audio.value += data['voz'] + ' ';
//                        btn_x.innerHTML = 'Estado';
                    }

                }).fail(function (jqXHR, textStatus, errorThrown) {
                    alert(textStatus + ': ' + errorThrown);

                }).always(function (data) {
                    btn.innerHTML = 'Ingreso por Voz';
                    btn_x.innerHTML = 'Estado';
                    btn_x.style.color = 'black';
                });

            }).catch((err) => {
                console.log(err);
            });

    });

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








