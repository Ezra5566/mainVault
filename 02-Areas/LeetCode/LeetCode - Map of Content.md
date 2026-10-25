---
tags: [leetcode, dsa, algorithms, python, interview, reference]
aliases: [LeetCode, DSA, Problem Set, Algorithms]
domain: computer-science
level: interview-prep + fundamentals
count: 215
difficulty-mix: [Easy, Medium, Hard]
language: Python
updated: 2026
status: reference
---

# LeetCode / DSA Problem Bank (Python)

> [!abstract] What this is
> A **~214‑problem** study bank organized by *pattern*, not by difficulty. Each problem gives you:
> - **The problem** in 1–2 sentences (enough to restate it from memory).
> - **Pattern** — the named technique (two‑pointers, sliding window, DP, …). This is the single most important line: it tells you *which file/toolbox to reach for* next time.
> - **A clean, commented Python solution** you can read top‑to‑bottom.
> - **Key insight** — the 1‑line "aha."
> - **Complexity** — `O(·)` time and space, and *why*.
>
> The goal is to make you **comprehend the language through problems**: you'll be using lists, dicts, sets, slices, comprehensions, `heapq`, `collections`, `deque`, recursion, and classes exactly the way an interview or a real codebase would.

> [!tip] How to actually study this (the method that works)
> 1. **Don't open the solution first.** Read the problem, write code for *15 minutes* even if you're stuck.
> 2. Compare with the reference. The *gap* between your attempt and the reference is what you learn.
> 3. **Recode the reference from memory** the next day. If you can't, you didn't get it.
> 4. Group by **pattern**, not by problem. Seeing 6 sliding‑window problems beats doing 24 random ones.
> 5. Track which patterns you keep missing; those are your weak files.

**Difficulty legend:** 🟢 Easy · 🟡 Medium · 🔴 Hard

---

## The pattern index (jump to the file)

| # | File | Pattern / theme | # probs |
|---|---|---|---|
| 1 | [[01-Arrays & Two Pointers]] | two‑pointers, prefix sum, in‑place, rotation | 26 |
| 2 | [[02-Strings & Hashing]] | substring, anagram, freq map, sliding window, KMP‑ish | 24 |
| 3 | [[03-Linked List & Binary Trees]] | pointers, recursion on trees, BFS levels, BST | 24 |
| 4 | [[04-Stacks, Queues & Sliding Window]] | monotonic stack/queue, min‑stack, queue simulation | 24 |
| 5 | [[05-Binary Search & Backtracking]] | binary search variants, recursion + prune, subsets/perms | 24 |
| 6 | [[06-Graphs, BFS-DFS & Toposort]] | islands, word ladders, course schedules, bipartite | 22 |
| 7 | [[07-Heaps, Greedy & Intervals]] | priority queues, greedy merge, top‑K, interval scheduling | 20 |
| 8 | [[08-Dynamic Programming]] | 1‑D DP, 2‑D grid, LCS, knapsack, bitmask, interval DP | 27 |
| 9 | [[09-Greedy, Math & Design]] | greedy, math tricks, data‑structure design, brainteasers | 24 |

**Total: 215 problems.** (Two of file 09's entries are cross‑references to problems covered in other files — see their inline links.)

---

## Suggested order for a CS major / interview prep

> [!note] If you have ~8–12 weeks
> - **Weeks 1–2:** Files **01 → 02** (arrays/strings). These are 60% of all Easy problems and build muscle.
> - **Weeks 3–4:** File **04** (sliding window & monotonic stack) + **03** (linked list & trees).
> - **Weeks 5–6:** File **05** (binary search & backtracking) + **06** (graphs/BFS).
> - **Weeks 7–8:** File **07** (heaps/greedy) + **08** (DP start: 1‑D + grids).
> - **Weeks 9–12:** Finish **08** (2‑D / bitmask / interval DP) + **09**. Then re‑do every problem you got wrong.

---

## Reading these notes well

- **Python idioms used throughout** (all explained in [[05-AI-Research/Deep Dives/Python]]):
  - `dict` / `collections.Counter` / `defaultdict` / `deque` — counting & sliding windows.
  - `heapq` — min‑heap, top‑K, median.
  - Recursion + `@functools.lru_cache` — backtracking & memoized DP.
  - List comprehensions, slices, `enumerate`, `zip`, `sorted(..., key=...)`.
  - `collections.deque` for O(1) both‑ends queue.
- **Complexity notation:** `O(n)` = linear; `O(log n)` = binary search; `O(n log n)` = sort + scan; `O(n²)` = nested loops; `O(1)` = constant (hash lookups, dict access). `O(2ⁿ)` = all‑subsets backtracking; `O(cⁿ·k)` = n‑queens/word‑search.
- **Space** is *extra* memory — the input array doesn't count. A recursion stack of depth `n` is `O(n)` space.

---

## The "I keep getting the same problem wrong" diagnostic

> [!question] I wrote the brute force. Now what?
> 1. **Can you state the complexity of your brute force?** (Usually O(n²) or worse.)
> 2. **What is the *operation* you're repeating?** (e.g., rescanning the array for each index.)
> 3. **Can you carry state forward as you scan once?** (That's the O(n) two‑pointer / prefix / sliding‑window trick — 70% of Mediums.)
> 4. **Can you replace "check everything" with a hash lookup?** (That's the O(n) hash trick — the rest.)
>
> If you can do the diagnostic above *in one minute*, you'll pass the interview regardless of which specific problem pops up.

## Related

- **Python language deep‑dive:** [[05-AI-Research/Deep Dives/Python]] · [[05-AI-Research/Deep Dives/Python for AI]]
- **The discrete‑math side of these:** [[06-Math/Discrete/Graph Theory]] · [[06-Math/Discrete/Combinatorics & Counting]]
- **The AI/ML side of your CS story:** [[Generative AI - Map of Content]]
