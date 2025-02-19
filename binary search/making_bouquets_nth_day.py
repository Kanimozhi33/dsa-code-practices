def bouquets(arr,m,k):
    if m*k > len(arr):
        return -1
    left = min(arr)
    right = max(arr)

    while left <= right:
        cut = 0
        bouquet = 0
        mid = (left+right)//2
        for num in arr:
            if num <=  mid:
                cut +=1
                if cut == k:
                    bouquet +=1
                    cut = 0
            else:
                cut = 0

        if bouquet >= m:
            if right == left:
                return left
            else:
                right = mid
        else:
            left = mid+1

    return left if left <= max(arr) else -1


print(bouquets([7,7,7,7,13,11,12,7],2,3))