---
tags: [leetcode, dsa, dynamic-programming, python, interview]
domain: computer-science
category: 08
count: 27
updated: 2026
status: reference
parent: "[[LeetCode - Map of Content]]"
---

# 08 · Dynamic Programming

> [!abstract] DP is one idea, wearing many hats
> Every DP problem is the same three questions answered:
> 1. **What is the *state*?** — the smallest inputs that fully describe a subproblem (usually an index, or a pair of indices, or a bitmask).
> 2. **What is the *transition*?** — how does `dp[state]` build from smaller states? (One equation.)
> 3. **What is the *base case*?** — the `dp[0]` / `dp[·][·]` values you start from.
>
> Once you can write those three, you can *almost always* code it. The rest of this file is those three questions filled in for 26 problems, grouped by the *shape* of the state.

> [!tip] Choose the shape first, then it's mechanical
> | Problem shape | State | Typical size |
> |---|---|---|
> | "prefix / up to index i" | `dp[i]` | `O(n)` |
> | "two strings" | `dp[i][j]` | `O(n·m)` |
> | "grid" | `dp[r][c]` | `O(rows·cols)` |
> | "subset / coin change" | `dp[amount]` | `O(amount)` |
> | "which items chosen" | `dp[i][w]` (knapsack) | `O(n·W)` |
> | "all subsets" | bitmask `dp[mask]` | `O(2ⁿ)` |
>
> **1‑D vs 2‑D rule of thumb:** if the answer depends on "up to the last element," it's 1‑D. If it depends on "how two strings/rows align," it's 2‑D. If it's "pick a subset," it's a knapsack.

> [!warning] Knapsack has two variants — get the loop order right
> - **0/1 knapsack** ("each item at most once"): iterate the inner `weight` loop **backwards** `for w in range(W, weight-1, -1)`.
> - **Unbounded knapsack** ("combinations with reuse," coin change): iterate **forwards** `for w in range(weight, W+1)`.
> The order is the *only* difference — and the most common interview mistake.

**Difficulty legend:** 🟢 Easy · 🟡 Medium · 🔴 Hard

---

## 1. Climbing Stairs (LC 70) · 🟢 *(the 1‑D template)*
Ways to climb `n` stairs (steps of 1 or 2).

```python
def climbStairs(n):
    a, b = 1, 1        # dp[0]=1, dp[1]=1
    for _ in range(n):
        a, b = b, a + b
    return a
```
**State** `dp[i]` = ways to reach step i. **Transition** `dp[i] = dp[i-1] + dp[i-2]`. **Base** `dp[0]=dp[1]=1`. Kept in two vars → `O(1)` space.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 2. Maximum Subarray (LC 53) · 🟡
Largest sum of any contiguous subarray.

```python
def maxSubArray(nums):
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)     # either start new at x, or extend
        best = max(best, cur)
    return best
```
**State** "best subarray ending exactly here." **Transition** `cur = max(x, cur + x)`. This *is* Kadane's algorithm.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 3. House Robber (LC 198) · 🟡
Max you can rob without taking adjacent houses.

```python
def rob(nums):
    take = skip = 0
    for x in nums:
        take, skip = skip + x, max(take, skip)
    return max(take, skip)
```
**State** "best ending *with* the current house" (`take`) and "best ending *without* it" (`skip`). **Transition** as written.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 4. House Robber II (LC 213) · 🟡
Same, but the house list is *circular* (first and last are neighbors).

```python
def rob(nums):
    def linear(a):
        take = skip = 0
        for x in a:
            take, skip = skip + x, max(take, skip)
        return max(take, skip)
    if len(nums) == 1:
        return nums[0]
    return max(linear(nums[:-1]), linear(nums[1:]))
```
**Key insight:** split into two linear problems — "rob 0..n−2" (first in, last out) and "rob 1..n−1" (last in, first out). Take the max.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 5. Maximum Product Subarray (LC 152) · 🟡
Max product of any contiguous subarray (negatives matter!).

```python
def maxProduct(nums):
    hi = lo = best = nums[0]
    for x in nums[1:]:
        hi, lo = max(x, hi * x, lo * x), min(x, hi * x, lo * x)
        best = max(best, hi)
    return best
```
**Key insight:** track *both* the max and min running product — a very negative number times a negative flip‑flops. The simultaneous `hi, lo = ...` uses the *old* values (Python evaluates the RHS first).
**Complexity:** `O(n)` time, `O(1)` space.

---

## 6. Best Time to Buy/Sell with Cooldown (LC 309) · 🟡
Max profit with a 1‑day cooldown after selling.

```python
def maxProfit(prices):
    hold, sold, rest = float("-inf"), 0, 0
    for p in prices:
        hold, sold, rest = max(hold, rest - p), hold + p, max(rest, sold)
    return max(rest, sold)
```
**States** — three: `hold` (in a stock), `sold` (just sold, in cooldown), `rest` (nothing, not in cooldown). The transitions handle "buy, sell, or wait."
**Complexity:** `O(n)` time, `O(1)` space.

---

## 7. Decode Ways (LC 91) · 🟡
A digit string encodes letters (1‑26). How many decodings?

```python
def numDecodings(s):
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 0 if s[0] == "0" else 1
    for i in range(2, n + 1):
        if s[i-1] != "0":
            dp[i] += dp[i-1]                       # 1 digit
        if s[i-2] == "1" or (s[i-2] == "2" and s[i-1] in "0123456"):
            dp[i] += dp[i-2]                       # 2 digits
    return dp[n]
```
**Key insight:** a "0" can't be a standalone letter, so the only way to decode position i is as part of "10" or "20"‑ish. The `s[i-1] in "0123456"` guard handles "20" but not "27."
**Complexity:** `O(n)` time, `O(n)` space.

---

## 8. Minimum Cost Climbing Stairs (LC 746) · 🟢
Each stair costs to *stand on*; return the min cost to reach the top.

```python
def minCostClimbingStairs(cost):
    a, b = 0, 0                       # min cost to be 2 and 1 steps back
    for c in cost:
        a, b = b, min(a, b) + c
    return a
```
**State** "min cost to *step off* from here." You can jump from `i-1` or `i-2`, so `min(a, b) + c`.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 9. Coin Change (LC 322) · 🟡
Min number of coins to make `amount` (unbounded).

```python
def coinChange(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if c <= i:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return -1 if dp[amount] == float("inf") else dp[amount]
```
**Key insight:** *unbounded* coin change. Each coin is a "way to reach i"; take the min. `dp[0] = 0` is the base.
**Complexity:** `O(n·amount)` time, `O(amount)` space.

---

## 10. Coin Change II (LC 518) · 🟡
*Number of combinations* of coins that sum to `amount`.

```python
def change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:                      # OUTER loop = coin
        for i in range(c, amount + 1):   # INNER loop = amount (forwards)
            dp[i] += dp[i - c]
    return dp[amount]
```
**Key insight:** "combinations" (not permutations) → outer loop iterates *coins* so order doesn't double‑count. This is the **unbounded knapsack** shape.
**Complexity:** `O(n·amount)` time.

---

## 11. Target Sum (LC 494) · 🟡
Assign `+` or `−` to reach `target`. Count assignments.

```python
def findTargetSumWays(nums, target):
    from functools import lru_cache
    @lru_cache(None)
    def dfs(i, rem):
        if i == len(nums):
            return 1 if rem == 0 else 0
        return dfs(i + 1, rem - nums[i]) + dfs(i + 1, rem + nums[i])
    return dfs(0, target)
```
**Key insight:** at each element, branch "add" or "subtract." `@lru_cache` memoizes the `(i, remaining)` state. This *is* a 2‑D DP `dp[i][sum]` in disguise.
**Complexity:** `O(n · |sum|)` time.

---

## 12. Partition Equal Subset Sum (LC 416) · 🟡
Can `nums` split into two equal‑sum subsets?

```python
def canPartition(nums):
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    seen = {0}                            # all achievable sums so far
    for x in nums:
        seen = seen | {s + x for s in seen if s + x <= target}
    return target in seen
```
**Key insight:** a subset‑sum reachability set. "Is `target` reachable?" is the whole question. A boolean array over `[0..target]` is the `O(n·target)` version.
**Complexity:** `O(n·sum)` time, `O(target)` space.

---

## 13. Longest Palindromic Substring (LC 5) · 🟡
The longest palindrome *contained in* `s`.

```python
def longestPalindrome(s):
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l + 1:r]
    best = ""
    for i in range(len(s)):
        for a, b in ((i, i), (i, i + 1)):     # odd & even length centers
            p = expand(a, b)
            if len(p) > len(best):
                best = p
    return best
```
**Key insight:** *expand around each center* (odd centers `i`, even centers `i,i+1`). `O(n²)` time; the `O(n)` version is Manacher's algorithm (rarely needed in interviews).
**Complexity:** `O(n²)` time, `O(1)` space.

---

## 14. Palindromic Substrings (LC 647) · 🟡
*Count* all palindromic substrings of `s`.

```python
def countSubstrings(s):
    total = 0
    for i in range(len(s)):
        for a, b in ((i, i), (i, i + 1)):
            l, r = a, b
            while l >= 0 and r < len(s) and s[l] == s[r]:
                total += 1
                l -= 1; r += 1
    return total
```
**Key insight:** same "expand around center" as LC 5, but count *every* expansion (each concentric ring is one more palindrome).
**Complexity:** `O(n²)` time, `O(1)` space.

---

## 15. Longest Common Subsequence (LC 1143) · 🟡
Longest subsequence of two strings that's identical.

```python
def longestCommonSubsequence(t1, t2):
    m, n = len(t1), len(t2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if t1[i-1] == t2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```
**State** "LCS of `t1[:i]` and `t2[:j]`." **Transition** "if the last chars match, add 1 to the diagonal; otherwise take the better of 'skip t1[i]' or 'skip t2[j]'."
**Complexity:** `O(m·n)` time, `O(m·n)` space (→ `O(min(m,n))` if you only keep two rows).

---

## 16. Distinct Subsequences (LC 115) · 🔴
How many distinct subsequences of `s` equal `t`?

```python
def numDistinct(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 1                    # empty t is a subsequence of anything
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i-1][j]       # don't use s[i-1]
            if s[i-1] == t[j-1]:
                dp[i][j] += dp[i-1][j-1]   # use it
    return dp[m][n]
```
**Key insight:** for each pair `(i, j)` either *skip* `s[i]` (carry `dp[i-1][j]`) or *match* it to `t[j-1]` (add `dp[i-1][j-1]` when they're equal).
**Complexity:** `O(m·n)`.

---

## 17. Edit Distance (LC 72) · 🟡
Min edits to turn `word1` into `word2` (insert, delete, replace).

```python
def minDistance(w1, w2):
    m, n = len(w1), len(w2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if w1[i-1] == w2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```
**Key insight:** the classic **Levenshtein** DP. "Match" costs 0 (diagonal); "replace/delete/insert" cost 1 and take the min of the three neighbor cells.
**Complexity:** `O(m·n)`.

---

## 18. Interleaving String (LC 97) · 🟡
Can `s3` be an interleaving of `s1` and `s2`?

```python
def isInterleave(s1, s2, s3):
    m, n = len(s1), len(s2)
    if len(s3) != m + n:
        return False
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for i in range(m + 1):
        for j in range(n + 1):
            if i + j == 0:
                continue
            dp[i][j] = False
            if i and dp[i-1][j] and s1[i-1] == s3[i+j-1]:
                dp[i][j] = True
            if j and dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                dp[i][j] = True
    return dp[m][n]
```
**State** "does `s1[:i] + s2[:j]` interleave to `s3[:i+j]`?" The cell is reachable from above (extend s1) or from the left (extend s2) when the next char matches.
**Complexity:** `O(m·n)`.

---

## 19. Word Break (LC 139) · 🟡
Can `s` be built from words in `wordDict`?

```python
def wordBreak(s, wordDict):
    words = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[len(s)]
```
**Key insight:** `dp[i]` = "can I split `s[:i]`?" The inner loop tries every last word `s[j:i]`.
**Complexity:** `O(n² · k)` where `k` is the slice‑comparison cost (hash is `O(n)`).

---

## 20. Word Break II (LC 140) · 🟡
*All* splits of `s` into `wordDict` words.

```python
def wordBreak(s, wordDict):
    from functools import lru_cache
    words = set(wordDict)
    @lru_cache(None)
    def from_pos(i):
        if i == len(s):
            return [""]
        out = []
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in words:
                for tail in from_pos(j):
                    out.append(s[i:j] + " " + tail if tail else s[i:j])
        return out
    return from_pos(0)
```
**Key insight:** memoized recursion over positions. The `""` base case collapses the join logic (`" " + ""` becomes just the word).
**Complexity:** `O(n²)` subproblems · `O(n)` each.

---

## 21. Unique Paths (LC 62) · 🟢
From top‑left to bottom‑right, moving only right/down: how many paths?

```python
def uniquePaths(m, n):
    dp = [1] * n                       # row 0 is all 1s
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]
```
**Key insight:** each cell = "from above + from the left." Row 0 and column 0 are all `1` (only one way to reach them). Closed form: `C(m+n-2, m-1)`.
**Complexity:** `O(m·n)` time, `O(n)` space.

---

## 22. Unique Paths II (LC 63) · 🟡
Same, but some cells are obstacles.

```python
def uniquePathsWithObstacles(g):
    m, n = len(g), len(g[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1 - g[0][0]
    for i in range(m):
        for j in range(n):
            if g[i][j] == 1:
                dp[i][j] = 0
                continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    return dp[m-1][n-1]
```
**Key insight:** an obstacle cell is `0`; everything else is "above + left."
**Complexity:** `O(m·n)`.

---

## 23. Minimum Path Sum (LC 64) · 🟡
Min sum of a top‑left → bottom‑right path.

```python
def minPathSum(g):
    m, n = len(g), len(g[0])
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            up = dp[i-1][j] if i else float("inf")
            left = dp[i][j-1] if j else float("inf")
            dp[i][j] = g[i][j] + (0 if i == 0 and j == 0 else min(up, left))
    return dp[m-1][n-1]
```
**Key insight:** "cost to reach this cell" = `min(above, left) + cell`. Corner case: `dp[0][0] = g[0][0]`.
**Complexity:** `O(m·n)`.

---

## 24. Dungeon Game (LC 174) · 🔴
Minimum *initial* health to reach the bottom‑right without ever hitting 0.

```python
def calculateMinimumHP(dungeon):
    m, n = len(dungeon), len(dungeon[0])
    # dp[i][j] = min health needed *before stepping on* (i,j) to reach exit.
    # The sentinel row/col are "unreachable from here" (inf); only dp[m][n-1]
    # and dp[m-1][n] (one step past the exit) are 1. Everything else defaults
    # to inf so a cell can't cheat by taking a non-existent neighbor.
    INF = float("inf")
    dp = [[INF] * (n + 1) for _ in range(m + 1)]
    dp[m][n - 1] = 1                  # enter the exit from above
    dp[m - 1][n] = 1                  # enter the exit from the left
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            # survive this tile AND reach the better of the two exits
            need = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
            dp[i][j] = max(1, need)    # health floors at 1
    return dp[0][0]
```
**Key insight:** reverse DP — work from the exit backwards. "How much health must I *have* on this tile so I survive it and reach the better of the two exits?" `max(1, ·)` floors at 1.
**Complexity:** `O(m·n)`.

---

## 25. Longest Increasing Subsequence (LC 300) · 🟡
Length of the longest strictly increasing subsequence.

```python
def lengthOfLIS(nums):
    # O(n^2) DP
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp) if nums else 0
```
> [!tip] The `O(n log n)` version is **patience sorting**:
> ```python
> import bisect
> def lengthOfLIS(nums):
>     tails = []
>     for x in nums:
>         i = bisect.bisect_left(tails, x)
>         if i == len(tails):
>             tails.append(x)
>         else:
>             tails[i] = x
>     return len(tails)
> ```
> `tails` is kept sorted; the length is the LIS length (not the actual subsequence).

**Key insight (O(n²) version):** `dp[i]` = "LIS ending at index i." Each `nums[j] < nums[i]` extends the subsequence ending at `j`.
**Complexity:** `O(n²)` time, `O(n)` space (DP) · `O(n log n)` time, `O(n)` space (patience).

---

## 26. Regular Expression Matching (LC 44) · 🔴
Match `s` to `p` with `.` (any char) and `*` (0 or more of the preceding).

```python
def isMatch(s, p):
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    # empty s matches p if p is a chain of "X*" pairs
    for j in range(1, n + 1):
        if p[j-1] == "*" and j >= 2:
            dp[0][j] = dp[0][j-2]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j-1] == s[i-1] or p[j-1] == ".":
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == "*" and j >= 2:
                # zero of p[j-2]  OR  (match s[i-1] and continue using the *)
                dp[i][j] = dp[i][j-2]
                if p[j-2] == s[i-1] or p[j-2] == ".":
                    dp[i][j] = dp[i][j] or dp[i-1][j]
    return dp[m][n]
```
**Key insight:** `*` gives *two* options: **use zero** of the preceding char (jump to `dp[i][j-2]`) **or** match one more `s[i-1]` and stay on `*` (`dp[i-1][j]`). The `j >= 2` guard prevents indexing `p[j-2]` past the front.
**Complexity:** `O(m·n)`.

---

## 27. Matrix Chain Multiplication (the classic *interval DP*) · 🔴
Given matrix dimensions, find the parenthesization minimizing multiplications.

```python
def matrixChain(dim):
    # dim[i] = rows of matrix i, dim[i+1] = cols of matrix i
    n = len(dim) - 1
    cost = [[0] * n for _ in range(n)]
    for gap in range(1, n):                     # "segment length"
        for l in range(n - gap):
            r = l + gap
            best = float("inf")
            for k in range(l, r):
                c = cost[l][k] + cost[k+1][r] + dim[l] * dim[k+1] * dim[r+1]
                best = min(best, c)
            cost[l][r] = best
    return cost[0][n-1]
```
**Key insight:** **interval DP** — the state is a *range* `[l..r]`; the transition picks where to *split* the range (`k`). Outer loop iterates the range *length* so subproblems are already solved.
**Complexity:** `O(n³)`.

---

## Self‑Test (cover the answers, then reveal)

> [!question] What's the *difference* in loop order between 0/1 and unbounded knapsack?
> 0/1 (each item once): `for w in range(W, weight-1, -1)` (backwards, so each item can only be used once). Unbounded (combinations with reuse): `for w in range(weight, W+1)` (forwards, so reusing the same item is allowed).

> [!question] House Robber II: why does the circular version split into two linear problems?
> If you rob house 0, you can't rob the last. If you don't, you can rob either. The two cases are exactly "0..n−2" and "1..n−1" — each is a normal linear House Robber.

> [!question] Maximum Product Subarray: why track the *min* too?
> A large negative min times a negative number becomes a large positive. If you only track the max, you can't "flip" back through a negative. Both extremes can be the future max.

> [!question] Edit Distance: what are the three "edit" transitions?
> **Insert** (skip `w2[j]`, cost 1 from `dp[i][j-1]`), **Delete** (skip `w1[i]`, cost 1 from `dp[i-1][j]`), **Replace** (diagonal `dp[i-1][j-1]` + 1 if chars differ). If chars are *equal*, the diagonal is free.

> [!question] Dungeon Game: why do we iterate *backwards* from the exit?
> The question is "minimum initial health," which is defined by "how much do I *need* to survive the tiles *ahead*." Forward DP would need to know the exit, so we solve it backwards.

> [!question] Regular Expression `*`: what are the two branches?
> "Use zero" (`dp[i][j-2]`) — skip the `X*` pair entirely. "Use one or more" (`dp[i-1][j]` when `X` matches `s[i-1]`) — consume one `s` char, stay on the same `*`.

> [!question] Matrix Chain: why does the outer loop iterate by *gap* (segment length)?
> A range of length `g+1` only depends on ranges of length `≤ g`. Doing `gap` from 1 to n−1 guarantees every subproblem is solved *before* it's needed.

> [!question] Word Break II (LC 140): why `""` (the empty string) as the base case, not `[]`?
> The join logic `w + " " + tail` breaks at the boundary (no trailing space). `""` collapses that: `w + " " + ""` → `w + " "`, which we special‑case to just `w` when `tail == ""`. Using a list of *lists* would require `"".join(tail_parts)`.

## Related

- Next: [[09-Greedy, Math & Design]] — the "no DP needed, just the right invariant" tier.
- Back to the index: [[LeetCode - Map of Content]].
- The **backtracking + memo** pattern in #11 and #20 is a bridge into the recursion territory of [[05-Binary Search & Backtracking]].
