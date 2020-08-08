function fishTank(length,width,height,percent) {
    let total = length * width * height
    let total_liters = total * 0.001
    let percen = percent * 0.01
    let last_total = total_liters * (1 - percen)
    console.log(last_total.toFixed(3))
}

fishTank(85,75,47,17)