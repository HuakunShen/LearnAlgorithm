from typing import List
import numpy as np


class Solution0:
    """
    Numpy Version
    """
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp_table = np.zeros((m + 1, n + 1)).astype(int)
        for s in strs:
            num_zeros = s.count("0")
            num_ones = len(s) - num_zeros
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i >= num_zeros and j >= num_ones:
                        dp_table[i, j] = max(dp_table[i - num_zeros, j - num_ones] + 1, dp_table[i, j])
        print(dp_table)
        return dp_table[m, n]


class Solution1:
    """
    Regular List Version
    """
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp_table = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            num_zeros = s.count("0")
            num_ones = len(s) - num_zeros
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i >= num_zeros and j >= num_ones:
                        dp_table[i][j] = max(dp_table[i - num_zeros][j - num_ones] + 1, dp_table[i][j])
        return dp_table[m][n]


if __name__ == '__main__':
    strs = ["10", "0001", "111001", "1", "0"]
    m, n = 5, 3
    sol = Solution0()
    print(sol.findMaxForm(strs, m, n))
