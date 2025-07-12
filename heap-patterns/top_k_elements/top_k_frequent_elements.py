# 🔢 LC 347 – Top K Frequent Elements
# ✅ Pattern: Frequency
# 📂 Template: HashMap + Min-Heap of size k
# 🧠 Tip: Push (freq, num) to min-heap → top holds least frequent of top-K

from collections import Counter

def topKFrequent(nums, k):
    freq_map = Counter(nums)                             # Count frequencies
    heap = []
    for num, freq in freq_map.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for (freq, num) in heap]

# 🔁 Variants:
# - Top K frequent words (lexicographic tie-breaker)
# - Bucket sort alternative for large n, small k
