class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left+right)//2
            hours = 0
            for num in piles:
                hours += (num + mid - 1) // mid
            if hours > h:
                left = mid+1
            elif hours <=h:
                ans = mid
                right = mid-1

        return ans