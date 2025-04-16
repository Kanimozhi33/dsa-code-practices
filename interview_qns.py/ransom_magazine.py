class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map = {}
        for letter in magazine:
            if letter in hash_map:
                hash_map[letter] += 1
            else:
                hash_map[letter] = 1
        for letter in ransomNote:
            if hash_map.get(letter,0) > 0:
                hash_map[letter] -= 1
            else:
                return False
        return True