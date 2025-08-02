


## 1. 🐢🐇 **Two-Pointer Techniques**

  <details>
    <summary> "**Cycle Detection**:" </summary>

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
    

  </details>


    


---

- **Cycle Entry Point**
    
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

- **Find Middle Node**
    
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

- **Palindrome Check**
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
    

---

### 2. 🔁 **Reversal (Full / Partial)**

- **Reverse Entire LL (Iterative)**
    
    use `prev`, `curr`, `nxt` to rewire pointers: preserve `curr.next` with `nxt`, point `curr.next` to `prev`, shift all forward.
    
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

- **Reverse Entire LL (Recursive) - (optional)**
    
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

- **🔁 Reverse Between [m, n] (LC 92 - Reverse LL II)**
    
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

- ****🔁 **Reverse in k-Group (LC 25)**
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
    

---

### 3. ⚔️ **Merging / Sorting / Intersection**

- **Merge 2 Sorted LLs**
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

- **Merge Sort Linked List**
    
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

- **Find Intersection Node of Two LLs (LC 160)**
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

- **Add Two Numbers Represented by LLs** (LC 2)
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
    

---
