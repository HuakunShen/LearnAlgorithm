/**
Runtime: 4 ms, faster than 22.72% of C++ online submissions for Minimum Operations to Make Array Equal.
Memory Usage: 5.8 MB, less than 66.88% of C++ online submissions for Minimum Operations to Make Array Equal.
*/
class Solution {
public:
    int minOperations(int n) {
        int less_count = 0;
        for(int i = 0; i < n; i++) {
            int num = 2*i+1;
            if (num > n) {
                less_count += num - n;                
            }
        }
        return less_count;
    }
};