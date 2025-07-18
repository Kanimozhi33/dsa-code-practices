def is_prime(n):
    if n<= 1:
        return False
    if n == 2:
        return True
    if n %2 == 0:
        return False
    for i in range(3, int(n**0.5)+1,2):
        if n%i == 0:
            return False
    return True
def twisted_prime(n):
    if not is_prime(n):
        return 0
    rev_n = int(str(n) [::-1])
    if is_prime:
        return 1
    else:
        return 0