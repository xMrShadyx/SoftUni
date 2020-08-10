function scholarship(income, grade, min_salary) {
    income = parseFloat(income)
    grade = parseFloat(grade)
    min_salary = parseFloat(min_salary)

    let scholarship1 = min_salary * 0.35
    let excellent_scholarship = grade * 25

    if (income < min_salary && grade > 4.5 && grade < 5.5) {
        console.log(`You get a Social scholarship ${Math.floor(scholarship1)} BGN'`)
    } else if (grade >= 5.5) {
        console.log(`You get a scholarship for excellent results ${Math.floor(excellent_scholarship)} BGN`)
    } else {
        console.log('You cannot get a scholarship!')
    }

}

scholarship(300, 5.65, 420)