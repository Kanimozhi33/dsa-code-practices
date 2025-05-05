function bestPrice(price, k) {
    if (price.length < k) {
        return 0;
    }

    let total = price.slice(0, k).reduce((sum, num) => sum + num, 0);
    let maxTotal = total;

    for (let i = 0; i < price.length - k; i++) {
        total -= price[i];
        total += price[i + k];
        maxTotal = Math.max(total, maxTotal);
    }

    return maxTotal;
}