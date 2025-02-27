
def maximum_ones(nums,target):


    max_one_index = -1
    max_ones = 0
    min_index = float('inf')
    for i in range(len(nums)):
        occurrence = len(nums[i])
        num_of_ones = 0

        left = 0
        right = len(nums[i]) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[i][mid] == target:
                occurrence = mid
                right = mid - 1

            elif nums[i][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if occurrence != len(nums[i]):
            num_of_ones = len(nums[i])-occurrence
            if num_of_ones > max_ones or (num_of_ones == max_ones and i < min_index):
                max_ones = num_of_ones
                max_one_index = i
                min_index = i


    return max_one_index

print(maximum_ones([[0,0],[0,0]],1))