class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        const monkeCanEatAll = (k) => {
            let totalHours = 0;
            for (const pile of piles) {
                totalHours += Math.ceil(pile / k);
            }
            return totalHours <= h;
        };
        let l = 1;
        let r = Math.max(...piles);

        while (l < r) {
            const mid = Math.floor((l + r) / 2);

            if (monkeCanEatAll(mid)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
}
