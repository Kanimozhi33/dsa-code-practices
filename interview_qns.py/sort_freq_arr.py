def frq_sort(arr):
    freq = {}
    for num in arr:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    sorted_arr = sorted(arr, key = lambda x: (-freq[x], x))
    return sorted_arr      