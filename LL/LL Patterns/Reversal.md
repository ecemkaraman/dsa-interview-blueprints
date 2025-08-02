### 2. 🔁 **Reversal (Full / Partial)**

**Reverse Entire LL (Iterative)** → use `prev`, `curr`, `nxt` to rewire pointers: preserve `curr.next` with `nxt`, point `curr.next` to `prev`, shift all forward.

```python
def reverse(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next       # 🧠 store next node
        curr.next = prev      # 🔄 reverse the pointer
        prev = curr           # 📍 move prev forward
        curr = nxt            # 📍 move curr forward
    return prev               # 🔚 new head
```

- 🪞 `prev` → holds the **previous node** to rewire `curr.next → prev`
- 🧭 `curr` → active pointer traversing the original list
- 🧷 `nxt` → temp holder to **preserve** `curr.next` before overwriting it
- 🔁 UC: Iterate backward in singly LL (no extra space): Reverse list → apply logic → reverse again to restore.

---

**Reverse Entire LL (Recursive) - (optional)**

```python
def reverse(head):
    if not head or not head.next:
        return head  # base case: empty or 1 node → return as is

    new_head = reverse(head.next)  # 🔽 Recurse to tail (=head.next)
    head.next.next = head  # 🔁 Reverse the link: tail.next = head
    head.next = None    # 🧹 Break old forward link

    return new_head   # ⬆️ Return new head (tail of original list)
```

🔁 **Recursive Descent**: Recurse on `head.next` until base case (last node) is reached. At deepest call → `head.next = tail` (**tail** becomes `new_head`). Reverse links & return `new_head` up stack 

---

**🔁 Reverse Between [m, n] (LC 92 - Reverse LL II)**

```python
def reverseBetween(head, m, n):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Step 1: Move prev m-1 steps (pre-reversal node)
    for _ in range(m - 1):
        prev = prev.next

    # Step 2: Init pointers for reversal
    start = prev.next         # m-th node, first node to reverse
    then = start.next         # (m+1)th node, next to reverse, insert after prev

    # Step 3: Reverse next (n - m) nodes
    for _ in range(n - m):
        start.next = then.next # skip then
        then.next = prev.next # insert then after prev
        prev.next = then # update head of reversed portion
        then = start.next # move to next node to reverse

    return dummy.next # updated head
```

---

 **🔁 **Reverse in k-Group (LC 25)**

- 🧷 Init `dummy → head`, `group_prev = dummy` → start reversal after dummy
- 🔍 **Find `kth` node** (reversal boundary): move `kth = group_prev` ahead `k` times
- 🎯 **Pointers**:
    - `group_prev`: end of the last reversed group
    - `group_next = kth.next` → node after current k-group
    - `prev = group_next`, `curr = group_prev.next` → for in-place reversal

```python
def reverseKGroup(head, k):
    dummy = ListNode(0)
    dummy.next = head
    group_prev = dummy

    while True:
        # Step 1: Find the kth node
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if not kth: # Not enough nodes left -> early exit
                **return dummy.next** # Updated head

        # Step 2: Define pointers
        group_next = kth.next
        prev, curr = group_next, group_prev.next

        # Step 3: Reverse k nodes
        for _ in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # Step 4: Connect previous group to reversed group
        tmp = group_prev.next # start of current group
        group_prev.next = kth # new group head
        group_prev = tmp # move prev for next round
```
