var maxScore = function(cardPoints, k) {
    if (k === cardPoints.length){
        return cardPoints.reduce((acc,num) => acc+num,0);
        }

    let left = 0, max = 0;
    let sum = 0;
    let count = 0;

    for(let right = 0; right < cardPoints.length; right++){
        sum+= cardPoints[right] 
        count++;
        if (count >= k){
            max = Math.max(max,sum);
            sum -= cardPoints[left];
            left++;
            count--;
           
        }
    }
    return max
};

// Example Test Case
console.log(maxScore([1,2,3,4,5,6,1], 3)); // Output: 12