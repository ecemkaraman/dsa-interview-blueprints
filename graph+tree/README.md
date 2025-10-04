# Graph & Tree - DFS/BFS Templates
<aside>

**BFS/DFS (graph/tree)**: `Time = O(V+E)` (trees: `O(n)`), **Space** = `O(V)` worst (stack/queue/recursion).

</aside>

# 🌳 Tree Traversals

> Assume class TreeNode: def __init__(self,val,left=None,right=None): ...
> 

### 🧊 Tree BFS (Level Order)

 `Queue levels → pop node → enqueue children`

```python
from collections import deque

def bfs_tree(root):
    if not root: return []
    q, order = deque([root]), []
    while q:
        node = q.popleft()
        order.append(node.val)
        if node.left:  q.append(node.left)
        if node.right: q.append(node.right)
    return order

```

---

### 🌲 Preorder (Root→Left→Right)

### Recursive

 `visit(root) → preorder(left) → preorder(right)`

```python
def preorder_rec(root):
    if not root: return []
    return [root.val] + preorder_rec(root.left) + preorder_rec(root.right)
```

### Iterative

 `Stack → pop → record → push Right then Left`

```python
def preorder_iter(root):
    if not root: return []
    stack, out = [root], []
    while stack:
        node = stack.pop()
        out.append(node.val)
        if node.right: stack.append(node.right)
        if node.left:  stack.append(node.left)
    return out
```

---

### 🌿 Inorder (Left→Root→Right)

### Recursive

 `inorder(left) → visit(root) → inorder(right)`

```python
def inorder_rec(root):
    if not root: return []
    return inorder_rec(root.left) + [root.val] + inorder_rec(root.right)

```

### Iterative

 `Go left pushing stack → pop/process → go right`

```python
def inorder_iter(root):
    out, stack, cur = [], [], root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        out.append(cur.val)
        cur = cur.right
    return out
```

---

### 🍂 Postorder (Left→Right→Root)

### Recursive

 `post(left) → post(right) → visit(root)`

```python
def postorder_rec(root):
    if not root: return []
    return postorder_rec(root.left) + postorder_rec(root.right) + [root.val]

```

### Iterative (Reverse-Preorder trick)

 `Traverse Root→Right→Left → reverse`

```python
def postorder_iter_reverse_pre(root):
    if not root: return []
    stack, out = [root], []
    while stack:
        node = stack.pop()
        out.append(node.val)
        if node.left:  stack.append(node.left)   # push Left first
        if node.right: stack.append(node.right) # so Right is processed first
    return out[::-1]

```

---

# 🧭 Graph Traversals

### 🔷 Graph BFS (adjacency list)

 `Queue + Visited → pop → enqueue unvisited neighbors`

- 🧮 Track `level`, `distance`, or `parent` inside BFS loop if needed

```python
from collections import deque

def bfs(start, graph):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

    return result
```

---

### 🕳️ Graph DFS – Recursive

`visit node → recurse on unvisited neighbors`

```python
def dfs_recursive(node, graph, visited, result):
    if node in visited:
        return
    visited.add(node)
    result.append(node)                # record traversal order
    for nei in graph[node]:
        dfs_recursive(nei, graph, visited, result)

# Usage:
visited, result = set(), []
dfs_recursive(start, graph, visited, result)
```

---

### 🧱 Graph DFS – Iterative (stack)

 `stack pop → if unseen, mark+record → push neighbors`

```python
def dfs_iterative(start, graph):
    visited, result = set(), []
    stack = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        result.append(node)

        for nei in graph[node]: # use **reversed(graph[node])** to match rec. order
            stack.append(nei)

    return result
```

- **Recursive DFS** → execute neighbor calls immediately **immediately in listed order**, **first neighbor visited first →** direct execution, no queueing
- **Iterative DFS (stack)** → **schedule** all neighbors on the stack first → then pops them in **reverse order** (LIFO)**→** opposite order or recursive DFS
- To match recursive order in iterative → **push `reversed(graph[node])`**

---

### 🪢 **Union-Find (Disjoint Set Union, DSU)**

- ✅ Used to track connected components efficiently (esp. dynamic merges)
- ✅ `find()` climb parent chain until the root of a node, with **path compression**
- ✅ `union()` merges two sets, optimized by **rank (tree height)→** attach smaller rank/size tree under larger.

```python
class UnionFind:
    def __init__(self, size):
    # Step 1: Init each node as its own parent
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)

        if rootX == rootY:
            return False  # already connected

        # union by rank
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True
```

---

### 🔁 **Topological Sort – BFS-based (Kahn’s)**

- Compute **indegree** for all nodes.
- Start with **indegree=0** nodes in queue.
- Remove nodes layer by layer (like BFS)**:** Pop → append to order → decrement neighbors’ indegree → enqueue when indegree=0.
- ✅ Detect cycles if result size < num nodes

```python
from collections import deque, defaultdict

def kahn_topo_sort(graph, num_nodes):
    indegree = [0] * num_nodes
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = deque([i for i in range(num_nodes) if indegree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == num_nodes else [] # return empty if cycle
```

```python
# Step 1: Build in-degree array
for node in graph → indegree[neighbor] += 1

# Step 2: Init queue with in-degree == 0
queue = deque([nodes with indegree 0])

# Step 3: While queue not empty
    pop node → add to result  
    for neighbor → reduce indegree  
    if indegree == 0 → enqueue

# Step 4: Return result or [] if cycle
```

---

## 📌 Summary

- **Graph BFS:** `Queue; seen; pop u → enqueue unseen neighbors`
- **Graph DFS Rec:** `visit u; recurse unseen neighbors`
- **Graph DFS Iter:** `Stack; push on discovery; pop/process`
- **Union-Find:** `Find rep with path compression; Union by rank/size`
- **Topo Sort (Kahn’s):** `Indegree → queue zeroes → pop & decrement → enqueue new zeroes`
- **Topo Sort (DFS):** `DFS; on exit push node → reverse list`
- **Tree BFS:** `Queue nodes; enqueue children`
- **Preorder Iter:** `Stack; pop→visit; push R then L`
- **Inorder Iter:** `Push left chain; pop→visit; go right`
- **Postorder Iter (rev-pre):** `Root→Right→Left, reverse`
- **Postorder Iter (last_visited):** `Peek; if right unvisited → go right else pop→visit`