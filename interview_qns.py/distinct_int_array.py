
def common_digits(self, nums):
    ans = []
    club_nums = "".join(str(num) for num in nums)
    for char in club_nums:
        if char not in ans:
            ans.append(char)
    return sorted(ans)