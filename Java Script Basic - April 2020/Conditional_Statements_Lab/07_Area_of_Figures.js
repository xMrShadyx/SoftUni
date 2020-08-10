function areaOfFigures(shape, num1, num2) {
    shape = String(shape)
    let a = parseFloat(num1)
    let b = parseFloat(num2)

    if (shape === 'square') {
        let result = a * a
        console.log(result.toFixed(3))
    } else if ( shape === 'rectangle') {
        let result = a * b
        console.log(result.toFixed(3))
    } else if (shape === 'triangle') {
        let result = (a * b) / 2
        console.log(result.toFixed(3))
    } else if (shape === 'circle') {
        let result = (a * a) * Math.PI
        console.log(result.toFixed(3))
    }

}

areaOfFigures('circle', 6,20)