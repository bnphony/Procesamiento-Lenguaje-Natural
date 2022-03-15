

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
//                        audio = new Audio(url);
//                        audio.play();
//                        console.log("TIPO luego sss:", typeof(audio));


                        // Prepare the playback
//                        var audioObject = $('<audio controls></audio>')
//                                .attr('src', url);
                        var file = new Blob([blob], {type: "audio/wav"});
//                        console.log(typeof(file));
//                        console.log(file);
//                        if (window.navigator.msSaveOrOpenBlob) {
//                            window.navigator.msSaveOrOpenBlob(file, file_name);
//                            console.log('entro en el primero');
//                        } else {
//                            console.log('entro en el segundo');
//                            var a = document.createElement("a");
//                            var url = URL.createObjectURL(file);
//                            a.href = url;
//                            a.download = 'audio.wav';
//                            document.body.appendChild(a);
//                            a.click();
//                            setTimeout(function() {
//                                document.body.removeChild(a);
//                                window.URL.revokeObjectURL(url);
//                            }, 0);
//                        }
                        convertirAudio(file);

                        // Prepare the download link
//                        var downloadObject = $('<a>&#9660;</a>')
//                                .attr('href', url)
//                                .attr('download', new Date().toUTCString() + '.wav');
//
//                        // Wrap everything in a row
//                        var holderObject = $('<div class="row"></div>')
//                                .append(audioObject)
//                                .append(downloadObject);

                        // Append to the list
//                        listObject.append(holderObject);
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
           x.value += data['audio'];
        }
        console.log(data);
    }).fail(function (jqYHR, textStatus, errorThrown) {
        alert(textStatus + ': ' + errorThrown);
    }).always(function (data) {

    });
}





//    const btnStartRecord = document.getElementById('btnStartRecord');
//    const btnStopRecord = document.getElementById('btnStopRecord');
//    var texto = document.getElementById('id_relatoUsuario')
//    const btnPlayText = document.getElementById('playText');
//
//    window.SpeechRecognition = window.webkitSpeechRecognition || window.SpeechRecognition
//    window.SpeechGrammarList = window.SpeechGrammarList || window.webkitSpeechGrammarList
//    window.SpeechRecognitionEvent = window.SpeechRecognitionEvent || window.webkitSpeechRecognitionEvent
//
//    const grammar = '#JSGF V1.0; grammar palabras; public <palabra> = pre;';
//    let recognition = new webkitSpeechRecognition || new SpeechRecognition();
//    var speechRecognitionList = new SpeechGrammarList();
//    speechRecognitionList.addFromString(grammar, 1);
//    recognition.grammars = speechRecognitionList;
//    recognition.lang = 'es-ES';
//    recognition.continuous = true;
//    recognition.interimResults = false;
//
//    recognition.onresult = (event) => {
//        const results = event.results;
//        const frase = results[results.length - 1][0].transcript;
//        texto.value += frase;
//        console.log(frase);
//        console.log(results[0][0].confidence)
//    }
//
//    recognition.onend = (event) => {
//        console.log('El microfono deja de escuchar');
//    }
//
//    recognition.onerror = (event) => {
//        console.log(event.error);
//    }
//
//    btnStartRecord.addEventListener('click', () => {
//        recognition.start();
//        btnStartRecord.disabled = true;
//        //btnStopRecord.disabled = false;
//    });
//
//    btnStopRecord.addEventListener('click', () => {
////        recognition.abort();
//        recognition.stop();
//        btnStartRecord.disabled = false;
//        //btnStopRecord.disabled = true;
//    });


//    btnPlayText.addEventListener('click', () => {
//        leerTexto(texto.value);
//    });


//    function leerTexto(texto){
//        const speech = new SpeechSynthesisUtterance();
//        speech.text = texto;
//        speech.volume = 1;
//        speech.rate = 1;
//        speech.pitch = 1;
//
//        window.speechSynthesis.speak(speech);
//    }