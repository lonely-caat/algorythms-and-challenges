function isValid(s){
    let stack = []
    let d = {'{':'}', '[':']', '(':')'}

    for (let element of s){
        if (element in d){
            stack.push(element)}

        else if (element !== d[stack.pop()]){
            return false
            }
    }
    return stack.length===0
}

console.log(isValid('{()}'))
