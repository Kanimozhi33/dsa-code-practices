// let num = 1111;
// let originalNum = num;
// let reversal = [];
// let temp = 0;
// while (num >0){
//     temp = num%10;
//     reversal.push(temp)
//     num = Math.floor(num/10);
// }
// if (reversal.join('') === originalNum.toString()){
//     console.log(true)
// }
// else{
//     console.log(false);
// }


// function sumOfDivisors(n) {
//     let sum = 0;
//     for (let i = 1; i <= n; i++) {
//         if (n % i === 0) {
//             sum += i;
//         }
//     }
//     return sum;
// }

// console.log(sumOfDivisors(5)); // Output: 6
// console.log(sumOfDivisors(12)); // Output: 28 (divisors: 1, 2, 3, 4, 6, 12)

// let x = 12;
// let y = (typeof x === typeof 12)
// console.log(y)





// const [task, setTask] = useState([])

// const TaskManager = () =>{
//     return (
//         <div><input id="tasks">
//         </input>
//         <button onClick={task = task.push()}>ok</button></div>
        
//     )
// }


// function removeDuplicates(nums){
//     if (!nums) return 0 
//     let sortedNums = nums.sorted();
//     let k =1;
//     for (let i =1; i< nums.length; i++){
//         if (sortedNums[i] != sortedNums[i-1]){
//             sortedNums[k] = sortedNums[i];
//             k +=1;
//         }
//     }
//     return sortedNums.slice(0,k)
// }


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


ans([1,2,3,4,5,6,7,8,1],3)