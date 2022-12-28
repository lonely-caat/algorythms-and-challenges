function getRandomRoll(max=6) {
    return Math.floor(Math.random() * max+1);
}

let randomDiceRollOne = getRandomRoll()
let randomDiceRollTwo = getRandomRoll()

let diceImageOne = `./images/dice${randomDiceRollOne}.png`
let diceImageTwo = `./images/dice${randomDiceRollTwo}.png`
document.querySelectorAll("img")[0].setAttribute("src", diceImageOne)
document.querySelectorAll("img")[1].setAttribute("src", diceImageTwo)




if(randomDiceRollOne > randomDiceRollTwo){
    document.querySelector("h1").innerHTML = "Player 1 wins"
}
else if(randomDiceRollOne < randomDiceRollTwo){
    document.querySelector("h1").innerHTML = "Player 2 wins"
}
else{document.querySelector("h1").innerHTML = "It's a draw baby 😸😸😸😸😸"}

