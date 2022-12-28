arr = [2,1,6,3,0]

for(elementsCounter in arr){
    for(let nums = 0;nums<(arr.length);nums++){
        if (arr[nums] > arr[nums+1]){
            [arr[nums], arr[nums+1]]=[arr[nums+1], arr[nums]]
        }
    }
}
console.log(arr)

const cat = require('./scratch_3.es6')
console.log(cat)

