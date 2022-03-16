

jQuery(document).ready(function () {
    init();
    var subirVoz = document.getElementById('subirVoz');
    var grabadora_estado = document.getElementById('estado_grabadora');
    var a_id = null;
    let contador = 3;

    var cont = function() {
        if (contador > 0) {
            grabadora_estado.innerHTML = contador;
            contador--;
        } else {
            grabadora_estado.innerHTML = 'Grabando...';
            grabadora_estado.style.color = 'green';
            clearInterval(a_id);
        }
     }

    var $ = jQuery;

    var myRecorder = {

        objects: {
            context: null,
            stream: null,
            recorder: null
        },
        init: function () {
            if (null === myRecorder.objects.context) {
                myRecorder.objects.context = new (
                    window.AudioContext || window.webkitAudioContext
                );
            }


        },
        start: function () {
            var lista = document.querySelector("#listaDeDispositivos");
            contador = 3;

            var options = {audio: { deviceId: lista.value }, video: false};
            navigator.mediaDevices.getUserMedia(options).then(function (stream) {
                a_id = setInterval(cont, 300);
                myRecorder.objects.stream = stream;
                myRecorder.objects.recorder = new Recorder(
                        myRecorder.objects.context.createMediaStreamSource(stream),
                        {numChannels: 1}
                );
                myRecorder.objects.recorder.record();
            }).catch(function (err) {
//                var p = navigator.mediaDevices.getUserMedia(options);
                alert("Debe dar permiso para utilizar el micrófono");

            });
        },
        stop: function (listObject) {

            if (null !== myRecorder.objects.stream) {
                myRecorder.objects.stream.getAudioTracks()[0].stop();
            }
            if (null !== myRecorder.objects.recorder) {
                myRecorder.objects.recorder.stop();

                // Validate object
                if (null !== listObject
                        && 'object' === typeof listObject
                        && listObject.length > 0) {
                    // Export the WAV file
                    myRecorder.objects.recorder.exportWAV(function (blob) {
                        var url = (window.URL || window.webkitURL)
                                .createObjectURL(blob);
                        grabadora_estado.innerHTML = 'Estado';

                        var file = new Blob([blob], {type: "audio/wav"});

                        convertirAudio(file);


                    });
                }
            }
        }
    };

    // Prepare the recordings list
    var listObject = $('[data-role="recordings"]');



    // Prepare the record button
    $('[data-role="controls"] > button').click(function () {
        // Initialize the recorder
        myRecorder.init();


        // Get the button state
        var buttonState = !!$(this).attr('data-recording');

        // Toggle
        if (!buttonState) {
            myRecorder.start();
            $(this).attr('data-recording', 'true');

        } else {
            myRecorder.stop(listObject);
            $(this).attr('data-recording', '');


        }
    });

});

function iniciarContador() {

}


const init = () => {
    const tieneSoporteUserMedia = () =>
    !!(navigator.mediaDevices.getUserMedia)

    if (typeof MediaRecorder === "undefined" || !tieneSoporteUserMedia()) {
        return alert("Su navegador web no cumple los requisitos; Utilize otro navegador, por favor!");
    }

    const $listaDeDispositivos = document.querySelector("#listaDeDispositivos");

    const limpiarSelect = () => {
        for (let x = $listaDeDispositivos.options.length - 1; x >= 0; x--) {
            $listaDeDispositivos.options.remove(x);
        }
    };

    const llenarLista = () => {
        navigator.mediaDevices
            .enumerateDevices()
            .then(dispositivos => {
                limpiarSelect();
                dispositivos.forEach((dispositivo, indice) => {
                    if (dispositivo.kind === "audioinput") {
                        console.log('Tiene dispositivo');
                        const $opcion = document.createElement("option");
                        $opcion.text = dispositivo.label  || `Dispositivo ${indice + 1}`;
                        $opcion.value = dispositivo.deviceId;
                        $listaDeDispositivos.appendChild($opcion);
                    }
                })
            })
    };
    llenarLista();
    console.log("se cargo el init()")
}


function convertirAudio(audio1) {

    var x = document.getElementById('id_relatoUsuario');
    var data = new FormData();
    data.append("audio", audio1)
    data.append("action", 'audio');
//    console.log('TIPO: ', typeof(data.get("audio")));

//    console.log(data.get("action"));
//    console.log('CONTENIDO: ', data.get("audio"));
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
           x.value += data['audio'] + ' ';
        }
        console.log(data);
    }).fail(function (jqYHR, textStatus, errorThrown) {
        alert(textStatus + ': ' + errorThrown);
    }).always(function (data) {

    });
}


