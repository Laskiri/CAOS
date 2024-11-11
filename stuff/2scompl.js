function calculateDecimalFrom2sComplement(binaryString) {
    // If the number is positive
    if (binaryString[0] === '0') {
        return parseInt(binaryString, 2);
    } 
    // If the number is negative
    else {
        let invertedBinaryString = '';
        let foundOne = false;
        for (let i = binaryString.length - 1; i >= 0; i--) {
            if (foundOne) {
                invertedBinaryString = (binaryString[i] === '0' ? '1' : '0') + invertedBinaryString;
            } else {
                invertedBinaryString = binaryString[i] + invertedBinaryString;
                if (binaryString[i] === '1') foundOne = true;
            }
        }
        return -parseInt(invertedBinaryString, 2);
    }
}

function binaryToHex(binaryString) {
    binaryString = binaryString.replace(/\s/g, '');
    let decimal = parseInt(binaryString, 2);
    let hex = decimal.toString(16);
    return hex;
}

function hexToDecimal(hexString) {
    return parseInt(hexString, 16);
}


console.log(1/7200 * 1/600 * 60 * 1000)
