class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        auto canEatAll = [&] (int k) -> bool {
            long long totalHours = 0;
            for (int pile : piles) {
                totalHours += (pile + k - 1) / k;
            }
            return totalHours <= h;
        };
        int l = 1;
        int r = *max_element(piles.begin(), piles.end());
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (canEatAll(mid)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
};
