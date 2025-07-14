function twoSum(nums, target) {
  const map = {};
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (map.hasOwnProperty(complement)) {
      return [map[complement], i];
    }
    map[nums[i]] = i;
  }
  return [];
}


function twoSum(nums, target){
    let left = 0;
    let right = nums.length-1;
    while(left< right){
        const sum = nums[left] + nums[right];
        if (sum === target){
          return [left, right];
        }
        else if(left < target){
          left ++;
        }
        else{
          right --;
        }
     }
     return [];
}