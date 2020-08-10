function Tailoring(tables, length, width) {
    let table = Number(tables)
    let length1 = Number(length)
    let width1 = Number(width)

    let area = table * (length1 + 2 * 0.30) * (width1 + 2 * 0.30)
    let total = table * (length1 / 2) * (length1 / 2)
    let last = (area * 7) + (total * 9)
    let bgn = last * 1.85

    console.log(`${last.toFixed(2)} USD`)
    console.log(`${bgn.toFixed(2)} BGN`)
}

Tailoring(5,1,0.50)