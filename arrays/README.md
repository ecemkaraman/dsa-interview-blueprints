## **🧠 Array Patterns**

```python
Array Problem
├── I. Array Type (Array Lens)
│   ├── 1D / 2D (Matrix)
│   ├── Sorted / Rotated / Partially sorted
│   ├── Fixed-size / Dynamic (sliding window potential)
│   └── Sparse / Dense (many zeros → use compression)

├── II. Input Type (Parse Layer)
│   ├── 📌 Raw Array → e.g., nums = [1,2,3,4]
│   ├── 📌 Multiple Arrays → merge, intersect, difference
│   ├── 📌 Stream Input → sliding window / prefix sums
│   └── 📌 2D Matrix → e.g., grid = [[1,0],[0,1]] 

├── III. Algorithm Toolbox (Array Engine)
│   ├── 🔁 Two Pointers → sorting, merging, in-place transform
│   ├── 🔁 Sliding Window (+ hashmap/counter)→ subarray length/sum/property
│   ├── 🧮 Prefix / Suffix Sum → range sum, subarray conditions
│   ├── 📊 HashMap / Counting → frequencies, indices, subarray checks
│   ├── 🔄 Binary Search → sorted / rotated arrays, search ranges
│   ├──⚡ Monotonic Stack / Deque → next greater/smaller element, window max
│   ├── 📈 Kadane’s Algo → Max subarray
│   ├── ⛏️ Heap / Quickselect → Top‑K / kth element
│   ├── 🧠 Greedy + Sweep Line → Intervals (starts/ends)
│   └── ➖ Difference Array → Range updates / interval ops (rarer)

└── IV. Pattern → Algorithm Mapping (Problem Intent)
    ├── 1) Subarray / Sum / Product
    │   • Max subarray → Kadane  
    │   • Subarray sum = k → Prefix sum + hashmap  
    │   • Subarray product < k → Sliding window
    ├── 2) Searching / Positioning
    │   • Rotated search / find min → Binary search variants  
    │   • First/last ≥/≤ target → Lower/upper bound
    ├── 3) K‑Sum Family
    │   • 2‑sum → Hashmap / Two pointers (sorted)  
    │   • 3‑sum / 4‑sum → Sort + two pointers (+ pruning)
    ├── 4) Intervals
    │   • Merge intervals → Sort by start, merge overlaps  
    │   • Non‑overlap / min removals → Sort by end, greedy keep  
    │   • Meeting rooms I/II → Starts/ends arrays or min‑heap of ends  
    │   • Min arrows (balloons) → Sort by end, greedy  
    │   • Intersection/union length, max overlap → Sweep line
    ├── 5) Top‑K / Selection
    │   • Kth largest/smallest → Quickselect or heap  
    │   • Top‑K frequent → Hashmap + heap / bucket  
    │   • K closest points → Heap / Quickselect
    ├── 6) Reorder / Partition / Dedupe
    │   • Remove duplicates (sorted) → Two pointers  
    │   • Dutch national flag (0/1/2) → 3‑way partition  
    │   • Cyclic sort (1..n) → Missing/duplicate
    └── 7) Matrix (2D Arrays)
        • Spiral / rotate / transpose → Simulation/in‑place  
        • 2D range sum → 2D prefix sums
```
