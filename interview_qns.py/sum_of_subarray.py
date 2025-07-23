class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum_up = 0
        min_len = float("inf")
        for right in range(len(nums)):
            sum_up += nums[right]
            while sum_up >= target:
                min_len = min(min_len,right-left+1)
                sum_up -= nums[left]
                left+=1
        if min_len == float("inf"):
            return 0
        else:
            return min_len


        