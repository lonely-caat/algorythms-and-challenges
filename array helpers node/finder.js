// This is a tough one!  The most common find operation is to an object that has a given property.  Rather than writing out a full function every time, it would be great if we has a shorthand syntax to find an object like this:
// findWhere(ladders, { height: '20 feet' });
// The object { ladders: '20 feet' } should be used as the search criteria - we would want to find a ladder whose 'height' property was '20 feet';
//
// Your goal: Write a 'findWhere' function that achieves this shorthand approach.  'findWhere' should return the found object.


var ladders = [
        { id: 1, height: 20 },
        { id: 3, height: 25 }
    ];

function findWhere(array, criteria){
    let crit = Object.keys(criteria)[0]
    return array.find(l=>l[crit]===criteria[crit])

}
console.log(findWhere(ladders, { height: 25 })); // result: { id:3, height: 25 }
