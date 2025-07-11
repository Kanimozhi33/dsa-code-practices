/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function(address) {
    if(address.length === 0) return 0;
    let ans = "";
    for (let i =0; i < address.length; i++){
        if(address[i] === "."){
            ans+= "[.]"
        }
        else{
            ans+=address[i]
        }
    }
    return ans;
};