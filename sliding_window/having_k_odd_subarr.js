/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numberOfSubarrays = function(nums, k) {
    const countSubArray = function(nums, k) {
        let left = 0;
        let oddCount = 0;
        let arrCount = 0;

        for (let right = 0; right < nums.length; right++) {
            if (nums[right] % 2 === 1) {
                oddCount++; // Increase count when encountering an odd number
            }

            while (oddCount > k) { // Shrink window when odd count exceeds k
                if (nums[left] % 2 === 1) {
                    oddCount--; // Adjust odd count when moving left
                }
                left++;
            }

            arrCount += (right - left + 1); // Count valid subarrays ending at 'right'
        }
        return arrCount;
    }
    return countSubArray(nums,k)- countSubArray(nums,k-1);
};
