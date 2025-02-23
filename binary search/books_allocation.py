
def books_allocation(nums,m):
    if m > len(nums):
        return -1
    left = max(nums)

    right = sum(nums)
    while left <= right:
        mid = (left+right)//2
        person = 1
        book = 0
        for num in nums:
            if book + num > mid:
                person +=1
                book = num
                if person > m:
                    break
            else:
                book += num

        if person > m:
            left = mid+1
        else:
            right = mid-1
    return left

print(books_allocation([12, 34, 67, 90],2))