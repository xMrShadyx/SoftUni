function godzillaVsKong(budget, statists, price_per_statist) {
    budget = parseFloat(budget)
    statists = parseInt(statists)
    price_per_statist = parseFloat(price_per_statist)

    let decor_price = budget * 0.1
    let cloth_price = statists * price_per_statist

    if (statists > 150) {
        cloth_price = cloth_price * 0.9
    }

    let total_price = decor_price + cloth_price
    let result = Math.abs(total_price - budget)

    if (total_price > budget) {
        console.log(`Not enough money!`)
        console.log(`Wingard needs ${result.toFixed(2)} leva more.`)
    } else {
        console.log('Action!')
        console.log(`Wingard starts filming with ${result.toFixed(2)} leva left.`)
    }

}

godzillaVsKong(9587.88,222,55.68)