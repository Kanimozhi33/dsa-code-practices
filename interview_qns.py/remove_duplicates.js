/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    if (!nums) return 0
    let k = 1;
    for (let i = 1; i < nums.length; i++){
        if (nums[i] != nums[i-1]){
            nums[k] = nums[i];
            k += 1;
        }

    }
    return k;
};