# Inorder Traversal

## Related Problems

- [230. Kth Smallest Element in a BST](../LeetCode/Problems/230.Kth-Smallest-Element-in-a-BST/README.md)
  - https://leetcode.com/problems/kth-smallest-element-in-a-bst/
- [897. Increasing Order Search Tree](../LeetCode/Problems/897.Increasing-Order-Search-Tree/README.md)
  - https://leetcode.com/problems/increasing-order-search-tree/solution/


In binary search tree problems (kind of sorted), many problems can be solved with in-order traversal just like iterating through a regular sorted array.

For example, for [230. Kth Smallest Element in a BST](../LeetCode/Problems/230.Kth-Smallest-Element-in-a-BST/README.md), suppose you are to select the Kth smallest element in a sorted array, you just need to iterate through the array (suppose you cannot use index). BST is pretty much equivalent to a sorted array, except that it cannot use index. So just do a in-order traversal to simulate the sorted array iteration.