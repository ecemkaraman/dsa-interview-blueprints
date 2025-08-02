# LL Patterns - Core Categories

### 1. **🐢🐇 Two-Pointer Techniques**

- `slow, fast = head, head`
- **Cycle detect** → `slow == fast ⇒ cycle`
- **Cycle entry** → reset one pointer to head after meeting, move both 1-step until equal
- **Middle node** → `fast moves 2x ⇒ slow at mid`
- **Nth from end** → `fast ahead n+1 ⇒ slow at node before target`
- **Palindrome check** → `find mid → reverse 2nd half → compare halves`
- **Intersection node** → `a=headA, b=headB → switch heads on end ⇒ meet or None`
  
---

### 2. **🔁 Reversal (Full / Partial)**

- **Full reversal** (iterative): `prev, curr = None, head` & `while curr: curr.next, prev, curr = prev, curr, curr.next`
- **Recursive reversal**: `new_head = reverse(curr.next) → curr.next.next = curr`
- **Reverse Between [m, n]** → locate bounds, reverse sublist in-place
- **Reverse in k-group** → validate block size → → reverse blocks of k; connect ends

---

### 3. **⚔️ Merging / Sorting**

- **Merge 2 sorted lists** → dummy + tail + 2-ptr comparison
- **Merge Sort LL** → recursive split by mid → merge sorted halves
- **Add Two Numbers** → dummy + carry logic → traverse both lists + remainder
- **Flatten Multilevel LL** → DFS/stack + stitching `.next`/`.child`

---

### 4. **🔄 Reordering & Swapping**

- **Reorder list** → `mid → reverse 2nd → merge zigzag`
- **Swap nodes (not values)** → 3-ptr relinking of node pairs
- **Pairwise swap** → dummy + loop: swap every 2 nodes
- **Odd-Even positioning** → split odd/even → reconnect

---

### 5. **🧼 Dummy Node / Sentinel**

- `dummy → head`, simplifies edge deletions
- Used in: delete node, insert at head, reverse partial lists
- Always return `dummy.next` for updated head
- Avoids special casing (e.g., deleting head, merging empty lists)

---

### 6. **🗑️ Deletion Patterns**

- **Delete N-th from end** → dummy + two-ptr (gap = n) → `second.next = second.next.next`
- **Delete node with value** → traverse + skip target by updating `prev.next`
- **Delete duplicates (sorted)** → `if curr.val == curr.next.val ⇒ skip`

---

### 7. **🔗 Intersection / Joining**

- **Find intersection** → two-ptr with head switch on end
- **Join k-parts** → divide length equally → slice with boundaries
- **Connect components** → check value adjacency or rewire pointers

---

### 8. **🔁 Recursive Patterns**

- Reverse, reorder, swap, flatten
- Clean for post-order changes
- Base case clarity + backtracking → often yields elegant solutions

---

### 9. **📏 Length‑Based Logic**

- Use for:
    - Splitting (e.g., k parts)
    - Finding midpoint (`len // 2`)
    - Validating reversals (e.g., k-group)

---

### 10. **🔪 Partitioning & Grouping**

- **Partition by value** → 2 dummies: less & greater, reconnect
- **Split into parts** → length-based slicing
- **Group by rules/index** → modular logic (e.g., reverse alt k nodes)

---

<aside>

- **🌀 Detect cycle:** Use `slow`, `fast` (2x speed); if they meet (`fast == slow`)  → cycle exists, else `fast` hits `None`.
- **🚪 Find cycle entry:** After meeting inside loop, reset `slow = head` → move both 1 step → meeting point = cycle start.
- **🧭 Find middle of LL:** Use `fast = 2x slow`; when `fast` ends → `slow = mid` (📎 even → 2nd mid, 📎 odd → exact mid).
- ❌ **Delete node by value**: Use `dummy → head`, track `prev` and `curr`; if `curr.val == target`, remove by `prev.next = curr.next`, else move both forward. Return `dummy.next`.
- 📍 **Delete N-th from End**: Create `dummy → head` → init `first = second = dummy` → move `first` ahead `n+1` steps (gap = `n`)→ traverse both until `first = None` (end) → now `second.next = target` → delete via `second.next = second.next.next` → return `dummy.next` (new head)
- 🔁 **Reverse full LL (iterative):** Use `prev`, `curr`, `nxt` to rewire links → shift all forward until `curr` is `None`.
- 🔁 **Reverse full LL (recursive):** Recurse to tail (`reverse(head.next)`), then reverse links on unwind → `head.next.next = head`, break with `head.next = None`, return new head from deepest call.
- ⚖️ **Merge 2 sorted LLs:** Init `dummy → head`, use `tail` to build → compare `l1.val` &  `l2.val`, attach smaller → move `tail` & chosen list → attach leftover list to end → return `dummy.next`.
- 🧹 **Remove duplicates in sorted LL:** Traverse with `curr`; if `curr.val == curr.next.val` → skip duplicate by `curr.next = curr.next.next`.
- 🔗 **Find intersection of 2 LLs:** Use 2 pointers (`a`, `b`); start on each LL → if `a != b` → move `a = a.next or headB`, `b = b.next or headA`→ they meet at intersection or `None`.
- ➕ **Add 2 numbers via LLs:** Traverse `l1`, `l2` + `carry`; append `(sum % 10)` to result, update `carry = sum // 10`.
- 🪞 **Check if LL is palindrome:** Find middle, reverse second half, compare both halves node by node.
- ✂️ **Split LL into k parts:** Count nodes, calculate part sizes, slice at calculated boundaries using pointer hops.

</aside>


