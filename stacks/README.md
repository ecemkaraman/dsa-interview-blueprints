## **🧠 Stack Strategy**
```python
Stack Problem
├── I. Stack Type (Stack Lens)
│   ├── Single Stack (LIFO logic: reverse, undo, scope)
│   ├── Monotonic Stack (incr/decr order for min/max)
│   ├── Two Stacks (min stack, eval stack, undo/redo)
│   ├── Indexed Stack (store (val, idx) for span/area)
│   └── Stack + Extra DS (set, map, list → decode/track)

├── II. Input Type (Parse Layer)
│   ├── String of brackets/ops → validity/canonical form
│   ├── List[int] → next greater/warmer span
│   ├── Expression (infix/postfix) → eval/convert
│   ├── Encoded string → decode nested patterns
│   └── Matrix/Histogram → largest rectangle

├── III. Algorithm Toolbox (Stack Engine)
│   ├── Basic Stack → LIFO logic (reverse, undo, nesting)
│   ├── Monotonic Stack → NGE/NSE, min/max window, span
│   ├── Stack + Index → area calc, window bounds
│   ├── Stack + Counter → balance open/close (greedy)
│   ├── Stack + Recursion → decode nested/DFS calls
│   ├── Two Stacks → simulate queue / support rollback
│   └── Stack + Heap → simulate eval w/ priority

└── IV. Pattern → Algorithm Mapping (Problem Intent)
    ├── Validity / Canonicalization
    │     ├── “valid parentheses / min remove”
    │     └── Stack + count or index track (greedy cleanup)
    ├── Decode / Expand
    │     ├── “decode 3[a2[c]]”
    │     └── Stack of (count, string) + build from inside out
    ├── Infix/Postfix Eval
    │     ├── “reverse polish / math eval”
    │     └── Stack for numbers/ops + process precedence
    ├── Monotonic Pattern
    │     ├── “next greater / smaller / daily temps”
    │     └── Monotonic stack (decreasing for NGE)
    ├── Histogram / Area
    │     ├── “largest rectangle / max area”
    │     └── Stack + index for left/right bound expansion
    ├── Remove Adjacent / Collapse
    │     ├── “remove duplicates / simplify path”
    │     └── Stack + compare with top (same char/path segment)
    ├── Balance / Match
    │     ├── “longest valid parens / check nesting”
    │     └── Stack + index OR count for max span
    ├── Backspace / Undo
    │     ├── “compare after backspace”
    │     └── Stack to simulate edits
    ├── Queue Simulation
    │     ├── “implement queue using stacks”
    │     └── Two stacks (in, out) for FIFO behavior
    └── Traversal / Recursion Simulation
          ├── “simulate recursion / call stack / DFS iter”
          └── Manual stack for iterative traversal or eval

```