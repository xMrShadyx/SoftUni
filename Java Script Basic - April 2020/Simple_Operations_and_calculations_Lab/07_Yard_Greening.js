function yardGreening(cubicm) {
    let total = cubicm * 7.61
    let discount = 0.18 * total
    let disc = total - discount
    console.log('The final price is: ' + disc + ' lv.')
    console.log('The discount is: ' + discount + ' lv.')

}

yardGreening(150)