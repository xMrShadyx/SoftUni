function yardGreening(cubicm) {
    let total = cubicm * 7.61
    let discount = 0.18 * total
    let disc = total - discount
    console.log('The final price is: ' + disc.toFixed(2) + ' lv.')
    console.log('The discount is: ' + discount.toFixed(2) + ' lv.')

}

yardGreening(540)