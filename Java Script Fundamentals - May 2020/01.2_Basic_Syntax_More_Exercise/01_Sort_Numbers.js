function sortNumbers(input) {
    let list = [];
    list += input.sort().reverse().join('');
    for (let i = 0; i < list.length; i++)
        console.log(parseFloat(list[i]))
}

sortNumbers([
    '-1',
    '0',
    '2'
])