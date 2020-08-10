function metricConverter(convert, arg1, arg2) {
    convert = parseFloat(convert)
    arg1 = String(arg1)
    arg2 = String(arg2)
    let result = 0

    if (arg1 === 'mm' && arg2 ==='m') {
        result = convert / 1000
    } else if (arg1 === 'm' && arg2 ==='cm') {
        result = convert * 100
    } else if (arg1 === 'cm' && arg2 ==='mm') {
        result = convert * 10
    } else if (arg1 === 'm' && arg2 ==='mm') {
        result = convert * 1000
    } else if (arg1 === 'cm' && arg2 ==='m') {
        result = convert / 100
    } else if (arg1 === 'mm' && arg2 ==='cm') {
        result = convert / 10
    }
    console.log(result.toFixed(3))

}

metricConverter(45, 'cm', 'mm')