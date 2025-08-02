## **🧠 Queue Strategy**
```python
Queue Problem
├── I. Queue Type (Queue Lens)
│   ├── simple / circular
│   ├── bounded / unbounded
│   ├── single / double-ended (deque)
│   ├── monotonic (inc/dec)
│   └── priority (min/max heap for PQ)

├── II. Input Type (Parse Layer)
│   ├── array-based queue → simulate with indices or collections.deque
│   ├── linked list queue → implement with Node pointers
│   ├── stream / real-time input → sliding window, first unique, moving avg
│   └── multiple queues → double-ended or multi-source BFS

├── III. Algorithm Toolbox (Queue Engine)
│   ├── BFS / Level-order traversal (graph/tree)
│   ├── Sliding window with deque (max/min in window)
│   ├── Monotonic queue (inc/dec for O(1) window extrema)
│   ├── Multi-source BFS (enqueue multiple starts)
│   ├── Queue with timestamp (rate limiter, recent counter)
│   └── PriorityQueue / Heap (min/max element retrieval)

└── IV. Pattern → Algorithm Mapping (Problem Intent)
    ├── Level-order Traversal
    │     ├── “BFS in tree/graph / shortest path unweighted”
    │     └── Use: Queue (FIFO)
    ├── Sliding Window
    │     ├── “max/min in window / first negative / moving avg”
    │     └── Use: Deque / Monotonic queue
    ├── Stream Processing
    │     ├── “first unique char / rate limiter / hit counter”
    │     └── Use: Queue + hash / timestamp logic
    ├── Multi-source Spread
    │     ├── “rotting oranges / walls & gates / spread infection”
    │     └── Use: Multi-source BFS
    ├── Top-K or Priority Retrieval
    │     ├── “kth largest / task scheduling / least freq”
    │     └── Use: PriorityQueue (heapq in Python)
    └── Simulation
          ├── “circular queue / recent requests / round robin”
          └── Use: Array index mod N / deque rotation

```