a = [6,4,3,8,91,1]


// function sortIt(arr){
//     for (element in arr) {
//         for (el of arr ) {
//             if (arr[el] > arr[el + 1]) {
//                 [arr[el], arr[el + 1]] = [arr[el + 1], arr[el]]
//             }
//         }
//     }
//         return arr
//     }
//
//
// console.log(sortIt(a))

function bubbleSort(arr) {
    for (let elementsCounter in arr) {
        for (let nums = 0; nums < (arr.length - elementsCounter - 1); nums++) {
            if (arr[nums] > arr[nums + 1]) {
                [arr[nums], arr[nums + 1]] = [arr[nums + 1], arr[nums]];
            }
        }
    }
    return arr;
}
console.log(bubbleSort(a))