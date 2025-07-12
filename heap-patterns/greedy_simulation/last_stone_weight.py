# 🔢 LC 1046 – Last Stone Weight
# ✅ Pattern: Greedy Simulation
# 📂 Template: Max-Heap via negation
# 🧠 Tip: Always smash 2 heaviest stones

import heapq

def lastStoneWeight(stones):
    max_heap = [-s for s in stones]   # Simulate max-heap
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        s1 = -heapq.heappop(max_heap)
        s2 = -heapq.heappop(max_heap)
        if s1 != s2:
            heapq.heappush(max_heap, -(s1 - s2))

    return -max_heap[0] if max_heap else 0

# 🔁 Variants:
# - Can be used for task pairings, weight balancing
