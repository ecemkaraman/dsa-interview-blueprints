# LL Patterns - Core Categories

### 1. **🐢🐇 Two-Pointer Techniques**

- `slow, fast = head, head`
- **Cycle detect** → `slow == fast ⇒ cycle`
- **Cycle entry** → reset one pointer to head after meeting, move both 1-step until equal
- **Middle node** → `fast moves 2x ⇒ slow at mid`
- **Nth from end** → `fast ahead n+1 ⇒ slow at node before target`
- **Palindrome check** → `find mid → reverse 2nd half → compare halves`
- **Intersection node** → `a=headA, b=headB → switch heads on end ⇒ meet or None`
<details>
- **🌀 Detect cycle:** Use `slow`, `fast` (2x speed); if they meet (`fast == slow`)  → cycle exists, else `fast` hits `None`.
- **🚪 Find cycle entry:** After meeting inside loop, reset `slow = head` → move both 1 step → meeting point = cycle start.
- **🧭 Find middle of LL:** Use `fast = 2x slow`; when `fast` ends → `slow = mid` (📎 even → 2nd mid, 📎 odd → exact mid).
</details>
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
