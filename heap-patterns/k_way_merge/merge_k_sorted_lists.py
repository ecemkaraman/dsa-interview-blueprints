# 🔢 LC 23 – Merge K Sorted Lists
# ✅ Pattern: K-Way Merge
# 📂 Template: Min-Heap of (val, list_idx, node)
# 🧠 Tip: Push next from the list the node came from

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

def mergeKLists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode(0)
    curr = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next

# 🔁 Variants:
# - Merge arrays instead of linked lists
# - Smallest k sum pairs (LC 373)
