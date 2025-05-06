
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    let count = {};
    let left = 0;
    let maxFreq = 0;
    let maxLen = 0;
    for (let right = 0; right<s.length; right++){
        count[s[right]] = (count[s[right]] || 0)+1;
        maxFreq = Math.max(maxFreq, count[s[right]]);
        if ((right-left+1 - maxFreq ) > k){
            count[s[left]]--;
            left++;
        }
        maxLen = Math.max(maxLen,right-left+1)

    }
    return maxLen;

};