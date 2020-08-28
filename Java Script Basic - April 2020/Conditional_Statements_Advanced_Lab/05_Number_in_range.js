function rangeIn(args) {
    args = parseInt(args)

    if (args >= -100 && args <= 100 && args !== 0) {
        console.log('Yes')
    } else {
        console.log('No')
    }

}

rangeIn(100)