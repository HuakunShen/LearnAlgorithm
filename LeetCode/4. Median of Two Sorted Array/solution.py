from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        >>> sol = Solution()
        >>> sol.findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
        5.5
        >>> sol.findMedianSortedArrays([1, 3], [2])
        2.0
        >>> sol.findMedianSortedArrays([1, 3, 5], [])
        3.0
        """
        total_num = len(nums1) + len(nums2)
        i = 0
        j = 0
        new_sorted = []
        while i + j < total_num // 2 + 1 and i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                new_sorted.append(nums1[i])
                i += 1
            else:
                new_sorted.append((nums2[j]))
                j += 1

        while i + j < total_num // 2 + 1:
            # if this while loop is entered, either nums1 or nums2 should be done, due to previous while loop
            if i < len(nums1):
                new_sorted.append(nums1[i])
                i += 1
            if j < len(nums2):
                new_sorted.append(nums2[j])
                j += 1

        if total_num % 2 == 1:
            return float(new_sorted[total_num // 2])
        else:
            return float((new_sorted[total_num // 2] + new_sorted[total_num // 2 - 1]) / 2)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
