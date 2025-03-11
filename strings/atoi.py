class Solution:
    def myAtoi(self, s: str) -> int:
        
        string = s.strip()
        if not string:
            return 0
        index = 0
        sign = 1
        res = 0
        
        if string[0] in ("-", "+"):
            if string[0] == "-":
                sign = -1
            index += 1
        
        while index < len(string):
            if not string[index].isdigit():
                break
            res = res * 10 + int(string[index])
            index += 1
        res *= sign
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
        return res