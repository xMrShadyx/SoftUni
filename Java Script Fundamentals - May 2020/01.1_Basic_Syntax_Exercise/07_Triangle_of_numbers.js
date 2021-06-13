function triangleNumbers(n) {
    for (let row = 1; row <= n; row++) {
        let output = '';
        for(let number = 1; number <= row; number++) {
            output += `${row} `;
        }
        console.log(output)

    }
}

triangleNumbers(6)