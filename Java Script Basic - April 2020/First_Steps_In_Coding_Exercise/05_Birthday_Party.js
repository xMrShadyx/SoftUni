function birthDay(rent) {
    let cakePrice = Number(rent) * 0.20
    let drinkPrice = cakePrice * 0.55
    let animatorPrice = Number(rent) / 3
    let result = Number(rent) + cakePrice + drinkPrice + animatorPrice
    console.log(result)

}

birthDay("3720")