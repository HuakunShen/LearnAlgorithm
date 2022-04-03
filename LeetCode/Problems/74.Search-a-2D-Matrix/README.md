# 74. Search a 2D Matrix

https://leetcode.com/problems/search-a-2d-matrix/

Level: Medium (I believe it's an Easy)

## Solution

The algorithm is super easy, go through every row, for each row check the first and last number.
If target is in range of current row, then break and search this row only.

Time and Space Complexity are O(n) and O(1) (ignoring input variables)

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                break
        return target in matrix[i]

```