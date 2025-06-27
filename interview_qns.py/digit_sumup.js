class Solution {
    sumOfDigits(n) {
        // code here
        if (n<0) return 0;
        let ans = 0;
        let digit = n.toString().split('').map(Number);
        while (digit.length !== 0) {
            ans+= digit.pop()
        }
        return ans
    }
}