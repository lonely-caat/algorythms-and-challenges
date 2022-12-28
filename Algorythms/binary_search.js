const a = [1,6,12,54,58,99,123 ]

function bSearch(arr, bingo){
    let rightArr = arr.splice(arr.length/2)
    let leftArr = arr

        if (bingo === leftArr.at(-1)) {
            console.log('found', bingo, leftArr.at(-1),leftArr)

        } else if (bingo > leftArr.at(-1)) {
            console.log(leftArr, rightArr)
            return bSearch(rightArr, bingo)
        }
        else if (bingo < leftArr.at(-1)){
            console.log(leftArr, rightArr)
            return bSearch(leftArr, bingo)
        }

}

bSearch(a, 6)