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


// if 1- indexed,
function twoSum(nums, target) {
  const map = {};
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (map.hasOwnProperty(complement)) {
      return [map[complement], i+1];
    }
    map[nums[i]] = i+1;
  }
  return [];
}


function twoSum(nums, target){
    let left = 0;
    let right = nums.length-1;
    while(left< right){
        const sum = nums[left] + nums[right];
        if (sum === target){
          return [left+1, right+1];
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