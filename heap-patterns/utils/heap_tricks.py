# ✅ Common Heap Patterns & Utilities in Python
# 🔧 Use to simulate max-heap, custom sort keys, or hybrid patterns

import heapq

# 🔼 Max-Heap Simulation using Negation
def push_max(heap, val):
    heapq.heappush(heap, -val)

def pop_max(heap):
    return -heapq.heappop(heap)

# 🔁 Build Max-Heap from list
def max_heapify(nums):
    heap = [-x for x in nums]
    heapq.heapify(heap)
    return heap

# 🧩 Push with custom priority (e.g., by frequency or distance)
def push_with_priority(heap, priority, item):
    heapq.heappush(heap, (priority, item))  # min-heap on priority

# 🧮 Use tuples for tie-breaking (e.g., lexicographic or index order)
# Example: (-freq, word) for max-heap sorted by freq, then lex

# 🔄 Extract k largest using heapq.nlargest (alternative to maintaining heap manually)
def top_k_largest(nums, k):
    return heapq.nlargest(k, nums)

# 🔁 Extract k smallest (uses heap internally)
def top_k_smallest(nums, k):
    return heapq.nsmallest(k, nums)

# 🧪 Sample usage
if __name__ == "__main__":
    heap = []
    for val in [3, 1, 5]:
        push_max(heap, val)
    print("Max pop:", pop_max(heap))  # Output: 5

    heap = max_heapify([4, 2, 7])
    print("Max heapified:", [-x for x in heap])  # Output: [7, 2, 4]
