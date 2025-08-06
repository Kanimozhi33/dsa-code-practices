class Solution:
    def isPalindrome(self, s):
        removed = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        reversed = removed[::-1]
        if removed == reversed:
            return True
        else:
            return False
        
# js 

# var isPalindrome = function(s) {
#     const cleaned = s.replace(/[^a-zA-Z0-9]/g,'').toLowerCase();
#     const reversed = cleaned.split('').reverse().join('');
#     return cleaned === reversed;
# };