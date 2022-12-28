const axios = require('axios');


async function getData() {
    return await axios.get('https://jsonplaceholder.typicode.com/posts');
}

(async () => {
    let cat = (await getData())
})()
const cat = 'meow'
module.exports = {cat}