function invNumber(args) {
    args = parseFloat(args)

    if (args < 100 && args !== 0) {
        console.log('invalid')
    }
    if (args > 200) {
        console.log('invalid')
    }
}

invNumber(150)