function passGuess(pass) {
    let passg = String(pass)

    if (passg === 's3cr3t!P@ssw0rd') {
        console.log('Welcome')
    } else {
        console.log('Wrong password!')
    }

}

passGuess('s3cr3t!P@ssw0rd')