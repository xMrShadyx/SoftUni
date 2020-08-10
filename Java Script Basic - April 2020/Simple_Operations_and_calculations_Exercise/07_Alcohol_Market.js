function Alcohol(price_whiskey, amount_beer, amount_wine, amount_rakia, amount_whiskey) {
    let var_price_whiskey = Number(price_whiskey)
    let var_amount_beer = Number(amount_beer)
    let var_amount_wine = Number(amount_wine)
    let var_amount_rakia = Number(amount_rakia)
    let var_amount_whiskey = Number(amount_whiskey)

    let price_rakia = var_price_whiskey / 2
    let price_wine = price_rakia - (0.4 * price_rakia)
    let price_beer = price_rakia - (0.8 * price_rakia)

    let rakia = price_rakia * var_amount_rakia
    let wine = price_wine * var_amount_wine
    let beer = price_beer * var_amount_beer
    let whiskey = var_amount_whiskey * var_price_whiskey

    let total = rakia + wine + beer + whiskey

    console.log(total.toFixed(2))


}

Alcohol(63.44, 3.57, 6.35, 8.15, 2.5 )