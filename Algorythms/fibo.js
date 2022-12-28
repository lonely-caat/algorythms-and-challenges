// function fibo(n) {
//     let a = [0, 1]
//     for (let el in [...Array(n)]) {
//         a.push(a[a.length - 1] + a[a.length - 2])
//     }
//     return a
// }
//
// function fiboAt(n){
//     for (let el in [...Array(5)]) {
//         a.push(a.at(-1) + a.at(-2))
//     }
//     return a
// }
//
//
// function fiboRecursion(num) {
//     if(num < 2) {
//         return num;
//     }
//     else {
//         return fiboRecursion(num-1) + fiboRecursion(num - 2);
//     }
// }
// const a = []
// for(let i = 0; i < 40; i++) {
//     a.push(fiboRecursion(i));
// }
// // console.log(a)

function fiboRecursionMemoization(num, prevValues=[]){
    let result
    if (prevValues[num] != null){
        return prevValues[num]
    }
    if (num <= 2) {
        result = 1;
    }
    else {
        result = fiboRecursionMemoization(num-1, prevValues) + fiboRecursionMemoization(num - 2, prevValues);
    }
    prevValues[num] = result
    return result
}



console.log(fiboRecursionMemoization(8))