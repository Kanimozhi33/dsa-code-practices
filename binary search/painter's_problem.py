def findLargestMinDistance(boards:list, k:int):
    # Write your code here
    # Return an integer
    left = max(boards)
    right = sum(boards)

    while left <= right:
        mid = (left+right)//2
        add_up = 0
        sub_array = 1
        for num in boards:
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


# completed