def find_int(a,b):
    i = 0
    j = 0
    while j<len(b):
        if a[i] != b[j]:
            return i 
        else:
            i+=1
            j+=1
    if j==len(b) and i< len(a):
        return i
    return 0