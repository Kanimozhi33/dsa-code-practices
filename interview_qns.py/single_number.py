class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_dict ={}
        for element in nums:
            if element in count_dict:
                count_dict[element] +=1
            else:
                count_dict[element]=1
        for keys,values in count_dict.items():
            if values == 1:
                return keys