const texts = document.querySelector('.texts');
let parar = document.getElementById('pararGrabacion');
let iniciar = document.getElementById('iniciarGrabacion')

window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
window.SpeechGrammarList = window.SpeechGrammarList || window.webkitSpeechGrammarList;
window.SpeechRecognitionEvent = window.SpeechRecognitionEvent || window.webkitSpeechRecognitionEvent;

const grammar = '#JSGF V1.0; grammar palabras; public <palabra> = pre;';

const recognition = new window.SpeechRecognition();
var speechRecognitionList = new SpeechGrammarList();
speechRecognitionList.addFromString(grammar, 1);
recognition.grammars = speechRecognitionList;
recognition.lang = 'es-ES';
recognition.interimResults = true;
recognition.maxAlternatives = 1;

//recognition.continuous = true;

let p = document.createElement('p');

recognition.addEventListener('result', (e) => {
    const text = Array.from(e.results)
        .map(result => result[0])
        .map(result => result.transcript)
        .join('');
    p.innerText = text;
    texts.appendChild(p);

    if (e.results[0].isFinal){
        if (text.includes('hello')){
            p = document.createElement('p');
            p.classList.add('replay');
            p.innerText = 'Hi';
            texts.appendChild(p);
        }
        if (text.includes('what is your name') || text.includes("what's your name")){
            p = document.createElement('p');
            p.classList.add('replay');
            p.innerText = 'My Name is Arfan';
            texts.appendChild(p);
        }
        p = document.createElement('p');
    }
    console.log(text);

})

recognition.addEventListener('end', () => {
//    recognition.start();

})

iniciar.addEventListener('click', function () {
    recognition.start();
    iniciar.disabled = true;
});



parar.addEventListener('click', function () {
    recognition.stop();
    iniciar.disabled = false;
});