function rounding(doubleNum, fixedNum) {

    if (fixedNum > 15) {
        fixedNum = 15;
    }

    let result = parseFloat(doubleNum.toFixed(fixedNum));
    console.log(result);
}

rounding(5.5, 3)