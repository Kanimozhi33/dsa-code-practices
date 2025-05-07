/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    if (nums.length === 0){
        return 0;
    }
    let numSet = new Set(nums);
    let maxCount = 0;
    for (let num of numSet){
        if (!numSet.has(num-1)){
            let currnum = num;
            let currlen = 1;
            while(numSet.has(currnum+1)){
                currnum +=1;
                currlen +=1;
            }
            maxCount = Math.max(maxCount,currlen);
        }
    }
    return maxCount;
};