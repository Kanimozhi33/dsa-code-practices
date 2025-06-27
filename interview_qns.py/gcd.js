class Solution {
    gcd(a, b) {
        // code here
        let ans = [];
        for (let i = 1; i <= Math.min(a,b); i++){
            if (a%i === 0 && b%i === 0){
                ans.push(i)
            }
        }
        return ans[ans.length-1];
}
}