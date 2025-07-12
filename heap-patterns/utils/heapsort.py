# 🔧 Heapsort using Min-Heap
# ✅ Foundation Concept – Not commonly used in interviews directly
# 📂 Template: heapify input → repeatedly heappop to get sorted array
# 🧠 Tip: Heapsort gives O(n log n) time and is in-place (but not stable)

import heapq

def heapsort(nums):
    heapq.heapify(nums)                        # Convert list to min-heap in O(n)
    return [heapq.heappop(nums) for _ in range(len(nums))]  # Pop all elements

# 🔁 Variants:
# - Descending order → use max-heap via negation:
#     return sorted([-heapq.heappop(max_heap) for _ in range(len(max_heap))])
# - Replace heapq with custom heap for learning purpose
# - Often used as building block for understanding Top-K

# 🧪 Example:
# print(heapsort([5, 1, 4, 2, 3]))  # Output: [1, 2, 3, 4, 5]
