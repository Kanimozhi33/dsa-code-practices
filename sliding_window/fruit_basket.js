
function totalFruits(fruits) {
    //your code goes here
    let left = 0;
    let maxfruits = 0;
    let fruitCount = new Map();
    for (let right=0; right < fruits.length; right++){
    fruitCount.set(fruits[right],(fruitCount.get(fruits[right]) || 0)+1);
    while (fruitCount.size > 2){
        fruitCount.set(fruits[left],fruitCount.get(fruits[left])-1);
        if (fruitCount.get(fruits[left]) === 0){
        fruitCount.delete(fruits[left]);

        }
        left++;

    }
    maxfruits = Math.max(maxfruits,right-left+1);
    }
    return maxfruits;
}

console.log(totalFruits([1,2,1])); // 3
console.log(totalFruits([0,1,2,2])); // 3

// - left → Keeps track of the start of our window.
// - maxFruits → Stores the maximum number of fruits picked.
// - fruitCount → A Map that stores the types of fruits and their count.

// - This loop moves right across the array to collect fruits.
// - fruitCount.set(fruits[right], (fruitCount.get(fruits[right]) || 0) + 1);
// - .get(fruits[right]) → Retrieves the count of a fruit.
// - || 0 → If the fruit is not in the Map, it sets the initial count to 0.
// - .set(fruits[right], count + 1) → Updates the count of the fruit.

// - If fruitCount.size > 2, we have more than two fruit types → Shrink the window.
// - Reduce the count of fruits[left] since we’re moving left.
// - If count reaches 0, use .delete(fruits[left]) to remove it from the Map.

// - he difference right - left + 1 gives the current window size.
// - Keep track of the largest window found.

// - After looping through all trees, maxFruits will store the maximum number of fruits we can pick.

// 📌 Explanation of Map(), .set(), .get() and .delete()
// 1️⃣ Map() → Creates a new key-value storage where each fruit type is stored with its count.
// let fruitCount = new Map();


// 2️⃣ .set(key, value) → Adds or updates an entry in the Map.
// fruitCount.set(2, 4); // Fruit "2" now has a count of 4


// 3️⃣ .get(key) → Retrieves the value for a given key.
// console.log(fruitCount.get(2)); // Output: 4


// 4️⃣ .delete(key) → Removes a key from the Map when its count reaches zero.
// fruitCount.delete(2); // Removes fruit type "2" from Map



// 🚀 Why Use Map() Instead of an Object?
// ✔ Map() keeps keys in insertion order, whereas regular objects do not.
// ✔ Map() offers better performance for frequent additions/removals.
// ✔ .size gives us the number of keys directly, unlike objects where we'd use Object.keys().length.

// Example Runs
// console.log(totalFruit([1, 2, 1])); // Output: 3
// console.log(totalFruit([1, 2, 3, 2, 2])); // Output: 4



// 🔥 Final Takeaways
// - Sliding Window helps us efficiently track the maximum fruit count.
// - Map() allows efficient storage of fruit types & their counts.
// - .set() updates fruit counts, .get() retrieves counts, .delete() removes fruit types when needed.
// Hope this deep dive helps! Let me know if you want further clarifications 🚀😃!
