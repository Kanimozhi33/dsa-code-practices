/**
 * @param {number[]} values
 * @param {number[]} labels
 * @param {number} numWanted
 * @param {number} useLimit
 * @return {number}
 */
var largestValsFromLabels = function(values, labels, numWanted, useLimit) {
    
    const items = values.map((val, i) => ({ val, label: labels[i] }));

    
    items.sort((a, b) => b.val - a.val);

    const labelCount = new Map();
    let total = 0;
    let chosen = 0;

    for (let item of items) {
        if (chosen >= numWanted) break;

        const count = labelCount.get(item.label) || 0;
        if (count < useLimit) {
            total += item.val;
            labelCount.set(item.label, count + 1);
            chosen++;
        }
    }

    return total;
}
// was hard..need to learn more about sorting and maps