---
tags: [leetcode, dsa, binary-search, backtracking, recursion, python]
domain: computer-science
category: 05
count: 24
updated: 2026
status: reference
parent: "[[LeetCode - Map of Content]]"
---

# 05 · Binary Search & Backtracking

> [!abstract] The two toolboxes
> **Binary search** (and its generalization, **search on the *answer***) is for anything "monotonic": a yes/no predicate that flips once and never flips back.
>
> **Backtracking** is "try a choice, recurse, undo the choice." It's how you enumerate *all* solutions to a constraint problem — subsets, permutations, Sudoku, N‑queens, word search.
>
> The single most common interview trap in this file: **the off‑by‑one in the binary‑search loop**. Pick *one* convention and stick with it:
> - `lo, hi = 0, len(arr)` (half‑open) → while `lo < hi`, `hi = mid`
> - `lo, hi = 0, len(arr) - 1` (closed) → while `lo <= hi`, `hi = mid - 1`
>
> Mixing conventions is how you spend 20 minutes on a 5‑minute problem.

**Difficulty legend:** 🟢 Easy · 🟡 Medium · 🔴 Hard

---

## 1. Binary Search (LC 704) · 🟢
Find `target` in a sorted array, or −1.

```python
def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```
**Key insight:** the classic closed‑interval form. `lo <= hi` (not `<`) is the closed version; `hi = mid - 1` (not `mid`) is what keeps it from infinite‑looping on a 2‑element array.
**Complexity:** `O(log n)` time, `O(1)` space.

---

## 2. Search a 2D Matrix (LC 74) · 🟡
A row‑major sorted matrix. Search in `O(log m + log n)`.

```python
def searchMatrix(matrix, target):
    if not matrix:
        return False
    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m * n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = matrix[mid // n][mid % n]
        if val == target:
            return True
        if val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
```
**Key insight:** the matrix is "flattened" — index `i` is row `i // n`, col `i % n`. One binary search over the virtual 1‑D index space.
**Complexity:** `O(log(mn))` time, `O(1)` space.

---

## 3. Search in Rotated Sorted Array (LC 33) · 🟡
A sorted array was rotated. Search for `target` in `O(log n)`.

```python
def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        # which half is actually sorted?
        if nums[lo] <= nums[mid]:
            # left half sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            # right half sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
```
**Key insight:** even in a rotated array, *one* half is sorted. If the target is in the sorted half, go there; otherwise the target must be in the other half.
**Complexity:** `O(log n)` time, `O(1)` space.

---

## 4. Find Minimum in Rotated Sorted Array (LC 153) · 🟡
Find the minimum of a rotated array. (See also [[01-Arrays & Two Pointers]] #22.)

```python
def findMin(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]
```
**Key insight:** compare the middle with the *right end*. `nums[mid] > nums[hi]` means the drop happened to the right of `mid`; otherwise the min is at `mid` or to its left.
**Complexity:** `O(log n)` time, `O(1)` space.

---

## 5. First Bad Version (LC 278) · 🟢
The classic "search on the answer" binary search.

```python
# The bool API is provided: isBadVersion(version) -> bool
def firstBadVersion(n):
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) // 2
        if isBadVersion(mid):
            hi = mid          # mid is bad; the *first* bad is in [lo, mid]
        else:
            lo = mid + 1     # mid is good; the first bad is to the right
    return lo
```
**Key insight:** the predicate `isBadVersion(v)` is **monotonic**: good, good, …, bad, bad, … . Binary search finds the *boundary*. Note `hi = mid` (not `mid - 1`) — we can't discard `mid` because it might *be* the boundary.
**Complexity:** `O(log n)` time.

---

## 6. Capacity To Ship Within D Days (LC 1011) · 🟡
Min capacity so the shipper can deliver in `D` days.

```python
def shipWithinDays(weights, D):
    lo, hi = max(weights), sum(weights)   # capacity can't be less than the biggest box, or more than the total
    while lo < hi:
        mid = (lo + hi) // 2
        # how many days do we need with capacity `mid`?
        days, cur = 1, 0
        for w in weights:
            if cur + w > mid:
                days += 1
                cur = 0
            cur += w
        if days <= D:
            hi = mid         # mid is "enough" — try smaller
        else:
            lo = mid + 1     # not enough — need bigger
    return lo
```
**Key insight:** "min capacity" is the classic *search‑on‑the‑answer*. The "days needed with capacity X" check is `O(n)`. Total `O(n · log Σ)` — a very common interview shape.
**Complexity:** `O(n log(Σw))` time.

---

## 7. Koko Eating Bananas (LC 875) · 🟡
Min integer eating rate to finish all piles in `h` hours.

```python
def minEatingRate(piles, h):
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        # hours needed if Koko eats `mid` per hour
        hours = sum((p + mid - 1) // mid for p in piles)   # ceil(p/mid)
        if hours <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo
```
**Key insight:** same *search‑on‑the‑answer* shape as LC 1011. `(p + mid - 1) // mid` is the integer‑division "ceiling" idiom.
**Complexity:** `O(n log max(piles))` time.

---

## 8. Find Smallest Letter Greater Than Target (LC 744) · 🟢
Smallest character in `ordered` strictly greater than `target`.

```python
def nextGreatestLetter(letters, target):
    lo, hi = 0, len(letters)
    while lo < hi:
        mid = (lo + hi) // 2
        if letters[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    if lo == len(letters):
        return letters[0]      # wrap around
    return letters[lo]
```
**Key insight:** `bisect_right` — find the first position `> target`. If we're past the end, wrap to the front.
**Complexity:** `O(log n)` time, `O(1)` space.

---

## 9. Search in a Binary Search Tree (LC 700) · 🟢
Find the node in a BST with value `val`.

```python
def searchBST(root, val):
    while root:
        if root.val == val:
            return root
        root = root.left if root.val > val else root.right
    return None
```
**Key insight:** if `val < root.val` the answer is in the left; else right. The `O(log n)` average is only guaranteed if the BST is *balanced* — otherwise `O(n)`.
**Complexity:** `O(h)` time where `h` is the tree height, `O(1)` space (iterative).

---

## 10. Insert into a Binary Search Tree (LC 701) · 🟡
Insert `val` into a BST.

```python
def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)
    return root
```
**Key insight:** the same `O(h)` walk; once you reach a `None` parent, attach the new node there.
**Complexity:** `O(h)` time, `O(h)` recursion space.

---

## 11. Delete Node in a BST (LC 450) · 🟡
Delete a node from a BST.

```python
def deleteNode(root, key):
    if not root:
        return None
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # key == root.val
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        # two children: replace with successor, delete it
        cur = root.right
        while cur.left:
            cur = cur.left
        root.val = cur.val
        root.right = deleteNode(root.right, cur.val)
    return root
```
**Key insight:** the "two‑children" case is the only hard one — replace with the **inorder successor** (leftmost of the right subtree) and delete that leaf.
**Complexity:** `O(h)` time, `O(h)` space.

---

## 12. Range Sum of BST (LC 938) · 🟢
Sum of node values in a BST within `[low, high]`.

```python
def rangeSumBST(root, low, high):
    if not root:
        return 0
    if low <= root.val <= high:
        return root.val + rangeSumBST(root.left, low, root.val - 1) \
                   + rangeSumBST(root.right, root.val + 1, high)
    if root.val < low:
        return rangeSumBST(root.right, low, high)
    return rangeSumBST(root.left, low, high)
```
**Key insight:** *prune the recursion*. If `root.val` is outside the range, the whole subtree on the wrong side is also outside — skip it.
**Complexity:** `O(n)` worst case, `O(1)` extra space (output aside).

---

## 13. Convert Sorted Array to BST (LC 108) · 🟡
Build a balanced BST from a sorted array.

```python
def sortedArrayToBST(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    node = TreeNode(nums[mid])
    node.left = sortedArrayToBST(nums[:mid])
    node.right = sortedArrayToBST(nums[mid + 1:])
    return node
```
**Key insight:** pick the *middle* as the root (balances the tree); recurse on the halves. `O(log n)` depth.
**Complexity:** `O(n)` time, `O(n)` space (the array copies).

---

## 14. Koko Eating Bananas — *variant*: binary search over the *rate*, verify by scanning.
Already shown in #7. The meta‑lesson: **whenever a problem says "find the minimum X such that P(X)", P is almost always monotonic — binary search the answer.**

---

## 15. Two Sum II — *binary search version* · 🟡
Given a sorted array and `target`, return the **1‑based** indices of two numbers summing to `target`.

```python
def twoSum(numbers, target):
    lo, hi = 0, len(numbers) - 1
    while lo < hi:
        s = numbers[lo] + numbers[hi]
        if s == target:
            return [lo + 1, hi + 1]
        if s < target:
            lo += 1
        else:
            hi -= 1
    return []
```
**Key insight:** two pointers (same as LC 167) — because the array is sorted, one pointer decides.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 16. Peak Index in a Mountain Array (LC 852) · 🟡
Find the peak in a strictly increasing‑then‑decreasing array.

```python
def findPeakIndex(arr):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < arr[mid + 1]:
            lo = mid + 1     # still going up — the peak is to the right
        else:
            hi = mid         # peak is at mid or to the left
    return lo
```
**Key insight:** binary search on a *unimodal* function. If `mid < mid+1` we're on the rising slope; go right.
**Complexity:** `O(log n)` time, `O(1)` space.

---

## 17. Count of Ranges (LC 1442 / generic) · 🟢
Count pairs `(i, j)` with `i < j` and `sum = sum(nums[i..j])` between `low` and `high`.

```python
def countRangeSum(nums, low, high):
    from bisect import bisect_left, bisect_right
    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + x)
    total = 0
    sorted_prefix = []
    for s in prefix:
        total += bisect_right(sorted_prefix, s - low) - bisect_left(sorted_prefix, s - high - 1)
        # insert s into sorted_prefix
        idx = bisect_left(sorted_prefix, s)
        sorted_prefix.insert(idx, s)
    return total
```
> [!note] A cleaner `O(n log n)` version uses a **Fenwick tree** (binary indexed tree) on the prefix sums after coordinate‑compression. The `insert` above is `O(n)` per step, so that whole thing is actually `O(n²)` — the Fenwick version is what a strong interview answer uses. The simpler `O(n²)` brute force also works on small constraints:

```python
def countRangeSum(nums, low, high):
    total = 0
    for i in range(len(nums)):
        s = 0
        for j in range(i, -1, -1):
            s += nums[j]
            if low <= s <= high:
                total += 1
    return total
```
**Complexity:** `O(n²)` brute force; `O(n log n)` with a Fenwick tree.

---

## 18. Subarray Product Less Than K (LC 713) · 🟡
Already in [[01-Arrays & Two Pointers]] #18 — sliding window, not binary search. Mentioned here for the "count subarrays" family.

---

## 19. Search Suggestions System (LC 1268) · 🟡
Autocomplete: after each prefix of `s`, return up to 3 matching products (lexicographic).

```python
class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        from bisect import bisect_left
        out = []
        prefix = ""
        for ch in searchWord:
            prefix += ch
            i = bisect_left(products, prefix)
            out.append(products[i:i + 3])
        return out
```
**Key insight:** binary search finds where `prefix` fits in the *sorted* product list; the next 3 elements are the candidates.
**Complexity:** `O(m log n + k)` where `m = len(searchWord)`, `n = len(products)`.

---

## 20. Time Based Key‑Value Store (LC 981) · 🟡
A store where `get(k, timestamp)` returns the last `set` at or before the timestamp.

```python
class TimeMap:
    def __init__(self):
        self.d = {}
    def set(self, key, timestamp, value):
        self.d.setdefault(key, []).append((timestamp, value))
    def get(self, key, timestamp):
        # binary search for the last (ts, val) with ts <= timestamp
        from bisect import bisect_right
        entries = self.d.get(key, [])
        i = bisect_right([e[0] for e in entries], timestamp) - 1
        return entries[i][1] if i >= 0 else ""
```
**Key insight:** the `bisect` module does "find the last value ≤ timestamp" in one call.
**Complexity:** `O(log m)` per `get` where `m` is the number of entries for `key`.

---

## 21. Generate a String With Characters of Odd Counts (LC 1248) · 🟢
Length `n`, all lowercase, odd counts for every character that appears.

```python
def generateTheString(n):
    # simplest: 1 of 'a' (if n is odd) + (n-1) of 'b', or n of 'a'
    if n % 2 == 0:
        return "a" * (n - 1) + "b"     # n-1 is odd, 1 is odd
    return "a" * n
```
**Key insight:** `n` chars of one letter works when `n` is odd; for even `n`, use `n−1` of `a` and `1` of `b` (both odd).
**Complexity:** `O(n)` time.

---

## 22. Permutations (LC 46) · 🟡
All permutations of a list of distinct numbers.

```python
def permute(nums):
    out = []
    def backtrack(path, remaining):
        if not remaining:
            out.append(path[:])
            return
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()
    backtrack([], nums)
    return out
```
**Key insight:** the classic "pick each unused item, recurse, undo" shape. `remaining[:i] + remaining[i+1:]` removes `remaining[i]` without mutating.
**Complexity:** `O(n! · n)` time (n! permutations, each O(n) to copy), `O(n)` stack.

---

## 23. Combinations Sum (LC 39) · 🟡
All combinations (with reuse) that sum to `target`.

```python
def combinationSum(candidates, target):
    out = []
    def dfs(start, path, rem):
        if rem == 0:
            out.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > rem:
                continue
            path.append(candidates[i])
            dfs(i, path, rem - candidates[i])   # `i`, not `i+1` — reuse allowed
            path.pop()
    dfs(0, [], target)
    return out
```
**Key insight:** `start` parameter + passing `i` (not `i+1`) back in = "reuse allowed." Passing `i + 1` = "no reuse." One‑line difference, two different problems.
**Complexity:** worst case `O(target)` deep recursion with many branches; bounded by the number of combinations.

---

## 24. Combination Sum II (LC 40) · 🟡
Same but *each number used at most once* and the input may have duplicates.

```python
def combinationSum2(candidates, target):
    candidates.sort()
    out = []
    def dfs(start, path, rem):
        if rem == 0:
            out.append(path[:])
            return
        prev = None
        for i in range(start, len(candidates)):
            # skip duplicates at the *same depth* to avoid duplicate combinations
            if candidates[i] == prev:
                continue
            prev = candidates[i]
            if candidates[i] > rem:
                break          # sorted; all later are bigger too
            path.append(candidates[i])
            dfs(i + 1, path, rem - candidates[i])   # i+1: no reuse
            path.pop()
    dfs(0, [], target)
    return out
```
**Key insight:** two tricks: (1) pass `i + 1` (no reuse), (2) `if candidates[i] == prev: continue` skips the duplicate *at the same tree level* — this is the classic "dedup in permutations" idiom.
**Complexity:** `O(n · 2ⁿ)` worst case.

---

## Self‑Test (cover the answers, then reveal)

> [!question] First Bad Version (LC 278): why `hi = mid` and not `hi = mid - 1`?
> Because `mid` *might* be the first bad version. Discarding it (`hi = mid - 1`) would skip the boundary. With `hi = mid`, the interval shrinks but always keeps the boundary in `[lo, hi]`.

> [!question] Why does `bisect_right(arr, target) - 1` give "the last value ≤ target"?
> `bisect_right` returns the first index where `arr[i] > target`. The previous index is the last one where `arr[i] <= target`. Subtracting 1 gives exactly that index.

> [!question] In "search on the answer" (LC 1011, 875), how do you pick `lo` and `hi`?
> `lo` = the smallest *feasible* value (usually `max(weights)` for capacity, `1` for rate), `hi` = the largest feasible value (usually `sum(weights)` for capacity, `max(piles)` for rate). Then binary search.

> [!question] Permutations (LC 46): why does `path[:]` (not `path`) go into `out`?
> `path` is *mutated* on the way back up (we `pop`). Storing the list itself would store the *same* object and later undo its contents. `path[:]` is a snapshot.

> [!question] Combination Sum II (LC 40): what does `if candidates[i] == prev: continue` actually prevent?
> It prevents two sibling branches that produce the *same* combination. After sorting, `[1, 1, 2]` could be chosen as "first 1, then 2" or "second 1, then 2" — both give `[1, 2]`. The skip collapses them into one.

> [!question] Peak Index (LC 852): why is `arr[mid] < arr[mid+1]` the right test?
> If `mid` is *smaller* than the next, the peak must be at or to the right of `mid+1` (still rising). If `arr[mid] > arr[mid+1]`, the peak is at or to the left.

## Related

- Next: [[06-Graphs, BFS/DFS & Toposort]] — graphs unlock a whole new dimension of the problem space.
- Back to the index: [[LeetCode - Map of Content]].
- Backtracking patterns (`path[:]` snapshot, "pick / recurse / undo") are the skeleton of DP too — see [[08-Dynamic Programming]].
