/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
    if (n < 0) {
        return 0;}
    let count = 0;
    while (n!==0){
        count ++;
        n = n & (n-1);
    }
    return count;
};