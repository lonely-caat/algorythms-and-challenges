for (let doc of document.querySelectorAll('.drum')) {
    doc.addEventListener('click', function (){
        let innerHtml = this.innerHTML
        playSoundOnPress(innerHtml)
        animateImage(innerHtml)
    })
}
document.addEventListener('keydown', function (event) {
    playSoundOnPress(event.key)
    animateImage(event.key)
})

function animateImage(key){
    let selector = document.querySelector(`.${key}`)
    selector.classList.add('pressed')
    setTimeout(function(){
        selector.classList.remove('pressed')
    }, 100)
}

function playSound(src){
    let audio = new Audio(src);
    audio.play();
}

function playSoundOnPress(key){
    switch (key) {
        case('w'):
            playSound('sounds/crash.mp3')
            break;
        case('a'):
            playSound('sounds/kick-bass.mp3')
            break;
        case('s'):
            playSound('sounds/snare.mp3')
            break;
        case('d'):
            playSound('sounds/tom-1.mp3')
            break;
        case('j'):
            playSound('sounds/tom-2.mp3')
            break;
        case('k'):
            playSound('sounds/tom-3.mp3')
            break;
        case('l'):
            playSound('sounds/tom-4.mp3')
            break;
        default:
            alert(key)
    }
}
