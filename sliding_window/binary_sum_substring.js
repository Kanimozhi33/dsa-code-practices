/**
 * @param {number[]} nums
 * @param {number} goal
 * @return {number}
 * 
 * 
 * 
 */


// using prefix sum and hash map to count the number of subarrays with a given sum
var numSubarraysWithSum = function(nums, goal) {
    let count = 0;
    let sum = 0;
    let prefixSum = { 0: 1 }; // Store counts of prefix sums

    for (let num of nums) {
        sum += num;

        // Check if there exists a previous prefix sum equal to `sum - goal`
        if (prefixSum[sum - goal] !== undefined) {
            count += prefixSum[sum - goal];
        }

        // Update prefix sum count
        prefixSum[sum] = (prefixSum[sum] || 0) + 1;
    }

    return count;

};

var numSubarraysWithSum = function(nums, goal) {
    let left1 = 0, left2 = 0, sum1 = 0, sum2 = 0, count = 0;

    for (let right = 0; right < nums.length; right++) {
        sum1 += nums[right];
        sum2 += nums[right];

        while (sum1 > goal && left1 <= right) {
            sum1 -= nums[left1];
            left1++;
        }

        while (sum2 > goal - 1 && left2 <= right) {
            sum2 -= nums[left2];
            left2++;
        }

        count += left2 - left1;
    }

    return count;
};

// Example Test Case
var numSubarraysWithSum = function(nums, goal) {
    let left1 = 0, left2 = 0, sum1 = 0, sum2 = 0, count = 0;

    for (let right = 0; right < nums.length; right++) {
        sum1 += nums[right];
        sum2 += nums[right];

        while (sum1 > goal && left1 <= right) {
            sum1 -= nums[left1];
            left1++;
        }

        while (sum2 > goal - 1 && left2 <= right) {
            sum2 -= nums[left2];
            left2++;
        }

        count += left2 - left1;
    }

    return count;
};

var numSubarraysWithSum = function(nums, goal) {
    let left1 = 0, left2 = 0, sum1 = 0, sum2 = 0, count = 0;

    for (let right = 0; right < nums.length; right++) {
        sum1 += nums[right];
        sum2 += nums[right];

        while (sum1 > goal && left1 <= right) {
            sum1 -= nums[left1];
            left1++;
        }

        while (sum2 > goal - 1 && left2 <= right) {
            sum2 -= nums[left2];
            left2++;
        }

        count += left2 - left1;
    }

    return count;
};

// using slidig window to count the number of subarrays with a given sum
var numSubarraysWithSum = function(nums, goal) {
    let left1 = 0, left2 = 0, sum1 = 0, sum2 = 0, count = 0;

    for (let right = 0; right < nums.length; right++) {
        sum1 += nums[right];
        sum2 += nums[right];

        while (sum1 > goal && left1 <= right) {
            sum1 -= nums[left1];
            left1++;
        }

        while (sum2 > goal - 1 && left2 <= right) {
            sum2 -= nums[left2];
            left2++;
        }

        count += left2 - left1;
    }

    return count;

}
console.log(binarySumSubstring([1, 0, 1, 0, 1], 2)); // Output: 4