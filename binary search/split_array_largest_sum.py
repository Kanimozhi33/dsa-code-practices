
def split_arrays(nums,k):
    left = max(nums)
    right = sum(nums)
    while left <= right:
        mid = (left+right)//2
        add_up = 0
        sub_array = 1
        for num in nums:
            if add_up +num > mid:
                sub_array +=1
                add_up = num
                if sub_array > k:
                    break
            else:
                add_up+=num
        if sub_array > k:
            left = mid+1
        else:
            right = mid-1
    return left


print(split_arrays([1,4,4],3))
