function longestSubStringLength(s){
    let seen = new Set();
    let maxlength = 0; left = 0;

    for (let right = 0; right < s.length; right++){
        while (seen.has(s[right])){
            seen.delete(s[left]);
            left++;
        }
        seen.add(s[right]);
        maxlength = Math.max(maxlength,right-left+1);
    }
    return maxlength;
}

console.log(longestSubStringLength("abcabcbb")); // 3