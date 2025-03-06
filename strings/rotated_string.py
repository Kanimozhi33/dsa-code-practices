class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        ans = goal+goal
        if s in ans:
            return True
        
        return False