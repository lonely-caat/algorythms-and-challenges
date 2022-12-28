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
a = [6,4,3,8,91,1]
console.log(bubbleSort(a))