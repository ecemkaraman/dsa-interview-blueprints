### 3. ⚔️ **Merging / Sorting / Intersection**

**Merge 2 Sorted LLs** 

- 🧷 Init `dummy → head`, use `tail` to build
- 🔁 Compare `l1.val` & `l2.val` → attach smaller to `tail`, move `tail` & chosen list
- ⛳ When one ends → attach leftover: `tail.next = l1 or l2`
- 🔚 Return `dummy.next` (start of merged LL)

```python
def merge_two_lists(l1, l2):
    dummy = ListNode(0)           
    tail = dummy                  # tail tracks end of merged list

    while l1 and l2:              # 🔁 Traverse while both lists have nodes
        if l1.val < l2.val:      
            tail.next = l1       
            l1 = l1.next          
        else:                     
            tail.next = l2        
            l2 = l2.next          
        tail = tail.next          

    tail.next = l1 if l1 else l2  # 📌 Attach remaining nodes from non-empty list
    return dummy.next             # 🔚 Return merged list head 
```

---

**Merge Sort Linked List**

```python
def sortList(head):
    if not head or not head.next: return head

    slow, fast = head, head.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    mid, slow.next = slow.next, None

    left = sortList(head)
    right = sortList(mid)
    return mergeTwoLists(left, right)
```

---

**Find Intersection Node of Two LLs (LC 160)**

- 🎯 Init `a = headA`, `b = headB` (start one on each list)
- 🔁 Traverse → when `a` hits end → wrap to `headB`; when `b` hits end → wrap to `headA`
- 🔁 This syncs their path lengths → both traverse `lenA + lenB`
- ✅ They meet at intersection node (or `None` if no intersection)
- 📦 Return `a` (which equals `b` at intersection or both `None`)

```python
def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None

    a, b = headA, headB
    while a != b:
        a = a.next if a else headB  # 🔁 Switch to other head after reaching end
        b = b.next if b else headA
    return a  # 📍 Intersection node or None
```

---

**Add Two Numbers Represented by LLs** (LC 2)

- 🧷 Init `dummy → head`, `curr = dummy`, `carry = 0`
- 🔁 While `l1 or l2 or carry`:
    - 🔢 Get vals: `val1 = l1.val if l1 else 0`, `val2 = l2.val if l2 else 0`
    - ➕ Add & carry: `total = val1 + val2 + carry`, `carry = total // 10`
    - 🧮 Append digit: `curr.next = ListNode(total % 10)`
    - 👉 Move `l1`, `l2`, `curr` forward
- 📦 Return `dummy.next` (result head)

```python
def addTwoNumbers(l1, l2):
    dummy = ListNode(0)       # 🧷 Dummy node to build result
    curr = dummy              # Pointer to construct result list
    carry = 0                 # ➕ Carry from sum > 10

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0  # Get l1's digit or 0
        val2 = l2.val if l2 else 0  # Get l2's digit or 0

        total = val1 + val2 + carry  # Total sum
        carry = total // 10          # Update carry for next digit

        curr.next = ListNode(total % 10)  # 🧮 Create node with digit
        curr = curr.next                  # Move forward in result

        if l1: l1 = l1.next       # Advance l1 if exists
        if l2: l2 = l2.next       # Advance l2 if exists

    return dummy.next            # 📦 Return result LL head
```
