
class Solution {
    isPowerOfAnother(X, Y) {
        // code here
        if ( Y===1) return true;
        if (X === 1 && Y!= 1) return false;
        if (Y%X === 0){
            while (Y > 1 ){
            Y = Y/X
        }
        return Y===1
        }
        else {
            return false
        }
        
    }
}
