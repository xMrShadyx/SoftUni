function timePlus(arg1, arg2) {
    arg1 = Number(arg1)
    arg2 = Number(arg2)

    let time_in_minutes = arg1 * 60 + arg2
    let time_plus_15_min = time_in_minutes + 15

    let final_hour = Math.floor(time_plus_15_min / 60)
    let final_mins = time_plus_15_min % 60


    if (final_hour > 23) {
        final_hour = Math.abs(final_hour - 24)
    }



    if (final_mins < 10) {
        console.log(`${final_hour.toFixed(0)}:0${final_mins}`)
    } else {
        console.log(`${final_hour.toFixed(0)}:${final_mins}`)
    }
}

timePlus(0,44)