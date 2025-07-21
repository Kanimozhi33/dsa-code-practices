def palindrome(s,t):
    u = sorted(s)
    v = sorted(t)
    return u ==v


def valid_palindrome(n):
    s = str(n)
    return s == s[::-1]