

def sumofsubarr(arr):
    mod = 10**9 +7
    stack = []
    prev = [-1] * len(arr)
    next = [len(arr)]*len(arr)
    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        if stack:
            prev[i] = stack [-1]
        stack.append(i)
    stack = []
    for i in range(len(arr)-1,-1,-1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            next[i] = stack[-1]
        stack.append(i)
    total = 0
    for i in range(len(arr)):
        count = (i-prev[i])*(next[i]-i)
        total += arr[i] *count
        total %= mod
    return total

print(sumofsubarr([3,1,2,4]))