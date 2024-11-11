// seconds

function calc_disc_acess(rr, avgseek, avgSPT) {
    // rr = rotational rate

    Tavgrotation = 1 / rr / 2 * 60
    Tavgseek = avgseek / 1000
    Tavgtranfer = (1 / rr * avgSPT * 60)

    return (Tavgrotation + Tavgseek + Tavgtranfer) * 1000
}


// console and conversion to ms 
console.log(calc_disc_acess(7200,9,400) + " ms");