/**
 * @param {string} text
 * @param {string} first
 * @param {string} second
 * @return {string[]}
 */
var findOcurrences = function(text, first, second) {
    const words = text.split(" ")
    const res = [];
    for (let i = 0; i< words.length-2; i++){
        if (words[i] === first && words[i+1] === second){
            res.push(words[i+2])
        }
    }
    return res;
};