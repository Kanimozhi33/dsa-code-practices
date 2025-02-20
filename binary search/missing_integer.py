def missing_integer(nums,k):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] != mid+1:
            missing = nums[mid] - (mid+1)
            if missing < k:
                left = mid+1
            else:
                right = mid-1
    return right+1+k 
    # or else we can also return left+k

print(missing_integer([4,5,6],3))