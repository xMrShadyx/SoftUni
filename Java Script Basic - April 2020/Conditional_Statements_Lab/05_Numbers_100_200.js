function numRange1(args) {
    let num = Number(args)

    if (num < 100) {
        console.log('Less than 100')
    } else if (num > 200) {
        console.log('Greater than 200')
    } else {
        console.log('Between 100 and 200')
    }

}

numRange1(120)