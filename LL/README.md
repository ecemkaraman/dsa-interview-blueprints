## **🧠 LL Strategy**

```python
Linked List Problem
├── I. List Type (Linked List Lens)
│   ├── singly / doubly
│   ├── cyclic (a) / acyclic
│   ├── dummy head used? / sentinel pattern
│   ├── static length / unknown length
│   └── sorted / unsorted

├── II. Input Type (Parse Layer)
│   ├── head node (ListNode) → typical LC format
│   ├── array → convert to LL for operations
│   ├── multiple heads → merge / intersection / compare
│   └── linked list + int/k → rotate / skip / partition

├── III. Algorithm Toolbox (Linked List Engine)
│   ├── Two Pointers (fast/slow) → cycle detect, middle, nth from end
│   ├── Dummy / Sentinel node → simplifies insert/delete/reverse
│   ├── Reversal → iterative or recursive (full / k-group)
│   ├── Merge Technique → merge k-lists, sort list (merge sort)
│   ├── Split & Combine → reorder, rotate, partition
│   ├── Stack → palindrome check, reverse printing
│   ├── Hashing / Set → detect cycle, intersection (if O(1) mem not needed)
│   └── Recursion → natural for reverse or divide & conquer

└── IV. Pattern → Algorithm Mapping (Problem Intent)
    ├── Reverse List
    │     ├── “reverse all / reverse k-group / partial reverse”
    │     └── Iterative pointer swap or recursion
    ├── Cycle Detection / Start of Cycle
    │     ├── “loop exists? / find entry node”
    │     └── Floyd’s Tortoise & Hare (fast/slow)
    ├── Middle / Nth From End
    │     ├── “find mid / remove nth from end”
    │     └── Two pointers (fast/slow or offset)
    ├── Merge / Sort
    │     ├── “merge 2 / merge k / sort list”
    │     └── Merge technique + dummy node (merge sort for sort)
    ├── Partition / Reorder
    │     ├── “odd-even / reorder L0→Ln→L1→Ln-1… / partition by value”
    │     └── Split & stitch using dummy nodes
    ├── Palindrome Check
    │     ├── “is list palindrome?”
    │     └── Reverse second half + compare OR stack
    ├── Intersection / Cycle Detection by Hash
    │     ├── “do two lists intersect?”
    │     └── Hash visited nodes OR length alignment trick
    └── Rotation / Modification
          ├── “rotate k / delete nodes / insert nodes”
          └── Dummy head + modular pointer moves

```