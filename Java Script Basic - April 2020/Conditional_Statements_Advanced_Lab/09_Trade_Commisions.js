function commissions(town, money) {
    town = String(town)
    money = Number(money)

    let commission = 0

        if (town === 'Sofia') {
            if (money >= 0 || money <= 500) {
                commission = money * 0.05
                console.log(commission)
            } else if (500 < money <= 1000) {
                commission = money * 0.07
                console.log(commission)
            } else if (1000 < money <= 10000) {
                commission = money * 0.08
                console.log(commission)
            } else if (money > 10000) {
                commission = money * 0.12
                console.log(commission)
            }

        } else if (town === 'Varna:') {
            if (0 <= money <= 500) {
                commission = money * 0.045
                console.log(commission)
            } else if (500 < money <= 1000) {
                commission = money * 0.075
                console.log(commission)
            } else if (1000 < money <= 10000) {
                commission = money * 0.10
                console.log(commission)
            } else if (money > 10000) {
                commission = money * 0.13
                console.log(commission)
            }

        } else if (town === 'Plovdiv:') {
            if (0 <= money <= 500) {
                commission = money * 0.055
                console.log(commission)
            } else if (500 < money <= 1000) {
                commission = money * 0.08
                console.log(commission)
            } else if (1000 < money <= 10000) {
                commission = money * 0.12
                console.log(commission)
            } else if (money > 10000) {
                commission = money * 0.145
                console.log(commission)
            }
        }

}

commissions('Sofia', 1500)