def shipping_packages(nums,days):
    left = max(nums)
    right = sum(nums)

    while left< right:
        day = 1
        sum_up = 0
        mid = (left+right)//2
        for num in nums:
            if sum_up +num > mid:
                day +=1
                sum_up = 0
            sum_up += num
        if day <= days:
           right = mid
        elif day > days:
            left = mid+1
    return left

print(shipping_packages([1,2,3,4,5,6,7,8,9,10],5))