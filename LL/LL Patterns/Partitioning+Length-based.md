### 6. 📏 **Partitioning / Length-Based Logic**

**Count length**

```python
def getLength(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count
```

**Split into k parts**

```python
def splitListToParts(head, k):
    length = getLength(head)
    part_len, extra = divmod(length, k)
    out = []
    curr = head
    for _ in range(k):
        dummy = write = ListNode(0)
        for _ in range(part_len + (extra > 0)):
            write.next = ListNode(curr.val)
            write = write.next
            if curr: curr = curr.next
        extra -= 1
        out.append(dummy.next)
    return out
```

---

**Partition Around Value**

```python
def partition(head, x):
    before = before_head = ListNode(0)
    after = after_head = ListNode(0)
    while head:
        if head.val < x:
            before.next, before = head, head
        else:
            after.next, after = head, head
        head = head.next
    after.next = None
    before.next = after_head.next
    return before_head.next
```

---

**Convert LL → Array**

```python
def linked_list_to_array(head):
    arr, curr = [], head
    while curr:
        arr.append(curr.val)
        curr = curr.next
    return arr
```
