//cake 45
// gofrette - 5.8
// pancake 3.2

function  charityCampaign(days,chefs,cakes,gofrettes,pancakes) {
    let price_cake = Number(cakes) * 45
    let price_goff = Number(gofrettes) * 5.8
    let price_pancakes = Number(pancakes) * 3.2
    let result = ((price_cake + price_goff + price_pancakes) * 8) * Number(days)
    console.log(result)
    let result2 = result / 8
    console.log(result2)
    let last_result = result - result2
    console.log(last_result)
}

charityCampaign(131,5,9,33,46)