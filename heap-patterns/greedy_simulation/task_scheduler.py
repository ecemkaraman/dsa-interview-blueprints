# 🔢 LC 621 – Task Scheduler
# ✅ Pattern: Greedy Simulation
# 📂 Template: Max-Heap of frequencies + cooldown queue
# 🧠 Tip: Greedy choose most frequent task

from collections import Counter, deque
import heapq

def leastInterval(tasks, n):
    freq = Counter(tasks)
    max_heap = [-f for f in freq.values()]
    heapq.heapify(max_heap)
    cooldown = deque()
    time = 0

    while max_heap or cooldown:
        time += 1
        if max_heap:
            task = heapq.heappop(max_heap) + 1  # Do task (increase since neg)
            if task:
                cooldown.append((task, time + n))

        if cooldown and cooldown[0][1] == time:
            heapq.heappush(max_heap, cooldown.popleft()[0])

    return time

# 🔁 Variants:
# - Variable cooldown
# - Return task schedule instead of just time
