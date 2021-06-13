function vacation(nights, type, time) {
    let price = 0.0;
    switch (time) {
        case 'Friday':
            if (type === 'Students') {
                price = 8.45;
            } else if (type === 'Business') {
                price = 10.90;
            } else if (type === 'Regular') {
                price = 15;
            }
            break;
        case 'Saturday':
            if (type === 'Students') {
                price = 9.80;
            } else if (type === 'Business') {
                price = 15.60;
            } else if (type === 'Regular') {
                price = 20;
            }
            break;
        case 'Sunday':
            if (type === 'Students') {
                price = 10.46;
            } else if (type === 'Business') {
                price = 16;
            } else if (type === 'Regular') {
                price = 22.50;
            }0
            break;
    }
    if (type === 'Students' && nights >= 30) {
        price = price * 0.85;
    } else if (type === 'Business' && nights >= 100) {
        nights -= 10;
    } else if (type === 'Regular' && nights >= 10 && nights <= 20) {
        price = price * 0.95;
    }
    let result = price * nights
    console.log(`Total price: ${result.toFixed(2)}`)

}

vacation(
    40,
    "Regular",
    "Saturday"
)