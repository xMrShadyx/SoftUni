function sumSeconds(arg1, arg2, arg3) {
    let time_first = parseFloat(arg1)
    let time_second = parseFloat(arg2)
    let time_third = parseFloat(arg3)

    let total_time = time_first + time_second + time_third

    let minutes = Math.floor(total_time / 60)
    let seconds = Math.round(total_time % 60)

    if (seconds < 10) {
        console.log(`${minutes}:0${seconds}`)
    } else {
        console.log(`${minutes}:${seconds}`)
    }

}

sumSeconds(35,45,44)