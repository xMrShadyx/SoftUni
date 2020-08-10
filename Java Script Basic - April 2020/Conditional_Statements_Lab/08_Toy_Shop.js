function toyStore(arg1, arg2, arg3, arg4, arg5, arg6) {
    let travel_price = parseFloat(arg1);
    let puzzles = Number(arg2);
    let talking_doll = Number(arg3);
    let teddy_brear = Number(arg4);
    let minions = Number(arg5);
    let trucks = Number(arg6);

    let total_money = puzzles * 2.6 + talking_doll * 3 + teddy_brear * 4.1
        + minions * 8.2 + trucks * 2

    let toy_amount = puzzles + talking_doll + teddy_brear
        + minions + trucks

    if (toy_amount >= 50)
        total_money = total_money* 0.75

    let rent = total_money * 0.9

    if (rent >= travel_price) {
        let last = rent - travel_price
        console.log(`Yes! ${last.toFixed(2)} lv left.`)
    } else {
        let last = travel_price - rent
        console.log(`Not enough money! ${last.toFixed(2)} lv needed.`)
    }

}

toyStore(320,8,2,5,5,1)