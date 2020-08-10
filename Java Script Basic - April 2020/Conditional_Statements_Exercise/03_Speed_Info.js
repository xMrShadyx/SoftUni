function speedInfo(args) {
    args = parseFloat(args)

    if (args <= 10) {
        console.log('slow')

    } else if (args > 10 && args <= 50) {
        console.log('average')

    } else if (args > 50 && args <= 150) {
        console.log('fast')

    } else if (args > 150 && args <= 1000) {
        console.log('ultra fast')

    } else {
        console.log('extremely fast')
    }

}

speedInfo(3500)