```python
├── I. Tree Type (Tree Lens)
│   ├── Binary Tree → at most 2 children (left, right)
│   ├── BST → ordered: left < root < right
│   ├── N-ary Tree (>2 children) → general tree structure
│   ├── Balanced / Full / Complete → structural constraints
│   └── Binary Heap (Min/Max) → often implicit in arrays (heapify ops)

├── II. Input Format (Parse Layer)
│   ├── 📌 Node Class (val, left, right) → traverse directly
│   ├── 📌 Level-Order Array → reconstruct tree using queue
│   ├── 📌 Preorder/Inorder/Postorder List → reconstruct tree
│   ├── 📌 Parent Map / ID Links → reverse build (child→parent)
│   └── 📌 Serialized String → deserialize before solving

├── III. Algorithm Toolbox (Tree Engine)
│   ├── 🔁 DFS (Recursive) → depth, path, bottom-up (postorder)
│   ├── 🔁 DFS (Iterative) → controlled traversal (stack)(pre/in/post)
│   ├── 🔁 BFS → level-order, width, shortest depth, queues
│   ├── 🪢 Inorder / Preorder / Postorder → specific ordering problems
│   └── ⚙️ Tree Rebuilding / Decomposition → reconstruction from traversals
│   └── 📚 Two Pointers / Morris Traversal → O(1) space traversal

└── IV. Pattern → Algorithm Mapping (Problem Intent)
    ├── 🧭 Traversals
    │     └── Pre/In/Post → DFS; Level Order → BFS
    ├── 📏 Depth / Height / Diameter
    │     └── DFS → bottom-up height or pair return
    ├── 🔗 Path Sum / Max Gain
    │     └── DFS + backtracking or accumulate values
    ├── 🧬 Subtree / LCA / Ancestor
    │     └── DFS + match target values or parent maps
    ├── 🔄 Symmetry / Balanced Check
    │     └── DFS → compare left vs right / height diff ≤ 1
    ├── 🧪 Validation (isBST, isSameTree)
    │     └── DFS + bounds (for BST) / node comparison
    ├── 🔃 Reconstruct Tree
    │     └── Pre + In / Post + In → recursive splitting
    ├── 🎯 Tree Modification
    │     └── Use: DFS (recursively rewrite), BFS (level pruning)
    ├── 📊 Width / Zigzag Level Order
    │     └──  BFS w/ level tracking or deque
    ├── 🧬 LCA / Subtree / Ancestors
    │     └── Use: DFS + backtracking or parent map 
```

---

## 🌳 **Tree Execution Strategy (4→1→2→3)**

🧠 **Pattern → Algorithm → Input Format → Code Template**

- 💡 Start with **Pattern** (depth? path? subtree? symmetry?)
- 🔎 Identify **Tree Type** (Binary? BST? N-ary? Complete?)
- 🧾 Parse **Input Format** (Node class? Array? Traversals?)
- 🔧 Choose **Algorithm** (DFS/BFS/Recurse/Rebuild) → Plug into **template**

---

## 🧠 **Tree Problem Strategy: Step-by-Step Mental Flow**

### 🟢 1. **Clarify the Ask**

- ❓ What’s being asked? → `Depth? Path sum? LCA? Rebuild?`
- 🎯 Output type? → `Bool / Count / Path / Node / Tree`

---

### 🟡 2. **Identify Tree Type**

- 🌲 Binary Tree → up to 2 children
- 🧮 BST → left < root < right (ordered)
- 🌿 N-ary → variable # of children
- 🧱 Complete / Full / Balanced → structure matters
- 🔄 Heap (Min/Max) → array-based; use heapify

---

### 🟠 3. **Understand Input Format**

- 🧩 `TreeNode(val, left, right)` → Traverse directly
- 📊 Level-order Array → Rebuild using queue (child index math)
- 🧾 Traversals (pre/in/post) → Use for reconstruction
- 🧬 Parent-child ID links → Reverse map (build tree from bottom)
- 🔐 Serialized String → Use `deserialize()` parser

---

### 🔴 4. Detect Pattern & Choose Algorithm

- 🔁 **Traversal** → Pre/In/Post (DFS), Level-order (BFS)
- 📏 **Depth / Height / Diameter** → DFS bottom-up
- 🔗 **Path Sum / Max Gain** → DFS with carry + backtrack
- 🧬 **Subtree / Ancestor (LCA)** → DFS w/ match or recursion rules
- 🔄 **Symmetry / Balance Check** → DFS: compare mirror nodes / heights
- ✅ **Validation (BST / Equal Trees)** → DFS + bounds / value match
- 🛠 **Reconstruct Tree** → Pre+In / Post+In split recursive
- 🔁 **Invert / Modify Tree** → DFS or BFS relink
- 📏 **Width / Zigzag Order** → BFS with level tracking / deque

---

### ⚪ 5. Code Template Setup

- 🔁 DFS → recursive / stack
- ⏫ BFS → queue
- 🧠 Carry values or return tuple if path needs aggregates
- 🧱 Use helper functions for depth/path/gain

---

## 🧠 **Summary Mental Model (Top-Down)**

```
1. What’s the ask? → Depth? Path? Node? Tree?
2. What type of tree? → Binary / BST / N-ary?
3. What’s the input format? → TreeNode? Array? Traversals?
4. Pick pattern → DFS/BFS/Rebuild/Subtree logic
5. Choose template → Carry, backtrack, return struct
6. Handle base case(s) → null, leaves, one-node
7. Dry run → Validate w/ small input

```

---

### 🎯 **Key Insight**

> Don’t force a traversal — let the problem pattern + input format drive your algorithm.
> 
> 
> Build muscle memory for:
> 
> - **DFS return variants**: count, bool, tuple, node
> - **Path logic**: backtrack or pass down
> - **Tree building**: recursion split logic (Pre/In, Post/In)