/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = [];
    let dictionary = {")":"(","]":"[","}":"{"};
    for (let i = 0; i < s.length;i++){
        if ((s[i] === "(") || (s[i] === "{") || (s[i] === "[")){
            stack.push(s[i])
        }
        else{
            if (stack.length != 0){
                let popped = stack.pop();
                if(dictionary[s[i]] != popped){
                    return false
                }
            
            }
            else{
                return false
            }
        }
    }
    
            
    return stack.length === 0;
    

};