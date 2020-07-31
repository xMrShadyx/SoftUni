function deposit(depositprice, timedeposit, yearfree) {
    let a = Number(depositprice) * (Number(yearfree) / 100)
    let feeyear = a / 12
    let result = Number(depositprice) + (Number(timedeposit) * feeyear)
    console.log(result)
}

deposit("2350", "6", "7")