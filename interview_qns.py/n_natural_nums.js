class Solution {
    /**
     * @param number n
     * @returns number
     */
    findSum(n) {
        // code here
        if (n<0) return 0
        let ans = 0;
        ans = n* ((n+1)/2)
        return ans
    }
}
