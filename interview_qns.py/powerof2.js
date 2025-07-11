/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    if (n === 1) return true;
    if (n <1) return false;
    if (n%2 !== 0) return false;
    return(Math.log2(n) % 1 === 0)
};