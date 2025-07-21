# missing number from  n natural numbers
def missing_num(arr):
    n = len(arr)+1
    total = n*(n+1)//2
    actual = sum(arr)
    return total-actual