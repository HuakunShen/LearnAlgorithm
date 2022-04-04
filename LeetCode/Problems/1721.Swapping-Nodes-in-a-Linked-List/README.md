# 1721. Swapping Nodes in a Linked List

## Solution

### Solution 1 O(n)

Without modifying node value.

```python
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count, cur = 0, head
        while cur is not None:
            count += 1
            cur = cur.next
        p2_pos = count - k + 1
        if k == p2_pos:
            return head
        if k > p2_pos:
            return self.swapNodes(head, p2_pos)
        i, cur, p1, p1_prev, p2, p2_prev = 0, head, None, None, None, None
        p2_pos = count - k + 1
        while cur is not None:
            if i + 2 == k and k != 1:
                p1_prev = cur
            if i + 2 == p2_pos:
                p2_prev = cur
            i += 1
            if i == k:
                p1 = cur
            if i == p2_pos:
                p2 = cur
            cur = cur.next
        p1_next = p1.next
        if p1_prev:
            p1_prev.next = p2
        p1.next = p2.next
        if p2_prev and p2_prev != p1:
            p2_prev.next = p1
        if p1_next != p2:
            p2.next = p1_next
        else:
            # initial: p1 -> p2
            p2.next = p1
        return p2 if k == 1 else head
        
```

## Solution 2 O(n)

Modify node value directly.

```python
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count, cur = 0, head
        while cur is not None:
            count += 1
            cur = cur.next
        p2_pos = count - k + 1
        count, cur = 0, head
        while cur is not None:
            count += 1
            if count == k:
                p1 = cur
            if count == p2_pos:
                p2 = cur
            cur = cur.next
        p1.val, p2.val = p2.val, p1.val
        return head
```

## Test Cases

```
[1,2,3,4,5]
2
[1]
1
[1,2]
1
[1,2]
2
```