function minDistance(word1, word2) {
    let dp = []
    let m = word1.length
    let n = word2.length
    for (let i = 0; i < m + 1; i++) {
        let temp = []
        for (let j = 0; i < n + 1; j++) {
            if (i === 0) {
                temp.push(j)
            }
            else if (j === 0) {
                temp.push(i)
            }
            else {
                temp.push(null)
            }
        }
    }
    console.log(dp);
}

minDistance('feoij', 'fhdfu')