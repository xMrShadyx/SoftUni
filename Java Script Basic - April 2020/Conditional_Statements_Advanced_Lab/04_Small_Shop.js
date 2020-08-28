function smallShop(drink, town, amount) {
    drink = String(drink)
    town = String(town)
    amount = parseFloat(amount)

    let price = 0

    if (drink === 'coffee') {
        if (town === 'Sofia') {
            price = 0.5
        } else if ( town === 'Plovdiv') {
            price = 0.4
        } else if (town === 'Varna') {
            price = 0.45
        }
    } else if (drink === 'water') {
        if (town === 'Sofia') {
            price = 0.8
        } else if ( town === 'Plovdiv') {
            price = 0.7
        } else if (town === 'Varna') {
            price = 0.7
        }
    } else if (drink === 'beer') {
        if (town === 'Sofia') {
            price = 1.2
        } else if (town === 'Plovdiv') {
            price = 1.15
        } else if (town === 'Varna') {
            price = 1.1
        }

    } else if (drink === 'sweets') {
        if (town === 'Sofia') {
            price = 1.45
        } else if (town === 'Plovdiv') {
            price = 1.3
        } else if (town === 'Varna') {
            price = 1.35
        }

    } else if (drink === 'peanuts') {
        if (town === 'Sofia') {
            price = 1.6
        } else if (town === 'Plovdiv') {
            price = 1.5
        } else if (town === 'Varna') {
            price = 1.55
        }

    }

    console.log(price * amount)

}

smallShop('sweets', 'Sofia', 2.23)