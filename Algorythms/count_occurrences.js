const input = [
    ['a', 'b', 'c'],
    ['c', 'd', 'f'],
    ['d', 'f', 'g'],
];

output = input
    .flat()
    .reduce((accumulator, currentValue) => {
        if(accumulator[currentValue]) {
            accumulator[currentValue] += 1;
        } else {
            accumulator[currentValue] = 1;
        }
        return accumulator;
    }, {});

console.log(output)