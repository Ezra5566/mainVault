---
tags: [math, discrete-math, graph-theory, algorithms, cs-foundations, reference]
aliases: [Graph Theory, Graphs, Trees, Euler Paths, Hamiltonian Cycles, Coloring]
unit: "Discrete Mathematics — Unit 5"
level: undergraduate
focus: [graphs, connectivity, trees, euler, hamilton, coloring, planarity, shortest-paths]
updated: 2026
status: reference
---

# Graph Theory

> [!abstract] What this note covers
> A **graph** is a finite set of *vertices* (points, `V`) connected by *edges* (lines, `E`). Almost every "network" question — internet, social media, road maps, dependency resolution, compilers — is a graph question in disguise.
>
> **CS payoffs (this is the most directly CS-applicable branch):**
> - **Connectivity / paths** → network reachability, `ping`, routing.
> - **Trees** → file systems, DOM trees, expression trees, `git` history, `HashMap` internals (when they degrade to trees).
> - **Euler paths** → "can I trace every street exactly once?" — postman's tour, circuit design, DNA sequencing.
> - **Hamiltonian cycles** → the Traveling Salesman Problem (NP-complete — the canonical "hard" problem).
> - **Shortest paths** (Dijkstra, Floyd–Warshall) → GPS, network routing (OSPF/IS-IS), pathfinding.
> - **Bipartite matching** → job assignment, course scheduling.
> - **Coloring** → register allocation in compilers, frequency assignment in wireless, map coloring.
> - **Planarity** → chip layout, `K₅` and `K_{3,3}` are the two "non-planar" shapes to recognize.

## 1. Basic Definitions

- **Graph** `G = (V, E)` with `|V| = n` vertices, `|E| = m` edges.
- **Directed (digraph)**: edges have orientation `(u → v)`. **Undirected**: edges are unordered pairs `{u, v}`.
- **Adjacent (neighboring):** two vertices joined by an edge. **Incident:** an edge touching a vertex.
- **Degree** `deg(v)`: number of edges at `v`. In digraphs split into **in-degree** and **out-degree**.
- **Path:** a walk with no repeated vertices (usually). **Cycle:** a closed path.
- **Subgraph:** a graph whose vertices and edges are subsets of another.
- **Complete graph** `K_n`: all pairs of vertices connected.
- **Simple graph:** no loops, no multiple edges between the same pair.

### 1.1 The Handshaking Lemma (use it constantly)

> [!abstract] In any undirected graph, the sum of all vertex degrees equals **twice** the number of edges.
> ```
> Σ_{v ∈ V} deg(v) = 2m
> ```
> *Why:* each edge contributes 1 to the degree of each of its two endpoints.
>
> **Immediate corollary:** the number of vertices with **odd** degree is *even*. (Proof: `2m` is even; sum of even-degrees is even; so the odd-degree degrees must sum to even, which means an *even count* of odd-degree vertices.)

> [!example] "Can I have a graph on 5 vertices where each has degree 3?"
> Sum of degrees would be `5 × 3 = 15`, but that must equal `2m` (even). 15 is odd ⇒ **impossible**. The handshaking lemma answers this in one line.

## 2. Connectivity & Components

- **Connected:** a path exists between every pair of vertices.
- **Component:** a maximal connected subgraph. A disconnected graph is a disjoint union of its components.
- **Clique:** a set of vertices all mutually adjacent.
- **Complement graph** `\bar{G}`: same vertices, edge iff `G` has *no* edge.
- **Cut vertex / cut edge (bridge):** removing it increases the number of components.
- **2‑connected:** no cut vertex. **Edge‑connectivity** / **vertex‑connectivity** measure "how many must I remove to disconnect it."
- **Strongly connected** (digraphs): every vertex reachable from every other in *both* directions. **Weakly connected:** connected if you ignore edge directions.

> [!tip] Tarjan's algorithm finds strongly-connected components in O(n + m) — this is how compilers do control-flow analysis and how network partitioning is computed.

## 3. Trees (the most important special case)

A **tree** is a connected graph with **no cycles**. The properties "connected + acyclic" and "exactly n−1 edges" are *equivalent* for a connected n-vertex graph.

### 3.1 Characterization (any ONE of these ⇒ tree)

- Connected, acyclic.
- Connected, `m = n − 1`.
- Acyclic, `m = n − 1`.
- Acyclic, every two vertices have a *unique* path between them.
- Adding any new edge creates exactly one cycle.

### 3.2 Rooted trees & parent/children

- **Root** `r`: a chosen vertex; every other vertex has a unique **parent** (the previous vertex on the path from `r`).
- **Leaf**: degree-1 vertex (except the root).
- Height of a tree = longest root-to-leaf path.

> [!tip] Python's built-in `dict`, C's `printf` trees, SQL's `WITH RECURSIVE` — all operate on tree structures. When you traverse a tree (BFS/DFS), you're doing graph traversal.

### 3.3 Spanning trees

A **spanning tree** of a connected graph `G` is a subgraph that is a tree on the same vertex set. Every connected graph has at least one.

> [!example] `K_4` (the complete graph on 4 vertices) has how many spanning trees?
> **Cayley's formula:** `n^{n−2}` labeled trees on n vertices. For `n = 4`: `4² = 16`. (For `K_n` specifically this is the count of all labeled trees.)

### 3.4 Minimal spanning trees (MST)

Weighted graphs: an **MST** is a spanning tree of minimum total edge weight.

- **Kruskal's:** sort edges by weight, add if it doesn't form a cycle (uses a union-find / disjoint-set).
- **Prim's:** grow from a single vertex, always adding the cheapest edge that touches the tree.
- Both are `O(m log m)`. Used in: network design (laying cable/road), clustering (hierarchical clustering is literally MST + cut edges).

### 3.5 Topological sorting (DAGs)

A **DAG** (directed acyclic graph) has a **topological ordering** — a vertex ordering such that every edge `(u,v)` has `u` before `v`.

> [!tip] This is how build systems (Make, `cargo`, `npm`) order tasks, how compilers order statements, how courses/prerequisites get scheduled. Kahn's algorithm (BFS with in-degree tracking) finds one in O(n+m); if you can't order all vertices, the graph has a cycle.

## 4. Euler Paths & Circuits

> [!abstract] An Euler path is a walk that uses *every edge exactly once*. An Euler circuit is a closed one.
>
> **Euler's theorem (1736):**
> - A connected graph has an **Euler circuit** iff **every** vertex has even degree.
> - A connected graph has an **Euler path** (but not circuit) iff **exactly two** vertices have odd degree (the path's start and end).
>
> *Historical origin:* Euler's 1736 "Seven Bridges of Königsburg" — a real city layout with 4 landmasses, each of odd degree, so **no** Euler path/circuit existed. He proved it, inventing graph theory in the process.

> [!example] Is there a route that crosses all seven bridges exactly once?
> No — 4 odd-degree vertices. Need ≤ 2. **Theorem ⇒ impossible.**

## 5. Hamiltonian Paths & Cycles (the "hard" cousin)

> [!abstract] A Hamiltonian path visits **every vertex exactly once**; a Hamiltonian circuit is a closed one.
>
> **Unlike Euler**, there's *no* simple degree-based criterion. Deciding whether a general graph has a Hamiltonian cycle is **NP-complete** (one of Karp's 21 problems). This is the reason the Traveling Salesman Problem (TSP) is the canonical "hard" problem.
>
> **Heuristic test (necessary, not sufficient):** if the graph has a Hamiltonian cycle, every cut-vertex is *not* allowed, and removing any single vertex shouldn't disconnect the graph. But those conditions are far from sufficient.

> [!example] `K_n` has a Hamiltonian cycle for every `n ≥ 3`. Proof sketch: `v₁, v₂, …, v_n, v₁` — the complete graph has every edge, so this is a legal cycle.

### 5.1 TSP heuristics

Since TSP is NP-complete, in practice:
- **Nearest neighbor** (greedy, bad but fast).
- **2-opt / Or-opt** (local improvement).
- **Christofides** (1.5×-approximation for metric TSP).
- **LKH** heuristic (the strongest "nearly optimal" for many instances).

## 6. Graph Coloring & Chromatic Numbers

> [!abstract] A **proper coloring** assigns each vertex a color so that *no two adjacent vertices share a color*. The minimum number of colors is the **chromatic number** `χ(G)`.
>
> **Edge coloring** is analogous (adjacent edges, same color forbidden).

### 6.1 Classical theorems

- **4‑Color Theorem (1976):** any planar graph has `χ ≤ 4`. (The proof is one of the first major theorem-assisted proofs — ~500 cases checked by computer. Still stands; later formalized in Coq.)
- **Greedy bound:** `χ(G) ≤ Δ(G) + 1` where `Δ` is the maximum degree. This is tight in the worst case (odd cycles).
- **Perfect graphs:** for these, `χ(G) = ω(G)` (maximum clique size).
- **Brooks' theorem:** a connected graph with max degree Δ has `χ ≤ Δ` unless it's a complete graph or an odd cycle.

### 6.2 Greedy coloring algorithm

```
color(G):
    order vertices v1, …, vn
    for i = 1..n:
        color(vi) = smallest color not used by vi's earlier-colored neighbors
```
This uses ≤ Δ+1 colors (the Brooks/greedy bound). Different *orderings* give different results — a known trick is **DSATUR**: pick the vertex with the most saturated (distinct colors on neighbors) degree first.

## 7. Planarity

> [!abstract] A graph is **planar** if it can be drawn on the plane with no edge crossings.
>
> **Euler's formula:** for a connected planar graph, `n − m + r = 2` where `r` = number of *faces* (regions including the outer one).
> **Corollary:** if planar and each face has ≥ 3 edges, `m ≤ 3n − 6`. If planar and *triangular*, `m = 3n − 6`.

### 7.1 Kuratowski's theorem (the two forbidden shapes)

> [!abstract] A graph is planar **iff** it contains no subgraph homeomorphic to `K_5` (5-vertex complete) or `K_{3,3}` (complete bipartite on 3+3 vertices).

> [!example] Why `K_5` isn't planar
> `K_5` has `n = 5, m = 10`. If planar, `m ≤ 3n − 6 = 9`. But 10 > 9 ⇒ **not planar**. One-line proof.
>
> Why `K_{3,3}` isn't: `n = 6, m = 9`. If planar, each face has ≥ 4 edges (bipartite ⇒ no odd cycle ⇒ no 3-gon). So `2m ≥ 4r`. Combined with Euler's `n − m + r = 2`: `6 − 9 + r = 2` ⇒ `r = 5`. But `2m = 18 ≥ 4·5 = 20`? No — 18 < 20. Contradiction. **Not planar.**

> [!tip] In chip design, a planar circuit has all wires on one side of the board; `K_5` or `K_{3,3}` in the signal graph means you **must** use vias (holes to the back side).

## 8. Shortest-Path Algorithms (the core of "routing")

### 8.1 Unweighted (BFS)

**Breadth-first search** from source `s`: distances from s to all reachable vertices in O(n+m) time.

### 8.2 Weighted (Dijkstra)

**Dijkstra** on a graph with **non-negative** edge weights:
1. Start with `dist(s) = 0`, all others `∞`.
2. Repeatedly pick the unvisited vertex with smallest tentative distance, finalize it, relax its outgoing edges.
3. `O((n+m) log n)` with a binary heap.

> [!warning] Dijkstra does **not** work with negative edges. For those, use **Bellman–Ford** `O(n·m)`, which also detects negative cycles.

### 8.3 All-pairs (Floyd–Warshall)

**Floyd–Warshall** computes shortest paths between *all* pairs in O(n³):
```
for k in 1..n:
    for i in 1..n:
        for j in 1..n:
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
```
Handles negative weights (no negative cycles) — the standard for small-to-medium dense graphs.

### 8.4 Real-world routing

- **OSPF / IS-IS** (IP networking) use Dijkstra for link-state routing.
- **GPS navigation** runs a *weighted* Dijkstra/A\* on a road graph; the A\* heuristic is "straight-line distance to destination."
- **Map matching** in transit apps is a layered graph + Dijkstra variant.

## 9. Bipartite Graphs & Matching

A **bipartite graph** has vertices split into two sets `L, R` where every edge goes between L and R (never within one set).

> [!example] Is this graph bipartite?
> A graph is bipartite **iff** it has **no odd cycle.** So `K_4` (has a 3-cycle) is *not* bipartite; `K_{3,3}` (all 4- and 6-cycles) *is* bipartite.

### 9.1 Maximum matching

A **matching** is a set of edges no two of which share a vertex. A **maximum matching** is the largest such set.

- **Kőnig's theorem (1931):** in any bipartite graph, the size of a maximum matching equals the size of a minimum vertex cover.
- **Augmenting-path algorithm (Kőnig):** repeatedly find an augmenting path (increases matching by 1) until none remain. O(m√n) via Hopcroft–Karp.

### 9.2 CS applications

- **Job assignment:** workers on `L`, jobs on `R`, edges = "worker can do job." Maximum matching = max # workers placed.
- **Course scheduling:** students on `L`, sections on `R`, edges = "prefers."
- **DNA sequence assembly** (overlapping read pairs) is a bipartite matching.
- **Database join algorithms** use bipartite structure when joining two tables.

## 10. A Python sanity check (Dijkstra)

```python
import heapq

def dijkstra(graph, source):
    """graph: dict mapping vertex -> list of (neighbor, weight).
    Returns {vertex: shortest distance from source}."""
    dist = {v: float("inf") for v in graph}
    dist[source] = 0
    pq = [(0, source)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

# Example: 5-node graph
g = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("D", 3)],
    "C": [("A", 2), ("D", 1), ("E", 5)],
    "D": [("B", 3), ("C", 1), ("E", 2)],
    "E": [("C", 5), ("D", 2)],
}
print(dijkstra(g, "A"))
# {'A': 0, 'B': 4, 'C': 2, 'D': 3, 'E': 5}
```

## 11. Related & Next

- **Prereqs:** [[Sets, Relations & Functions]] (a *directed graph is literally a binary relation on a set of vertices*).
- **Cross-links:**
  - **Recurrences on graphs:** dynamic programming on DAGs (topological order → DP) is how the running-time of many algorithms is bounded; see [[Number Theory & Recurrence Relations]] §4.6 (Master Theorem preview).
  - **Cryptography:** elliptic-curve crypto uses *graphs over finite fields*; see [[class_AI/AI_Foundations_Weeks_1-2]] for applied references.
  - **Combinatorics:** graph enumeration (labeled trees, etc.) is a counting problem; see [[Combinatorics & Counting]].
- **Hub:** [[Discrete Mathematics - Map of Content]].

## 12. Self‑Test (active recall)

> [!question] Why does the handshaking lemma imply "the number of odd-degree vertices is even"?
> Sum of degrees = 2m (even). Split the sum into even-degree + odd-degree. The even-degree part is even. So the odd-degree part must be even; but a sum of k odd numbers is even **only if** k is even. Hence an even count of odd-degree vertices.

> [!question] Characterize when a connected graph has an Euler circuit vs an Euler path.
> **Circuit:** every vertex even degree. **Path:** exactly two odd-degree vertices (the path's endpoints).

> [!question] Why is the Traveling Salesman Problem "hard" while the Postman problem (Euler circuit) is "easy"?
> Finding a **minimum-weight Hamiltonian cycle** is NP-complete (no known polynomial algorithm). Deciding **whether an Euler circuit exists** is just counting odd-degree vertices — linear time. The asymmetry is the whole point of Karp's list of NP-complete problems: some "sound like counting" but are deep.

> [!question] Is `K_6` planar? Why?
> `K_6`: `n = 6, m = 15`. Planar requires `m ≤ 3n − 6 = 12`. 15 > 12 ⇒ **not planar**. (Any `K_n` for n ≥ 5 is not planar.)

> [!question] Why does Dijkstra fail on negative-weight edges?
> Dijkstra's key assumption: "once I finalize the shortest distance to a vertex, no later discovery can improve it." Negative edges break this — a "worse" path that goes through a negative edge can later turn out to be better. Use **Bellman–Ford** instead.

> [!question] Prove that any tree on n vertices has n − 1 edges (by induction).
> **Base n = 1:** one vertex, zero edges, `0 = 1 − 1` ✓.
> **Step:** assume any tree on k vertices has k − 1 edges. Take a tree on k+1 vertices; remove a leaf (always exists in a tree). The result is a tree on k vertices, so by IH it has k − 1 edges; the leaf's one edge makes the total k. Hence any tree on k+1 vertices has `(k+1) − 1 = k` edges. ∎
> (This is *exactly* the induction technique from [[Logic & Proof Techniques]] §5.5.)

> [!question] What's the chromatic number of an odd cycle `C_7`?
> 3 (odd cycles are the tight cases: they need exactly 3 colors — one more than their two endpoints would want).

> [!question] What two graphs are **forbidden** in every planar graph (Kuratowski)?
> `K_5` and `K_{3,3}`. Their *subdivisions* (stretching edges) too.
