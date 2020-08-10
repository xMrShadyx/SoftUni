function Charity(days, chefs, cake, goff, pancake) {
    let day = Number(days)
    let chef = Number(chefs)
    let cake1 = Number(cake)
    let gof = Number(goff)
    let panc = Number(pancake)

    let amount_cakes = cake1 * 45
    let amount_goff = gof * 5.8
    let amount_pancake = panc * 3.2

    let total_price = (amount_cakes + amount_goff + amount_pancake) * chef
    let total_for_days = total_price * day
    let result = (total_for_days / 8) - total_for_days

    console.log(Math.abs(result).toFixed(2))

}

Charity(131, 5, 9, 33, 46)