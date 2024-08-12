const a = [1,6,12,54,58,99,123 ]

function binarySearch(arr, target, left=0, right=arr.length-1) {
    if (left>right){
        return -1
    }
    let middle = Math.floor((left+right)/2)
    if (arr[middle] === target){
        return middle
    }
    if (arr[middle] > target) {
        return binarySearch(arr,target, left, middle-1)
    }
    if (arr[middle] < target){
        return binarySearch(arr, target, middle+1, right)
    }

}

binarySearch(a, 6)
