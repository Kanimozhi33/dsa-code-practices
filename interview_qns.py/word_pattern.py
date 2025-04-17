class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        word_map = {}
        reverse_map = {}
        if len(pattern) != len(words):
            return False
        for word,letter in zip(words,pattern):
            if letter in word_map:
                if word_map[letter] != word:
                    return False
            elif word in reverse_map:
                if reverse_map[word] != letter:
                    return False
            else:
                word_map[letter] = word
                reverse_map[word] = letter

        return True 

