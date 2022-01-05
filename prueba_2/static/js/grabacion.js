//jQuery(document).ready(function () {
//    var $ = jQuery;
//    var myRecorder = {
//        objects: {
//            context: null,
//            stream: null,
//            recorder: null
//        },
//        init: function () {
//            if (null === myRecorder.objects.context) {
//                myRecorder.objects.context = new (
//                        window.AudioContext || window.webkitAudioContext
//                        );
//            }
//        },
//        start: function () {
//            var options = {audio: true, video: false};
//            navigator.mediaDevices.getUserMedia(options).then(function (stream) {
//                myRecorder.objects.stream = stream;
//                myRecorder.objects.recorder = new Recorder(
//                        myRecorder.objects.context.createMediaStreamSource(stream),
//                        {numChannels: 1}
//                );
//                myRecorder.objects.recorder.record();
//            }).catch(function (err) {});
//        },
//        stop: function (listObject) {
//            if (null !== myRecorder.objects.stream) {
//                myRecorder.objects.stream.getAudioTracks()[0].stop();
//            }
//            if (null !== myRecorder.objects.recorder) {
//                myRecorder.objects.recorder.stop();
//
//                // Validate object
//                if (null !== listObject
//                        && 'object' === typeof listObject
//                        && listObject.length > 0) {
//                    // Export the WAV file
//                    myRecorder.objects.recorder.exportWAV(function (blob) {
//                        var url = (window.URL || window.webkitURL)
//                                .createObjectURL(blob);
//
//                        // Prepare the playback
//                        var audioObject = $('<audio controls></audio>')
//                                .attr('src', url);
//
//                        // Prepare the download link
//                        var downloadObject = $('<a>&#9660;</a>')
//                                .attr('href', url)
//                                .attr('download', new Date().toUTCString() + '.wav');
//
//                        // Wrap everything in a row
//                        var holderObject = $('<div class="row"></div>')
//                                .append(audioObject)
//                                .append(downloadObject);
//
//                        // Append to the list
//                        listObject.append(holderObject);
//                    });
//                }
//            }
//        }
//    };
//
//    // Prepare the recordings list
//    var listObject = $('[data-role="recordings"]');
//
//    // Prepare the record button
//    $('[data-role="controls"] > button').click(function () {
//        // Initialize the recorder
//        myRecorder.init();
//
//        // Get the button state
//        var buttonState = !!$(this).attr('data-recording');
//
//        // Toggle
//        if (!buttonState) {
//            $(this).attr('data-recording', 'true');
//            myRecorder.start();
//        } else {
//            $(this).attr('data-recording', '');
//            myRecorder.stop(listObject);
//        }
//    });
//
//
//});
//
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
//
//
////    btnPlayText.addEventListener('click', () => {
////        leerTexto(texto.value);
////    });
//
//
//    function leerTexto(texto){
//        const speech = new SpeechSynthesisUtterance();
//        speech.text = texto;
//        speech.volume = 1;
//        speech.rate = 1;
//        speech.pitch = 1;
//
//        window.speechSynthesis.speak(speech);
//    }