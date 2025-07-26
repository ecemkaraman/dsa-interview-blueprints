```python
Graph Problem
├── I. Graph Type (Graph Lens)
│   ├── Directed? Cyclic? Weighted?
│   └── Grid? Dense? Connected?

├── II. Input Type (Parse Layer)
│   ├── 📌 Edge List → use directly for Union-Find, else build adj list
│   ├── 📌 Adjacency List → traversal-ready
│   ├── 📌 Adjacency Matrix → dense graphs or all-pairs path, DP style
│   └── 📌 Grid (2D Matrix) → Treat as graph -Islands, maze, flood fill

├── III. Algorithm Toolbox (Graph Engine)
│   ├── 🔁 BFS → shortest path (unweighted), level-order, reachability
│   ├── 🔁 DFS (r&i) → components, cycles, topo (post-order)
│   ├── 🪢 Union-Find → dynamic connectivity/merging, disjoint sets
│   ├── 📍 Dijkstra → weighted shortest path (≥0), Min-heap priority queue
│   └── 📚 Topo Sort → Scheduling, DAGs, dependencies
						└── DFS-based(post-order reverse), BFS-based (Kahn’s w/ in-degree)

└── IV. Pattern → Algorithm Mapping (Problem Intent)
    ├── 🔗 Connected Components
    │     ├── “how many groups?”, “fully connected?”
    │     └── Use: DFS / BFS / Union-Find
    ├── 🔁 Cycle Detection
    │     ├── “loop?”, “valid tree?”
    │     └── Use: DFS (with parent/ rec stack), Union-Find
    ├── 🧭 Pathfinding
    │     ├── “shortest path”, “reach B from A”
    │     └── Use: BFS (unweighted) / Dijkstra (weighted)
    ├── 🗓 Scheduling / Dependencies
    │     ├── “can finish all tasks?”, “build order”
    │     └── Use: Topological Sort (DFS or BFS-based)
    └── 🌊 Grid Traversal / Flood Fill
          ├── “islands”, “regions”, “fill area”, "walls and gates"
          └── Use: BFS / DFS over grid (2D matrix)
```

Execution Strategy (4→1→2→3)

🧠 **Pattern → Algorithm → Input format → Code template**

- 💡 **Start with Pattern (what is being asked?)**
- 🔎 **Check Graph Type (directed, weighted?)**
- 🧾 **Parse Input (edge list? grid?)** → build Adjacency List unless using Union-Find, Build a reusable `build_graph()` helper for edge list → adj list
- 🔧 **Choose Algorithm (DFS/BFS/UF/Topo/Dijkstra) →** Know both **template** + **when to use**
- 🧪 **Plug into Template (code)**

---

# 🧠 **Graph Problem Strategy: Step-by-Step Mental Flow**

### 🟢 1. **Clarify the Problem/Ask**

- ❓ What’s being asked? → `Path? Shortest path? # of components? Cycle?`
- 🎯 What’s the output? → `Bool / Count / Path / Order`

---

### 🟡 2. Identify the **Graph Type**

- 🌳 **Tree** → Acyclic, connected, `n-1` edges → usually **no visited needed**
- 🕸 **General Graph** → May be cyclic/disconnected → **need visited / special handling**
- 🧱 **Grid** → Implicit graph (cells = nodes, neighbors = directions) → **manual neighbor calc**
    
    → Use DFS/BFS with bounds + visited marking
    

---

### 🟠 3. Understand the **Input Format**

- 🧩 **Edge List** → Convert to `adj_list`
- 🧾 **Adjacency List** → Use directly
- 🧮 **Adj** **Matrix** → Use nested loops → Iterate via rows/columns
- 🔢 **Grid (2D)**→ Use `(r, c)` pairs as nodes + direction vectors

---

### 🔵 **4. Choose the Right Graph Representation**

- 🗂 **Adjacency List** → ✅ Best for traversal, sparse graphs
- 📊 **Adjacency Matrix** → ✅ Fast edge lookup - Rare; use for dense graphs
- 🧾 **Edge List** → Only works w/ Union-Find or initial conversion

---

### 🔴 **5. Detect Sub-Pattern & Choose Algorithm**

- 🔍 **Path Existence** → BFS (default) / DFS (enumerate all paths)
- 🛣 **Shortest path** → BFS (unweighted) / Dijkstra (weighted)
- 🔁**Cycle detection (undirected)**→ `DFS + parent` or `Union-Find`
- 🔁**Cycle detection (directed)** → `DFS + visited (3-state)` or `Topological Sort`
- 🌐**Connected components** → DFS / BFS / Union-Find
- 🧱**Flood fill / 2D area** → BFS / DFS w/ bounds + visited on 2D matrix
- 🧮**Node ordering (DAG)** → Topo Sort (DFS or Kahn’s)

---

### 🟤 **6. Handle Traversal Safely**

- ✅ Use `visited` to avoid cycles (esp in DFS)
- 🔁 Add early return if seeking first/shortest match
- ↔ Directed vs undirected affects edge handling
- ⚠ DFS cycle checks differ: use `parent` for undirected, 3-state visited for directed

---

### ⚪ **7. Code Template Setup**

- 🧱 Build `adj_list = defaultdict(list)`
- ⏹ Prepare reusable traversal templates
    - BFS → `queue`
    - DFS → recursive or `stack`
    - Grid → 4-direction moves + bounds check
- ✅ Write test case or dry run small input

---

## 🧠 Summary Mental Model (Top-Down)

```
1. What’s the ask? → Path / Count / Order?
2. What type? → Tree / General / Grid?
3. Input format? → Edge list / Matrix / Grid?
4. Convert to adj_list if needed?
5. Pick traversal → DFS / BFS / UF / Topo / Dijkstra
6. Consider edge cases → Cycles, bounds, disconnected
7. Set up template → Build, trace, code
```

---

### 🎯 Key Insight

> Don’t force-fit. Let input + question guide your graph strategy.
> 
> 
> Focus on identifying the **subpattern**, not just the structure.
>