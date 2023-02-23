strs = ["flower","flow","floght"]


function commonPrefix(strs) {
    let commonLetters = ""
    let firstWord = strs[0]
    for (letterPosition in firstWord){
        for (word of strs){
            if (firstWord[letterPosition]!==word[letterPosition]){
                return commonLetters
            }
        }
        commonLetters += word[letterPosition]
    }
    return commonLetters
}

console.log(commonPrefix(strs))
