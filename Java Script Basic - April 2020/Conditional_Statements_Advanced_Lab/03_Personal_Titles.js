function personalTitles(age, gender) {
    age = parseInt(age)
    gender = String(gender)

    if (gender === 'f') {
        if (age >= 16) {
            console.log('Ms.')
        } else {
            console.log('Miss')
        }
    }
    if (gender === 'm') {
        if (age >= 16) {
            console.log('Mr.')
        } else {
            console.log('Master')
        }
    }

}

personalTitles(12,'f')