class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        def sumOfElements(nums, isMax):
            stack = []
            total = 0
            n = len(nums)

            for i in range(n + 1):
                while stack and (i == n or (nums[stack[-1]] > nums[i] if isMax else nums[stack[-1]] < nums[i])):
                    j = stack.pop()
                    left = j - (stack[-1] if stack else -1)
                    right = i - j
                    total += nums[j] * left * right
                stack.append(i)

            return total
        maxi = sumOfElements(nums, True)
        mini = sumOfElements(nums, False)

        return  mini-maxi