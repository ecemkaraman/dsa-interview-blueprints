### 1. 🐢🐇 **Two-Pointer Techniques**

**Cycle Detection**:

`fast = 2x slow` → if they meet(`fast == slow`) → **cycle exists**

- no cycle: `fast` reaches `None`
- detect point: `fast` & `slow` meet inside the loop

```python
def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True  # Cycle detected
    return False  # No cycle
```

---

**Cycle Entry Point**

After `fast == slow` → reset `slow = head` → move `slow` & `fast` 1 step each → where they meet = **entry point → • logic: distance from head to entry = distance from meeting point to entry**

```python
def find_cycle_entry_point(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            **break** #Exit loop immediately (stop everything inside the loop)
    else:
        return None  # 🔴 No cycle

    # Step 2: Find entry point
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow  # 🟢 Start of cycle
```

🔚 `break` → **Exit loop** immediately (stop everything inside the loop).

🔄 `while ... else`→ Runs **only** if `while` ended *without hitting `break`*

---

**Find Middle Node**

🐢🐇 `fast = 2x slow` → end reached → `slow = mid`

→ If `LL = even` → when `fast = None` → `slow = 2nd mid`

→ If `LL = odd`  → when `fast.next = None` → `slow = mid`

```python
def middleNode(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

---

**Palindrome Check**

- 🧭 **Find midpoint**: Use fast/slow → when `fast` ends, `slow` = mid
- 🔁 **Reverse 2nd half**: From `slow` to end → `prev` becomes new head of reversed half
- 🆚 **Compare** halves: Traverse both from `head` and `prev`, check `.val`
- ✅ Return `True` if all values match, else `False`

```python
def isPalindrome(head):
    # Step 1: Find middle (slow ends at midpoint)
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse second half
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    # Step 3: Compare both halves
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
```
