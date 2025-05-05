function longestOnes(nums,k){
    let left = 0;
    let right = 0;
    let maxCount = 0;
    let zeroCount = 0;
    while (right < nums.length){
        if (nums[right]===0){
            zeroCount++;
        }
        while (zeroCount > k){
            if (nums[left]===0){
                zeroCount--;
            }
            left++;
        }
        maxCount = Math.max(maxCount, right-left+1);
        right++;

}
    return maxCount;

}
console.log(longestOnes([1,0,0,1,1,0,1],2)); // 5