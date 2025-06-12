var countDigits = function (num){
    num = Math.abs(num);
    if (num === 0) return 1;
    let count = 0;
    let temp = num;
    while (temp >0) {
        count +=1 ;
        temp =Math.floor(temp/10);
    }

    return count;
}
