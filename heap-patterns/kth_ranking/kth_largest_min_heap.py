# 🔢 LC 215 – Kth Largest Element in Array
# ✅ Pattern: Ranking
# 📂 Template: Min-Heap of size k
# 🧠 Tip: Heap top always keeps the k-th largest seen so far
# ⚠️ Trap: Don't sort entire array – keep heap to k elements
# 🔁 Variation: Kth smallest = Max-Heap of size k (negate nums)

import heapq

def findKthLargest(nums, k):
    heap = nums[:k]                        # Build heap from first k
    heapq.heapify(heap)                   # O(k)
    for num in nums[k:]:                  # Rest of elements
        if num > heap[0]:                 # Only pushpop if num is larger
            heapq.heappushpop(heap, num)
    return heap[0]                        # K-th largest = smallest in heap

# 🔁 Variants:
# - Find K-th smallest (invert signs or use max-heap pattern)
# - K-th largest in stream (convert to class)
