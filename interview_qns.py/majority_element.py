class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        n = len(nums)
        for index, element in enumerate(nums):
            if element not in dict:
                dict[element] =1
            else:
                dict[element] += 1
        for key, value in dict.items():
            if value > (n/2):
                return key
    
    # javascript solution
    # majorityElement(nums) {
    #     let dict = {};
    #     let n = nums.length;
    #     for (let i = 0; i < n; i++) {

    #         if (!dict[nums[i]]) {
    #            dict[nums[i]] = 1;
    #        } else {
    #           dict[nums[i]] += 1;
    #        }
    #     }
    #     for (let key in dict) {
    #         if (dict[key] > n / 2) {
    #             return key;
    #         }
    #     }
    # }
    