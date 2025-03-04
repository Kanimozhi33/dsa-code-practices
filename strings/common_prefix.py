def longest_common_str(strs):
    res = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]

    return res


print(longest_common_str(["flow"]))


def common_prefix(str):
    res = ""
    sorted_str = sorted(str)
    first = sorted_str[0]
    last =sorted_str[-1]
    for i in range(min(len(first),len(last))):
        if first[i] != last[i]:
            return res
        res += first[i]
    return res


print(common_prefix(["flow","flower","f"]))
