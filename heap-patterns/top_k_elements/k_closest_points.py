# 🔢 LC 973 – K Closest Points to Origin
# ✅ Pattern: Proximity
# 📂 Template: Max-Heap of size k using -distance²
# 🧠 Tip: Use -dist² to simulate max-heap


def kClosest(points, k):
    max_heap = []
    for x, y in points:
        dist = -(x*x + y*y)
        heapq.heappush(max_heap, (dist, [x, y]))
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return [point for (dist, point) in max_heap]

# 🔁 Variants:
# - Return sorted by distance
# - Handle tie-breaking or weights
