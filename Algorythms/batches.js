function batches(recipe, ingredients) {
    if (recipe.length>ingredients.length){console.log(0)}
    milk = Object.values(ingredients)[0] / Object.values(recipe)[0]
    butter = Object.values(ingredients)[1] / Object.values(recipe)[1]
    cheese = Object.values(ingredients)[2] / Object.values(recipe)[2]

    item = Math.min(...[milk, butter, cheese])
    console.log(Math.floor(item))

}

const batches = (recipe, available) =>
    Math.floor(
        Math.min(...Object.keys(recipe).map(k => available[k] / recipe[k] || 0))
    )


// 0 batches can be made
batches(
    { milk: 100, butter: 50, flour: 5 },
    { milk: 132, butter: 48, flour: 51 }
)
batches(
    { milk: 100, flour: 4, sugar: 10, butter: 5 },
    { milk: 1288, flour: 9, sugar: 95 }
)

// 1 batch can be made
batches(
    { milk: 100, butter: 50, cheese: 10 },
    { milk: 198, butter: 52, cheese: 10 }
)

// 2 batches can be made
batches(
    { milk: 2, sugar: 40, butter: 20 },
    { milk: 5, sugar: 120, butter: 500 }
)