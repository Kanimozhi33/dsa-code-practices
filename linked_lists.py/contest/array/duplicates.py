class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_map = {}
        for x in nums:
            if x not in dict_map:
                dict_map[x] = 1
            else:
                return True
        return False