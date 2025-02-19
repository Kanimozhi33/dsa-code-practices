def smallest_divisor(nums,t):
    left = 1
    right = max(nums)
    while left <= right:
        add_up = 0
        mid = (left+right)//2
        for num in nums:
            add_up += (num+mid-1)//mid

        if add_up <= t:
            if left == right:
                return left
            else:
                right = mid
        else:
            left = mid+1
    return left

print(smallest_divisor([1,2,3,4,5], 8))