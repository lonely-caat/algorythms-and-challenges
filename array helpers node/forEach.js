function handlePosts() {
    var posts = [
        { id: 23, title: 'Daily JS News', oldId: 1 },
        { id: 52, title: 'Code Refactor City', oldId: 1 },
        { id: 105, title: 'The Brightest Ruby', oldId: 1 }
    ];

    posts.forEach(function(post) {
        console.log(post.id+post.oldId);
    })
}

handlePosts()

var images = [
    { height: 10, width: 30 },
    { height: 20, width: 90 },
    { height: 54, width: 32 }
];
var areas = [];

images.forEach(function(image){let c = image.height*image.width; areas.push(c)})





var images = [
    { height: '34px', width: '39px' },
    { height: '54px', width: '19px' },
    { height: '83px', width: '75px' },
];

var heights;

heights = images.map(function(arr){return arr.height;})





var trips = [
    { distance: 34, time: 10 },
    { distance: 90, time: 50 },
    { distance: 59, time: 25 }
];

var speeds;

speeds = trips.map(function(arr){return arr.distance/arr.time})







var paints = [ { color: 'red' }, { color: 'blue' }, { color: 'yellow' }];
function pluck(array, property) {
    return array.map(function(arr){return arr[property]})

}






var numbers = [15, 25, 35, 45, 55, 65, 75, 85, 95];

var filteredNumbers;

filteredNumbers = numbers.filter(function(nums){return nums>50})



var users = [
    { id: 1, admin: true },
    { id: 2, admin: false },
    { id: 3, admin: false },
    { id: 4, admin: false },
    { id: 5, admin: true },
];

var filteredUsers;

filteredUsers = users.filter(function(arr){return arr.admin===true})




var accounts = [
    { balance: -10 },
    { balance: 12 },
    { balance: 0 }
];

var account;

account = accounts.find(accounts=>accounts.balance===12)
