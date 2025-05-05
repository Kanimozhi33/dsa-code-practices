def best_price(price,k):
    if len(price) < k :
        return 0
    total = sum(price[:k])
    maxtotal = total
    for i in range(len(price)-k):
        total -= price[i]
        total += price[i+k]
        maxtotal = max(maxtotal, total)
    return maxtotal

# javascript version:

# function bestPrice(price,k){
#    if (price.length < k) {
# return 0};
# }
#   let total = 0;
#   for (let i = 0; i < k; i++) {
#     total += price[i];
#   }
#   let maxtotal = total;
#   for (let i = 0; i < price.length - k; i++) {
#     total -= price[i];
#     total += price[i + k];
#     maxtotal = Math.max(maxtotal, total); 
#   }
#   return maxtotal;
# }
    