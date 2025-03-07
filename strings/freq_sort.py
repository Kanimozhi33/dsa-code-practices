def frequency_sort(str):
    dict = {}
    for s in str:
        if s in dict:
            dict[s] +=1
        else:
            dict[s] = 1
    sorted_dict = sorted(dict.items(), key=lambda item:item[1], reverse=True)
    ans = []
    for key, value in sorted_dict:
        ans.append(key*value)
    return "".join(ans)

print(frequency_sort("tree")) # eert