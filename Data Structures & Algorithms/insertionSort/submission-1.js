/**
 * Pair class to store key-value pairs
 */
// class Pair {
//     /**
//      * @param {number} key The key to be stored in the pair
//      * @param {string} value The value to be stored in the pair
//      */
//     constructor(key, value) {
//         this.key = key;
//         this.value = value;
//     }
// }
class Solution {
    /**
     * @param {Pair[]} pairs
     * @returns {Pair[][]}
     */
    insertionSort(pairs) {
        const arr = pairs.slice() // don't mutate input
        const snapshots = [];

        for (let i = 0; i < arr.length; i++) {
            const current = arr[i];
            let j = i - 1;

            // Stable: shift only > keys
            while (j >= 0 && arr[j].key > current.key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = current;
            snapshots.push(arr.slice());
        }
        return snapshots;
    }
}
