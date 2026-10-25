---
tags: [leetcode, dsa, graph, bfs, dfs, topological-sort, python]
domain: computer-science
category: 06
count: 22
updated: 2026
status: reference
parent: "[[LeetCode - Map of Content]]"
---

# 06 · Graphs, BFS/DFS & Toposort

> [!abstract] The toolbox in this file
> - **Graph representation** — adjacency list (`dict` of lists) vs. adjacency matrix. The list is almost always the right call.
> - **BFS** (`collections.deque`) — shortest path in *unweighted* graphs, layer‑by‑layer traversal.
> - **DFS** (recursion or a stack) — reachability, cycle detection, *islands* counting.
> - **Union‑Find** — the "merge two sets, are they connected?" data structure behind most "how many components" and "redundant edge" problems.
> - **Topological sort** — ordering a DAG (Kahn's algorithm). If the algorithm can't order *every* node, the graph has a cycle.
>
> The meta‑lesson: **most "grid" problems in LeetCode *are* graph problems** — the cells are nodes, the four neighbors are edges. "Number of islands" and "rotting oranges" are BFS/DFS on a grid.

**Difficulty legend:** 🟢 Easy · 🟡 Medium · 🔴 Hard

---

## 1. Valid Sudoku (LC 36) · 🟢
Check an unfinished 9×9 Sudoku board.

```python
def isValidSudoku(board):
    rows, cols, boxes = [set() for _ in range(9)] * 3
    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v == ".":
                continue
            if v in rows[r] or v in cols[c] or v in boxes[(r // 3) * 3 + c // 3]:
                return False
            rows[r].add(v); cols[c].add(v); boxes[(r // 3) * 3 + c // 3].add(v)
    return True
```
**Key insight:** three parallel sets (row, col, 3×3 box). The box index `(r//3)*3 + c//3` is the standard 0‑8 mapping.
**Complexity:** `O(81)` = `O(1)` time, `O(1)` space.

---

## 2. Number of Islands (LC 200) · 🟡
Count the connected land regions in a 2‑D grid.

```python
def numIslands(grid):
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    def flood(r, c):
        if not (0 <= r < m and 0 <= c < n) or grid[r][c] != "1":
            return
        grid[r][c] = "0"            # mark visited in place
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            flood(r + dr, c + dc)
    count = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == "1":
                flood(r, c)
                count += 1
    return count
```
**Key insight:** the classic "flood fill" — every time you hit unvisited land, flood it (change it to water) and increment the counter. **In‑place** marking avoids a separate `visited` set.
**Complexity:** `O(m·n)` time, `O(m·n)` worst‑case recursion stack.

---

## 3. Surrounded Regions (LC 130) · 🟡
Flip `'O'` → `'X'` for every `O` region *not* touching the border.

```python
def solve(board):
    if not board:
        return
    m, n = len(board), len(board[0])
    def flood(r, c):
        if 0 <= r < m and 0 <= c < n and board[r][c] == "O":
            board[r][c] = "1"            # mark "safe"
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                flood(r + dr, c + dc)
    # 1. Mark all border "O"s as safe
    for i in range(n):
        flood(0, i); flood(m - 1, i)
    for j in range(m):
        flood(j, 0); flood(j, n - 1)
    # 2. Flip the rest
    for r in range(m):
        for c in range(n):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "1":
                board[r][c] = "O"
```
**Key insight:** invert the problem — instead of finding "O's trapped inside," find "O's that *reach* the border." Everything else is trapped.
**Complexity:** `O(m·n)` time, `O(1)` extra (the in‑place "1" marker).

---

## 4. Max Area of Island (LC 695) · 🟡
Largest connected land region.

```python
def maxAreaOfIsland(grid):
    def flood(r, c):
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] != 1:
            return 0
        grid[r][c] = 0
        area = 1
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            area += flood(r + dr, c + dc)
        return area
    best = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            best = max(best, flood(r, c))
    return best
```
**Key insight:** `flood` returns the size of the island it starts on; take the max.
**Complexity:** `O(m·n)` time, `O(m·n)` stack.

---

## 5. Pacific Atlantic Water Flow (LC 417) · 🟡
Cells from which water flows to *both* the Pacific (top/left) and Atlantic (bottom/right).

```python
def pacificAtlantic(heights):
    m, n = len(heights), len(heights[0])
    pac, atl = set(), set()
    def flood(r, c, target):
        if (r, c) in target or not (0 <= r < m and 0 <= c < n):
            return
        target.add((r, c))
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc
            # water flows from `nr,nc` to `r,c` when the neighbor is higher or equal
            if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[r][c]:
                flood(nr, nc, target)
    for i in range(n):
        flood(0, i, pac); flood(m - 1, i, atl)
    for j in range(m):
        flood(j, 0, pac); flood(j, n - 1, atl)
    return [
        [i, j]
        for i in range(m)
        for j in range(n)
        if (i, j) in pac and (i, j) in atl
    ]
```
**Key insight:** instead of asking "does water from (i,j) flow to the Pacific?", ask "from the Pacific, which cells can water *reach* going uphill?" The two sets' intersection is the answer. A "reverse‑BFS from the borders" trick.
**Complexity:** `O(m·n)` time, `O(m·n)` space.

---

## 6. Graph Validity Check (LC 832) · 🟡
Can every node reach every other via undirected edges?

```python
def isValid(edges, n):
    # BFS from node 0; count how many we reach
    from collections import deque
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v); adj[v].append(u)
    seen = set([0])
    q = deque([0])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in seen:
                seen.add(v); q.append(v)
    return len(seen) == n
```
**Key insight:** one BFS from an arbitrary node. If the count is `n`, the graph is connected.
**Complexity:** `O(n + m)` time, `O(n + m)` space.

---

## 7. Rotting Oranges (LC 994) · 🟡
Minimum minutes until all fresh oranges rot (BFS by level).

```python
def orangesRotting(grid):
    from collections import deque
    m, n = len(grid), len(grid[0])
    q, fresh, mins = deque(), 0, 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 2:
                q.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1
    while q:
        r, c, t = q.popleft()
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                q.append((nr, nc, t + 1))
                fresh -= 1
                mins = max(mins, t + 1)
    return -1 if fresh else mins
```
**Key insight:** multi‑source BFS — *all* rotting oranges are in the queue simultaneously. `fresh` counts how many we've rotted; `mins` is the level of the last fresh one.
**Complexity:** `O(m·n)` time, `O(m·n)` space.

---

## 8. Alien Dictionary (LC 274) · 🔴
Topological order from a lexicographic "word" list (in an alien language).

```python
def alienOrder(words):
    from collections import defaultdict, deque
    # 1. Build the graph: edge c1 -> c2 if c1 must come before c2
    adj = defaultdict(set)
    in_deg = defaultdict(int)
    seen = set()
    for w in words:
        for c in w:
            in_deg[c] = 0
            seen.add(c)
    for w1, w2 in zip(words, words[1:]):
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in adj[c1]:
                    adj[c1].add(c2)
                    in_deg[c2] += 1
                break                            # first differing letter decides
        # a shorter word can't come after a longer prefix of it
        if len(w1) > len(w2) and w1.startswith(w2):
            return ""
    # 2. Kahn's algorithm
    q = deque([c for c, d in in_deg.items() if d == 0])
    order = []
    while q:
        c = q.popleft()
        order.append(c)
        for nxt in adj[c]:
            in_deg[nxt] -= 1
            if in_deg[nxt] == 0:
                q.append(nxt)
    return "".join(order) if len(order) == len(seen) else ""
```
**Key insight:** the first *differing* letter in a pair of consecutive words gives the constraint. "a short word followed by a word that has it as a prefix" is a contradiction (the short one must come first, not second).
**Complexity:** `O(S)` time where `S` is the total number of letters.

---

## 9. Course Schedule (LC 207) · 🟡
Can you finish all courses given the prerequisite pairs? (Cycle detection in a directed graph.)

```python
def canFinish(numCourses, prerequisites):
    from collections import defaultdict, deque
    adj = defaultdict(list)
    in_deg = [0] * numCourses
    for a, b in prerequisites:
        adj[b].append(a)
        in_deg[a] += 1
    q = deque([i for i in range(numCourses) if in_deg[i] == 0])
    count = 0
    while q:
        u = q.popleft()
        count += 1
        for v in adj[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                q.append(v)
    return count == numCourses
```
**Key insight:** Kahn's topological sort. If we can order *all* `numCourses` nodes, no cycle. Otherwise there's a cycle we can't complete.
**Complexity:** `O(n + m)` time, `O(n + m)` space.

---

## 10. Course Schedule II (LC 210) · 🟡
Return *a* topological order, or `[]` if a cycle exists.

```python
def findOrder(numCourses, prerequisites):
    from collections import defaultdict, deque
    adj = defaultdict(list)
    in_deg = [0] * numCourses
    for a, b in prerequisites:
        adj[b].append(a); in_deg[a] += 1
    q = deque([i for i in range(numCourses) if in_deg[i] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                q.append(v)
    return order if len(order) == numCourses else []
```
**Key insight:** same as LC 207 but *return the order*. The check `len(order) == numCourses` catches the "cycle left over" case.
**Complexity:** `O(n + m)` time.

---

## 11. Redundant Connection (LC 684) · 🟡
Given `n + 1` edges in an otherwise‑tree‑like graph, find the edge that creates the cycle.

```python
def findRedundantConnection(edges):
    # Union‑Find: the first edge that connects two nodes already in the same set is the redundant one
    parent = list(range(len(edges) + 1))
    rank = [0] * (len(edges) + 1)
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]   # path halving
            x = parent[x]
        return x
    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return [u, v]
        if rank[ru] < rank[rv]:
            ru, rv = rv, ru
        parent[rv] = ru
        rank[ru] = max(rank[ru], rank[rv] + 1)
    return []
```
**Key insight:** **Union‑Find** — process edges in order; when both endpoints already share a root, that edge is the cycle‑maker.
**Complexity:** `O(n α(n))` time where `α` is the (tiny) inverse Ackermann function.

---

## 12. Redundant Connection II (LC 685) · 🔴
Same but the graph is *directed* (each node has exactly one outgoing edge, possibly one incoming "extra").

```python
def findRedundantDirectedConnection(edges):
    n = len(edges)
    parent = [0] * (n + 1)
    has_two = None
    # 1. Find a node with two incoming edges — one of them is the "2nd parent"
    for u, v in edges:
        if parent[v]:
            has_two = (parent[v], v)     # remember the *earlier* edge
            parent[v] = 0               # drop the new one for now
        else:
            parent[v] = u
    # 2. Union‑find with the current parent pointers
    uf = list(range(n + 1))
    def find(x):
        while uf[x] != x:
            uf[x] = uf[uf[x]]
            x = uf[x]
        return x
    for u, v in edges:
        if v:
            ru, rv = find(u), find(v)
            if ru == rv:
                return [u, v]           # cycle, not a 2nd‑parent case
            uf[rv] = ru
    return list(has_two) if has_two else []
```
**Key insight:** there are two possible causes of a redundant edge: (1) a *cycle*, caught by Union‑Find; (2) a node with *two* incoming edges, caught by scanning first.
**Complexity:** `O(n α(n))`.

---

## 13. Number of Provinces (LC 547) · 🟡
Count the connected components in a 2‑D adjacency matrix.

```python
def findCircleNum(isConnected):
    n = len(isConnected)
    seen = [False] * n
    def dfs(u):
        for v in range(n):
            if isConnected[u][v] and not seen[v]:
                seen[v] = True
                dfs(v)
    count = 0
    for i in range(n):
        if not seen[i]:
            seen[i] = True
            dfs(i)
            count += 1
    return count
```
**Key insight:** each new `i` we haven't seen starts a new component.
**Complexity:** `O(n²)` time.

---

## 14. Friend Circles (LC 1135) · 🟡
Given an `n×n` matrix where `m[i][j] == 1` means students `i` and `j` are friends, count the friend *circles* (connected components).

```python
def countFriendCircles(m):
    n = len(m)
    color = [0] * n
    def dfs(i):
        for j in range(n):
            if m[i][j] and color[j] == 0:
                color[j] = 1
                dfs(j)
    circles = 0
    for i in range(n):
        if color[i] == 0:
            dfs(i)
            circles += 1
    return circles
```
**Key insight:** identical shape to LC 547 — "connected components of an adjacency matrix." Each new uncolored student starts a new circle.
**Complexity:** `O(n²)` time.

---

## 15. Number of Connected Components in an Undirected Graph (LC 323) · 🟡
Given `n` nodes and `edgeList`, count connected components.

```python
def countComponents(n, edgeList):
    from collections import defaultdict, deque
    adj = defaultdict(list)
    for u, v in edgeList:
        adj[u].append(v); adj[v].append(u)
    seen = set()
    count = 0
    for start in range(n):
        if start in seen:
            continue
        count += 1
        q = deque([start])
        seen.add(start)
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in seen:
                    seen.add(v); q.append(v)
    return count
```
**Key insight:** each new unvisited node starts a new component. (Equivalent: union‑find, `n − (edges that don't create a cycle)`.)
**Complexity:** `O(n + m)`.

---

## 16. All Paths from Source to Target (LC 797) · 🟡
All paths from node 0 to node `n−1` in a DAG.

```python
def allPathsSourceTarget(graph):
    out = []
    def dfs(path):
        u = path[-1]
        if u == len(graph) - 1:
            out.append(path[:])
            return
        for v in graph[u]:
            path.append(v)
            dfs(path)
            path.pop()
    dfs([0])
    return out
```
**Key insight:** the graph is a DAG, so no cycle check is needed — every path has a finite length. The `path[:]` snapshot stores the finished path before we backtrack.
**Complexity:** depends on the DAG structure; `O(n + m)` per path.

---

## 17. Reconstruct Itinerary (LC 332) · 🟡
Given all tickets for one itinerary, reconstruct the route (use the lexicographically smallest at every step).

```python
def findItinerary(tickets):
    import heapq
    from collections import defaultdict
    adj = defaultdict(list)
    for a, b in tickets:
        adj[a].append(b)
    for k in adj:
        heapq.heapify(adj[k])          # smallest airport name first
    route = []
    def dfs(u):
        while adj[u]:
            dfs(heapq.heappop(adj[u]))
        route.append(u)                 # postorder: add after visiting children
    dfs("JFK")
    return route[::-1]
```
**Key insight:** Hierholzer's algorithm for Eulerian paths. Visit everything (heap gives the smallest first), then append the node to the route *after* its children (postorder), then reverse.
**Complexity:** `O(n log n)`.

---

## 18. Clone Graph (LC 133) · 🟡
Deep‑clone a labeled graph.

```python
def cloneGraph(node):
    if not node:
        return None
    seen = {}
    def dfs(u):
        if u in seen:
            return seen[u]
        clone = Node(u.val, [])
        seen[u] = clone
        for v in u.neighbors:
            clone.neighbors.append(dfs(v))
        return clone
    return dfs(node)
```
**Key insight:** the `seen` dict maps *original* node → *clone* node. The moment we clone a node we add it to `seen` (before recursing) so that cycles are detected and not infinite‑reversed.
**Complexity:** `O(V + E)`.

---

## 19. Bipartite Check (LC 886) · 🟡
Is the graph 2‑colorable?

```python
def isBipartite(graph):
    from collections import deque
    color = {}
    for start in range(len(graph)):
        if start in color:
            continue
        q = deque([(start, 0)])
        color[start] = 0
        while q:
            u, c = q.popleft()
            for v in graph[u]:
                if v in color:
                    if color[v] == c:
                        return False    # two same‑colored neighbors -> not bipartite
                else:
                    color[v] = 1 - c
                    q.append((v, 1 - c))
    return True
```
**Key insight:** color each node; every edge must connect opposite colors. A same‑color edge is the contradiction.
**Complexity:** `O(V + E)`.

---

## 20. Is Graph Bipartite? (LC 802) · 🟡
Same problem, 0‑indexed. The LC 886 and 802 are *the same shape* — just reindexing.

```python
def isBipartite(graph):
    from collections import deque
    color = [-1] * len(graph)
    for start in range(len(graph)):
        if color[start] != -1:
            continue
        color[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in graph[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False
    return True
```
**Complexity:** `O(V + E)`.

---

## 21. Min Cost to Connect All Points (LC 1584) · 🔴
Min cost to connect all points (a 2‑D MST).

```python
import heapq
def minCostConnectPoints(points):
    n = len(points)
    def dist(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    # Prim's: start at 0, grow the tree
    in_tree = [False] * n
    in_tree[0] = True
    pq = [(dist(points[0], points[i]), i) for i in range(1, n)]
    heapq.heapify(pq)
    total = 0
    while pq:
        cost, u = heapq.heappop(pq)
        if in_tree[u]:
            continue
        in_tree[u] = True
        total += cost
        for v in range(n):
            if not in_tree[v]:
                heapq.heappush(pq, (dist(points[u], points[v]), v))
    return total
```
**Key insight:** **Prim's MST** algorithm on a *complete* graph (all pairs have an edge). The lazy heap version (skip already‑in‑tree edges) is the standard Python shape.
**Complexity:** `O(n² log n)`.

---

## 22. Cheapest Flights Within K Stops (LC 787) · 🔴
Cheapest path with at most `K` intermediate stops.

```python
def findCheapestPrice(n, flights, src, dst, k):
    import heapq
    adj = [[] for _ in range(n)]
    for a, b, c in flights:
        adj[a].append((b, c))
    # Dijkstra on (cost, node, stops)
    pq = [(0, src, 0)]
    best = [float("inf")] * n
    best[src] = 0
    ans = float("inf")
    while pq:
        cost, u, stops = heapq.heappop(pq)
        if u == dst:
            ans = min(ans, cost)
            break
        if stops > k:
            continue
        for v, w in adj[u]:
            if cost + w < best[v]:
                best[v] = cost + w
                heapq.heappush(pq, (cost + w, v, stops + 1))
    return ans if ans != float("inf") else -1
```
**Key insight:** Dijkstra's with a *stops* dimension. The `stops > k` check is what keeps the answer correct.
**Complexity:** `O((n + m) log n · k)` in the worst case.

---

## Self‑Test (cover the answers, then reveal)

> [!question] In "Number of Islands," why do we flip `grid[r][c]` to `"0"` *before* recursing?
> Without that, the DFS would revisit the same cell infinitely (the grid has no separate "visited" array). In‑place marking is the trick that lets us use the grid *as* the visited set.

> [!question] Why does "Pacific Atlantic" solve the problem by running BFS *from* the oceans instead of *to* the oceans?
> Walking "uphill from the border" is easier than "downhill from every cell." The reverse‑BFS approach is *monotonic*: once we've decided a cell can reach the Pacific, we don't need to reconsider it.

> [!question] Why does Kahn's algorithm fail (i.e., not order every node) if and only if there's a cycle?
> In a DAG, at least one node has in‑degree 0. We remove it, which lowers its neighbors' in‑degree. Repeat. If we order all `n` nodes, no cycle. If a cycle exists, every node in it has in‑degree ≥ 1 at every step — none can be removed.

> [!question] What's the role of `parent[v]` in the "2nd‑parent" check of LC 685?
> We're building the Union‑Find *without* the new (v‑directed) edge, treating the *first* incoming edge as the parent. If a later edge points to a node that already has a parent, the *new* edge is the redundant one.

> [!question] Why does Hierholzer's algorithm (LC 332) append to `route` *after* the while loop?
> Postorder. We want the *last* visited node to be the *first* one in the route (Eulerian paths are built by "peeling off" from the end). The `route[::-1]` at the end reverses to get the correct reading order.

> [!question] Is the bipartite check "two adjacent nodes have the same color" or "some node has an odd cycle"?
> Both — the same fact phrased two ways. A graph is bipartite ⟺ it has no odd cycle.

## Related

- Next: [[07-Heaps, Greedy & Intervals]] — the "always pick the best available" pattern.
- Back to the index: [[LeetCode - Map of Content]].
- The **Union‑Find** (used in #11, #12, and any "how many connected components?" problem) is the single most under‑taught data structure in the average interview prep. See [[02-Areas/LeetCode/01-Arrays & Two Pointers]] for the "two‑pointer" sibling.
