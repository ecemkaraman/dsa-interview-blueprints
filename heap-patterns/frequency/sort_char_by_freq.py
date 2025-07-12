# 🔢 LC 451 – Sort Characters by Frequency
# ✅ Pattern: Frequency
# 📂 Template: HashMap + Max-Heap
# 🧠 Tip: Frequency count → push (-freq, char) into max-heap
# 🔁 Variation: Bucket sort for linear time

from collections import Counter
import heapq

def frequencySort(s):
    freq = Counter(s)
    max_heap = [(-f, ch) for ch, f in freq.items()]
    heapq.heapify(max_heap)
    result = []
    while max_heap:
        f, ch = heapq.heappop(max_heap)
        result.append(ch * -f)
    return ''.join(result)

# 🔁 Variants:
# - Bucket sort approach (group by freq)
# - Return top K frequent characters
# - Custom sorting using tuples
