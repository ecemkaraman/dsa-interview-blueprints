# 🔢 LC 295 – Find Median from Data Stream
# ✅ Pattern: Two Heaps
# 📂 Template: Max-Heap for left, Min-Heap for right
# 🧠 Tip: Keep left heap (negated) ≤ right heap in size

class MedianFinder:
    def __init__(self):
        self.left = []   # Max-heap (invert values)
        self.right = []  # Min-heap

    def addNum(self, num):
        heapq.heappush(self.left, -num)
        heapq.heappush(self.right, -heapq.heappop(self.left))
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self):
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2

# 🔁 Variants:
# - Return mode, mean, median in stream
# - Apply for sliding window median
