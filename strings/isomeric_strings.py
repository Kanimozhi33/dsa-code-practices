def isomeric_string(s,t):
    if len(s) != len(t):
        return False
    map1 = []
    map2 = []
    for ltr in s:
        map1.append(s.index(ltr))
    for ltr in t:
        map2.append(t.index(ltr))
    if map1 == map2:
        return True
    return False