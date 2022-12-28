// function fiboRecursionMemoization(num, prevValues=[]){
//     let result
//
//     if (prevValues[num] != null){
//         return prevValues[num]
//     }
//     if(num <= 2) {
//         result = 1;
//     }
//     else {
//         result = fiboRecursionMemoization(num-1, prevValues) + fiboRecursionMemoization(num - 2, prevValues);
//     }
//     prevValues[num] = result
//     return result
// }
//
// console.log(fiboRecursionMemoization(100))


// function square(num) {
//     result = 0
//     for (let el in [...Array(num)]) {
//         for (let element in [...Array(num)]) {
//             result += 1
//         }
//     }
//     return result
// }


function fiboRecursionMemoization(num, prevValues = []){
    let result
    if (prevValues[num] != null){
        return prevValues[num]
    }
    if (num <= 2){
        result = 1
    }
    else {
        result = fiboRecursionMemoization(num -1, prevValues) + fiboRecursionMemoization(num -2, prevValues)
    }
    prevValues[num] = result
    return result
}


console.log(fiboRecursionMemoization(8))
