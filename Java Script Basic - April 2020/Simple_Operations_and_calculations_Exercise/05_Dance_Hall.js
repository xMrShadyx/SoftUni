function DanceHall(l, w, a) {
    let side1 = Number(l);
    let side2 = Number(w);
    let side3 = Number(a);

    let hall_width = (side1 * 100) * (side2 * 100)
    let wardrobe = (side3 * 100) * (side3 * 100)
    let bench_size = hall_width / 10
    let free_space = hall_width - wardrobe - bench_size
    let last = free_space / (40 + 7000)

    console.log(Math.floor(last).toFixed(0))

}

DanceHall(15.5,25.2,2.1)