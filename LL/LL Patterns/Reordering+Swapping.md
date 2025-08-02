### 4. 🔄 **Reordering & Swapping**

**Reorder List**

```python
def reorderList(head):
    if not head: return

    # Find mid
    slow, fast = head, head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    # Reverse second half
    prev, curr = None, slow.next
    slow.next = None
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    # Merge halves
    first, second = head, prev
    while second:
        first.next, second.next, first, second = second, first.next, first.next, second.next
```

**Swap Nodes in Pairs**

```python
def swapPairs(head):
    dummy = ListNode(0, head)
    prev = dummy
    while head and head.next:
        first, second = head, head.next
        prev.next, first.next, second.next = second, second.next, first
        prev, head = first, first.next
    return dummy.next
```
