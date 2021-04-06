# 1551. Minimum Operations to Make Array Equal

Medium

This is a Math problem.

Since the array is guaranteed to be able to be averaged, we can simply count the sum of difference between all numbers smaller than average and the average.

Time Complexity: O(n)

Space Complexity: O(1)

```python
class Solution:
    def minOperations(self, n: int) -> int:
        less_count = 0
        for i in range(n):
            num = 2*i+1
            if num > n:
                less_count += num - n
        return less_count
        
```

```cpp
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
```