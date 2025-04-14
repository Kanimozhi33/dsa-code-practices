class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        nge = [-1] * len(nums)
        n = len(nums)
        for i in range(2*n-1,-1,-1):
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            if i < n:
                if not stack:
                    nge[i] = -1
                else:
                    nge[i] = stack[-1]
            stack.append(nums[i%n])
        return nge