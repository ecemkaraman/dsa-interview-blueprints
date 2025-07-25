## **🧠 Heap Patterns**

### 🧭 Step 1: Recognize Heap Need

> “Do I need to frequently access min/max/top-k with efficient updates?”
> 

If **yes** → It’s a **heap pattern problem**

---

| Cluster | Trigger Keywords | Template Type | Example Problems |
| --- | --- | --- | --- |
| [**Ranking**](https://github.com/ecemkaraman/dsa-interview-blueprints/tree/main/heap-patterns/kth_ranking) | kth largest, smallest | Min-heap (size `k`) | [LC 215](https://leetcode.com/problems/kth-largest-element-in-an-array/), [LC 703](https://leetcode.com/problems/kth-largest-element-in-a-stream/) |
| [**Top-K Elements**](https://github.com/ecemkaraman/dsa-interview-blueprints/tree/main/heap-patterns/top_k_elements) | top-k, most frequent, closest | Min/max-heap (size `k`) | [LC 347](https://leetcode.com/problems/top-k-frequent-elements/), [LC 973](https://leetcode.com/problems/k-closest-points-to-origin/), [LC 692](https://leetcode.com/problems/top-k-frequent-words/) |
| [**Frequency**](https://github.com/ecemkaraman/dsa-interview-blueprints/tree/main/heap-patterns/frequency) | frequent elements, count, score | HashMap + heap | [LC 347](https://leetcode.com/problems/top-k-frequent-elements/), [LC 451](https://leetcode.com/problems/sort-characters-by-frequency/) |
| [**Proximity**](https://github.com/ecemkaraman/dsa-interview-blueprints/tree/main/heap-patterns/top_k_elements/k_closest_points.py) | closest/farthest, distance, near origin | Max-heap with comparator | [LC 973](https://leetcode.com/problems/k-closest-points-to-origin/), [LC 658](https://leetcode.com/problems/find-k-closest-elements/) |
| [**Streaming**](https://github.com/ecemkaraman/dsa-interview-blueprints/tree/main/heap-patterns/streaming) | incoming values, maintain k, real-time | Class + heap | [LC 703](https://leetcode.com/problems/kth-largest-element-in-a-stream/), [LC 295](https://leetcode.com/problems/find-median-from-data-stream/) |
| [**K-Way Merge**](https://github.com/ecemkaraman/dsa-interview-blueprints/tree/main/heap-patterns/k_way_merge) | merge k lists, sorted arrays | Min-heap of `(val, src)` | [LC 23](https://leetcode.com/problems/merge-k-sorted-lists/), [LC 373](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) |
| [**Two Heaps**](https://github.com/ecemkaraman/dsa-interview-blueprints/tree/main/heap-patterns/two_heaps) | find median, balanced halves | Max-heap + min-heap | [LC 295](https://leetcode.com/problems/find-median-from-data-stream/) |
| [**Greedy Simulation**](https://github.com/ecemkaraman/dsa-interview-blueprints/tree/main/heap-patterns/greedy_simulation) | simulate, rearrange, cooldown, max first | Max-heap + custom logic | [LC 1046](https://leetcode.com/problems/last-stone-weight/), [LC 621](https://leetcode.com/problems/task-scheduler/), [LC 358](https://leetcode.com/problems/rearrange-string-k-distance-apart/) |
---

### 🧩 Step 3: Plug the Right Template

| Goal | Template Description |
| --- | --- |
| [**Top-K Elements**](https://github.com/ecemkaraman/dsa-interview-blueprints/blob/main/heap-patterns/top_k_elements/top_k_frequent_elements.py) | Min-heap (size `k`), push + pop |
| [**K-th Largest**](https://github.com/ecemkaraman/dsa-interview-blueprints/blob/main/heap-patterns/kth_ranking/kth_largest_min_heap.py) | Heapify first `k`, then pushpop |
| [**Frequency-Based Ranking**](https://github.com/ecemkaraman/dsa-interview-blueprints/blob/main/heap-patterns/frequency/sort_char_by_freq.py) | HashMap + heap of `(-freq, val)` |
| [**Merge K Sorted Lists**](https://github.com/ecemkaraman/dsa-interview-blueprints/blob/main/heap-patterns/k_way_merge/merge_k_sorted_lists.py) | Min-heap of `(val, list_idx, val_idx)` |
| [**Streaming K-th Largest**](https://github.com/ecemkaraman/dsa-interview-blueprints/blob/main/heap-patterns/streaming/kth_largest_stream_class.py) | Class with min-heap + `add()` method |
| [**Median in Stream**](https://github.com/ecemkaraman/dsa-interview-blueprints/blob/main/heap-patterns/two_heaps/median_finder.py) | Two heaps: max-heap left, min-heap right |
| [**Cooldown Simulation**](https://github.com/ecemkaraman/dsa-interview-blueprints/blob/main/heap-patterns/greedy_simulation/task_scheduler.py) | Max-heap + greedy intervals |
