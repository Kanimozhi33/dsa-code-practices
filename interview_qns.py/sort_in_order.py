class Solution:
    def sortIt(self, arr):
        # code here
        
        odd =[] 
        even =[]
        for x in arr:
            if x %2 ==0:
                even.append(x)
            else:
                odd.append(x)
            
        odd.sort(reverse=True)
        even.sort()
        
        return odd+even
        
    