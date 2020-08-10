function bonusScore(score) {
    score = Number(score)
    let bonus = 0.0

    if (score <= 100) {
        bonus = 5
    } else if (score > 1000) {
        bonus = score * 0.1
    } else {
        bonus = score * 0.2
    }

    if (score % 2 === 0) {
        bonus += 1
    } else if (score % 10 === 5) {
        bonus += 2
    }

    let result = bonus + score

    console.log(bonus)
    console.log(result)


}

bonusScore(15875)