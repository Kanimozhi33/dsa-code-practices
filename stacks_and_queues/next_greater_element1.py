# monotonic stack
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        nums_ind = {n:i for i,n in enumerate(nums1)}
        res  = [-1]*len(nums1)
        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                ind = nums_ind[val]
                res[ind] = curr
            if curr in nums1:
                stack.append(curr)
        return res