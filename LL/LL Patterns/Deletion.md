### 5. 🧼 **🗑️ Deletion Patterns**

**Delete N-th Node from End**

- 🧷 Create **`dummy** → head` → enables uniform deletion incl. head
- ⚙️ Init `first = second = dummy` → move `first` `n+1` steps (gap = `n`)
- 🔁 While `first`: move both → when `first = None`(end), `second.next = target`
- ❌ Delete target: `second.next = second.next.next` (skips target)
- 🔚 Return `dummy.next` → always valid head, handles head deletion (`n = len(LL)`) edge case

```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first, second = dummy, dummy
    for _ in range(n + 1): # Move first n+1 steps (gap=n)
        first = first.next
    while first: 
        first = first.next # Move both pointers until first reaches None(end)
        second = second.next
    second.next = second.next.next
    return dummy.next  # Head of the modified list
```

---

❌ **Delete node by value**: Use `dummy → head`, track `prev` and `curr`; if `curr.val == target`, remove by `prev.next = curr.next`, else move both forward. Return `dummy.next`.

```python
def delete_node(head, val):
    dummy = ListNode(0)    
    dummy.next = head
    prev, curr = dummy, head

    while curr:
        if curr.val == val:
            prev.next = curr.next  # ❌ Skip target node
            break                  # ✅ Only first match removed
        prev, curr = curr, curr.next

    return dummy.next              # 🔚 Return new head
```

---

**Remove Duplicates from a Sorted LL** (`LC 83`)

**🧠 Key Idea:** Since the list is **sorted**, duplicates will be **adjacent**. If `curr.val == curr.next.val` → skip the next node (duplicate)

```python
def delete_duplicates(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next  # ❌ Skip duplicate node
        else:
            curr = curr.next            # ✅ Move to next node if unique
    return head  # 🔚 In-place modification
```
