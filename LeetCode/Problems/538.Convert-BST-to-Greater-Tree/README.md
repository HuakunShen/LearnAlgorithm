# 538. Convert BST to Greater Tree

https://leetcode.com/problems/convert-bst-to-greater-tree/

Level: Medium

## Solution

My thinking process while tackling this problem is in the method docstring.

Given number of nodes = $N$

Time Complexity: $O(N)$
- One traversal

Space Complexity: $O(N)$
- No extra space used for storing tree
- Recursion takes $O(N)$ space. Each recursive call costs constant space.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        The left children will be updated based on accumulated values on the right children
        To make the algorithm more efficient, for the right subtree, we must use a bottom-up approach
        i.e. accumulate from leaves upwards using recursion
        On the contrary, the left subtree will need a top-down approach where the sum is passed down to the children.
        This will also be a recursion, but requires a helper function with an extra "acc" parameter
        The helper function can also be reused for the right subtree by setting "acc" param to 0
        """
        def update(root: Optional[TreeNode], acc: int):
            if root is None:
                # Base Case
                return 0
            else:
                # Recursive Step
                right_sum = update(root.right, acc)
                left_input = root.val + right_sum + acc
                left_sum = update(root.left, left_input)
                ret = root.val + left_sum + right_sum
                # print(f"root.val: {root.val}, acc: {acc}, left_sum: {left_sum}, right_sum: {right_sum}, ret: {ret}") # debug message
                root.val = left_input
                return ret
                
        update(root, 0)
        return root
```