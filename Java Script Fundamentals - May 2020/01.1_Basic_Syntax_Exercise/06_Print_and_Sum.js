function printSum(num1, num2) {
    let result = 0;
    let s = '';
    for (let i = num1; i <= num2; i++) {
        s += i + ' ';
        result += i;
    }
    console.log(s)
    console.log(`Sum: ${result}`)
}

printSum(5, 10)