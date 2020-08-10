function swimmingRecord(rec_in_sec, distance, time_in_sec) {
    rec_in_sec = parseFloat(rec_in_sec)
    distance = parseFloat(distance)
    time_in_sec = parseFloat(time_in_sec)

    let needed_time = 0

    let need_to_swim = distance * time_in_sec
    let extra_time = Math.floor(distance / 15)
    extra_time = extra_time * 12.5

    let total = need_to_swim + extra_time
    let left_time = total - rec_in_sec

    if (rec_in_sec <= total) {
    console.log(`No, he failed! He was ${left_time.toFixed(2)} seconds slower.`)
    } else {
        console.log(`Yes, he succeeded! The new world record is ${total.toFixed(2)} seconds.`)
    }

}

swimmingRecord(55555.67,3017,5.03)