def aggr_cows(arr,cows):
    arr.sort()
    left = 0
    right = max(arr) - min(arr)
    ans = 0
    while left <= right:
        mid = (left+right)//2
        cow_count = 1
        last_cow = arr[0]

        for i in range(1,len(arr)):
            if arr[i] - last_cow >= mid:
                cow_count +=1
                last_cow = arr[i]



        if cow_count >= cows:
            ans = mid
            left = mid+1

        else:
            right = mid-1
    return ans

print(aggr_cows([1,2,3,4,6],3))