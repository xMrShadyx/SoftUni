function fruitShop(fruit, day, amount) {
    fruit = String(fruit)
    day = String(day)
    amount = Number(amount)

    let price = 0
    switch (day) {
        case 'Monday':
        case 'Tuesday':
        case 'Wednesday':
        case 'Thursday':
        case 'Friday':
            if (fruit === 'banana') {
                price = 2.50
                console.log((((price * amount) * 100) / 100).toFixed(2))
                break;
            } else if (fruit === 'apple') {
                price = 1.20
                console.log((((price * amount) * 100) / 100).toFixed(2))
                break;
            } else if (fruit === 'orange') {
                price = 0.85
                console.log((((price * amount) * 100) / 100).toFixed(2))
                break;
            } else if (fruit === 'grapefruit') {
                price = 1.45
                console.log((((price * amount) * 100) / 100).toFixed(2))
                break;
            } else if (fruit === 'kiwi') {
                price = 2.7
                console.log((((price * amount) * 100) / 100).toFixed(2))
                break;
            } else if (fruit === 'pineapple') {
                price = 5.5
                console.log((((price * amount) * 100) / 100).toFixed(2))
                break;
            } else if (fruit === 'grapes') {
                price = 3.85
                console.log((((price * amount) * 100) / 100).toFixed(2))
                break;
            }else {
                console.log('error')
            }
            break;

        case 'Saturday':
        case 'Sunday':
            if (fruit === 'banana') {
                price = 2.70
                console.log((((price * amount) * 100) / 100).toFixed(2))
                break;
            } else if (fruit === 'apple') {
                price = 1.25
                console.log((((price * amount) * 100) / 100).toFixed(2))
                break;
            } else if (fruit === 'orange') {
                price = 0.90
                console.log((((price * amount) * 100) / 100).toFixed(2))
                break;
            } else if (fruit === 'grapefruit') {
                price = 1.60
                console.log((((price * amount) * 100) / 100).toFixed(2))
                break;
            } else if (fruit === 'kiwi') {
                price = 3.00
                console.log((((price * amount) * 100) / 100).toFixed(2))
                break;
            } else if (fruit === 'pineapple') {
                price = 5.60
                console.log((((price * amount) * 100) / 100).toFixed(2))
                break;
            } else if (fruit === 'grapes') {
                price = 4.2
                console.log((((price * amount) * 100) / 100).toFixed(2))
                break;
            } else {
                console.log('error')
            }
            break;
        default:
            console.log('error')
            break;
    }
}

fruitShop('banana', 'Monday', 5)