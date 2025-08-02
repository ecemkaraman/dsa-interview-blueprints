# 🔢 LC 358 – Rearrange String k Distance Apart
# ✅ Pattern: Greedy Simulation
# 📂 Template: Max-Heap of frequencies + cooldown queue
# 🧠 Tip: Always place most frequent character not on cooldown
# ⚠️ Trap: Fails if not all characters can be spaced out → return ""

from collections import Counter, deque
import heapq

def rearrangeString(s, k):
    if k == 0:
        return s

    freq = Counter(s)
    max_heap = [(-f, ch) for ch, f in freq.items()]  # Max-heap by freq
    heapq.heapify(max_heap)
    cooldown = deque()  # (freq, ch, ready_time)
    result = []
    time = 0

    while max_heap or cooldown:
        time += 1
        if max_heap:
            f, ch = heapq.heappop(max_heap)
            result.append(ch)
            if -f > 1:
                cooldown.append((f + 1, ch, time + k))  # reduce freq

        if cooldown and cooldown[0][2] == time:
            heapq.heappush(max_heap, (cooldown[0][0], cooldown[0][1]))
            cooldown.popleft()

    return "".join(result) if len(result) == len(s) else ""

# 🔁 Variants:
# - LC 621 (Task Scheduler)
# - Custom k-distance constraints for reordering
