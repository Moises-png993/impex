function hammingDistance(str1, str2) {
    if (str1.length !== str2.length) {
        throw new Error("Las cadenas deben tener la misma longitud.");
    }
    let distance = 0;
    for (let i = 0; i < str1.length; i++) {
        if (str1[i] !== str2[i]) {
            distance++;
        }
    }
    return distance;
}

function findMostSimilar(inputString) {
    stringsList = [
        "SSNNNSNNNNNSS", "SSSNNNNNNNNSS", "SSSNNNSNNNNSS", "SSNNNNNNNNNSS",
        "NNNNNNNSSNNSS", "NNNNNNNSNNNSS", "NNNNSNNNNNNSS", "NNSNNSNNNNNSS",
        "NNSNNNNNNNNSS", "NNNNNSNNNNNSS", "NNNNNNNNNNNSS", "NNNNNNNSSNNLS",
        "NNNNNNNSNNNLS", "NNNNNNNNNSNLL", "NNNNNSNNNNNLS", "NNSNNNNNNNNLL",
        "NNNNNNNNNNNLL", "NNSSNNNNNNNLM", "NNSNNNNNNNNLS", "NNNSNNNNNNNLM",
        "NNNNNNNNNNNLS", "NNNNNNNSNNNTS", "NNNNNNNNNNSTS", "NNNNNNNNNNNTS",
        "NNNNNNNNNNNTL", "NNNNNNNNNNNLO", "NNNNNNNNNNNTO", "NNNNNNNNNNNOO",
        "NNNNNNNNNNNSO"
    ]
    let minDistance = Infinity;
    let mostSimilarString = "";

    stringsList.forEach(str => {
        let distance = hammingDistance(inputString, str);
        if (distance < minDistance) {
            minDistance = distance;
            mostSimilarString = str;
        }
    });

    return mostSimilarString;
}

module.exports = {
    hammingDistance,
    findMostSimilar
};
