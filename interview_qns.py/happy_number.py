class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = {}
        while n != 1:
            if cycle.get(n, False):  # If number was seen before, it's in a loop
                return False
            
            cycle[n] = True  # Mark number as seen
            
            # Compute the sum of squares of digits
            addup = 0
            for digit in str(n):  
                addup += int(digit) ** 2  # Convert digit to int before squaring
            
            n = addup
        return True