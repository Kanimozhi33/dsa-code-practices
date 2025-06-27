class Solution {
    simpleInterest(P, R, T) {
        // code here
        let ans = 0;
        ans = (P*R*T)/100;
        return ans.toFixed(2);
    }
}
