---
tags: [leetcode, dsa, greedy, math, design, brainteaser, python]
domain: computer-science
category: 09
count: 22
updated: 2026
status: reference
parent: "[[LeetCode - Map of Content]]"
---

# 09 · Greedy, Math & Data-Structure Design

> [!abstract] The three shapes of problem in this file
> - **Greedy without a proof** — "sort by X, then walk" is the template (jump game, gas station, car pool, task scheduler). Most of these have a clean proof the interviewer may ask for.
> - **Pure math / bit tricks** — `xor`, `modular`, `greatest common divisor`, `two-pointer on digits`. Often the "aha" is one line.
> - **Data-structure design** — implement a class with `O(1)` operations (LRU cache, min-stack, median-finder). These are where Python's built-ins (`OrderedDict`, `heapq`, `defaultdict`) carry you across the finish.
>
> **The single lesson this file teaches:** "the right invariant" beats "the clever algorithm." Once you can *state* what must be true at each step, the code is usually 10 lines.

**Difficulty legend:** 🟢 Easy · 🟡 Medium · 🔴 Hard

---

## 1. Jump Game (LC 55) · 🟡
Can you reach the last index given each cell's jump length?

```python
def canJump(nums):
    reach = 0
    for i, x in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + x)
    return True
```
**Key insight:** track the *farthest* reachable index. If you hit a position you can't reach, you're stuck.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 2. Jump Game II (LC 45) · 🟡
Min jumps to reach the last index.

```python
def jump(nums):
    jumps = 0
    end = 0                 # right boundary of the current "reachable so far"
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == end:        # we've exhausted the current reach
            jumps += 1
            end = farthest
            if end >= len(nums) - 1:
                break
    return jumps
```
**Key insight:** greedy BFS-by-level. Each "jump" advances the right boundary to the farthest reachable so far. The loop runs once — no need to track a full array.
**Complexity:** `O(n)`.

---

## 3. Jump Game III (LC 1345) · 🟢
Start at `start`; can you reach an index with value 0?

```python
def canReach(arr, start):
    seen = set()
    def dfs(i):
        if i < 0 or i >= len(arr) or i in seen or arr[i] < 0:
            return False
        if arr[i] == 0:
            return True
        seen.add(i)
        return dfs(i + arr[i]) or dfs(i - arr[i])
    return dfs(start)
```
**Key insight:** DFS with a `seen` set (negative values indicate already-visited, but the explicit set is clearer).
**Complexity:** `O(n)` time, `O(n)` space.

---

## 4. Gas Station (LC 134) · 🟡
Start with an empty tank; find the index to start so you can complete the loop.

```python
def canCompleteCircuit(gas, cost):
    total = 0
    tank = 0
    start = 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        tank += gas[i] - cost[i]
        if tank < 0:
            tank = 0
            start = i + 1
    return start if total >= 0 else -1
```
**Key insight:** if a prefix is negative, *no* starting point within that prefix works — skip past the end of the negative segment. If the total is non-negative, exactly one answer exists.
**Complexity:** `O(n)`.

---

## 5. Trapping Rain Water (LC 42) · 🔴 *(revisited as pure greedy)*
Two-pointer version (see [[04-Stacks, Queues & Sliding Window]] #10 for the stack version).

```python
def trap(height):
    left, right = 0, len(height) - 1
    l_max, r_max = 0, 0
    water = 0
    while left < right:
        if height[left] <= height[right]:
            if height[left] >= l_max:
                l_max = height[left]
            else:
                water += l_max - height[left]
            left += 1
        else:
            if height[right] >= r_max:
                r_max = height[right]
            else:
                water += r_max - height[right]
            right -= 1
    return water
```
**Complexity:** `O(n)` time, `O(1)` space.

---

## 6. Candy (LC 135) · 🟡
Distribute candies: each child gets ≥ 1, and neighbors of higher rating get more.

```python
def candy(ratings):
    n = len(ratings)
    c = [1] * n
    for i in range(1, n):                    # left → right
        if ratings[i] > ratings[i - 1]:
            c[i] = c[i - 1] + 1
    for i in range(n - 2, -1, -1):           # right → left
        if ratings[i] > ratings[i + 1]:
            c[i] = max(c[i], c[i + 1] + 1)
    return sum(c)
```
**Key insight:** two passes. Pass 1 (L→R) fixes every ascending run. Pass 2 (R→L) fixes every descending run. Take the `max` in pass 2 to keep pass 1's work.
**Complexity:** `O(n)`.

---

## 7. Gas station — *variant*: "min refills" / *Car Pooling* (LC 1286) · 🟡
Can the car fit all riders within its capacity?

```python
def carPooling(trips, capacity):
    # event-based: sort by pickup/dropoff
    events = []
    for start, end, num in trips:
        events.append((start, num))
        events.append((end, -num))
    events.sort()
    running = 0
    for _, delta in events:
        running += delta
        if running > capacity:
            return False
    return True
```
**Key insight:** the sweep-line trick — sort events by location, keep a running passenger count, and check against capacity.
**Complexity:** `O(n log n)`.

---

## 8. Maximum Subarray — *the greedy you know* (LC 53) · 🟡
See [[08-Dynamic Programming]] #2.

---

## 9. Single Number (LC 136) · 🟢
Every number appears twice except one. Find it.

```python
def singleNumber(nums):
    ans = 0
    for x in nums:
        ans ^= x
    return ans
```
**Key insight:** `x ^ x == 0`. Every pair cancels; the lone number survives.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 10. Single Number II (LC 137) · 🟡
Every number appears **three** times except one. Find it.

```python
def singleNumber(nums):
    # bitwise: count each bit's occurrences; take mod 3
    ans = 0
    for bit in range(32):
        count = sum((x >> bit) & 1 for x in nums)
        if count % 3:
            ans |= 1 << bit
    # handle signed numbers (Python ints have arbitrary length, so we'd need to
    # special-case sign extension; LeetCode's inputs fit in 32 bits)
    if ans >= 1 << 31:
        ans -= 1 << 32
    return ans
```
**Key insight:** for each bit position, count how many numbers have that bit set. The bit is set in the "lone" number iff the count is `1 mod 3`.
**Complexity:** `O(32n)` time, `O(1)` space.

---

## 11. Add Binary (LC 67) · 🟢
Already in [[02-Strings & Hashing]] #15.

---

## 12. Power of Two (LC 231) · 🟢
Is `n` a power of 2?

```python
def isPowerOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0
```
**Key insight:** `n & (n-1)` clears the lowest set bit. For a power of two, that's the *only* bit, so the result is 0.
**Complexity:** `O(1)`.

---

## 13. Add Digits (LC 258) · 🟢
Repeatedly sum digits until one digit remains.

```python
def addDigits(num):
    while num >= 10:
        num = sum(int(d) for d in str(num))
    return num
```
> [!tip] The `O(1)` closed form:
> ```python
> def addDigits(num):
>     return num % 9 if num == 0 else 1 + (num - 1) % 9
> ```
> (The **digital root**.)

**Complexity:** `O(log n)` (the digits version), `O(1)` (digital root).

---

## 14. Pow(x, n) (LC 50) · 🟡
Compute `x^n` in `O(log n)`.

```python
def myPow(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / myPow(x, -n)
    half = myPow(x, n // 2)
    return half * half * (x if n % 2 else 1)
```
**Key insight:** **fast exponentiation** — square the half-power. If `n` is odd, multiply by an extra `x`.
**Complexity:** `O(log n)` time, `O(log n)` recursion space.

---

## 15. Reverse Integer (LC 7) · 🟢
Reverse the digits of an integer (handle negatives and overflow).

```python
def reverse(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    out = 0
    while x:
        out = out * 10 + x % 10
        x //= 10
    out *= sign
    # clamp to 32-bit signed range
    return max(-2**31, min(2**31 - 1, out))
```
**Key insight:** read digits from the right (`x % 10`), build the answer by shifting (`out * 10 + digit`). Clamp at the end.
**Complexity:** `O(log |x|)`.

---

## 16. Reverse Bits (LC 190) · 🟢
Reverse the 32-bit binary representation.

```python
def reverseBits(n):
    out = 0
    for _ in range(32):
        out = (out << 1) | (n & 1)
        n >>= 1
    return out
```
**Key insight:** read 1 bit from `n` at a time, shift it into position in `out`. 32 iterations because 32 bits.
**Complexity:** `O(1)` (32 iterations).

---

## 17. Hamming Distance (LC 461) · 🟢
Count the differing bits between two integers.

```python
def hammingDistance(x, y):
    return bin(x ^ y).count("1")
```
**Key insight:** `x ^ y` has a 1 wherever they differ. Count the 1s.
**Complexity:** `O(log max(x,y))`.

---

## 18. Number of 1 Bits (LC 191) · 🟢
Count the 1-bits in a positive integer (also called the "popcount").

```python
def hammingWeight(n):
    return bin(n).count("1")
```
> [!tip] Brian Kernighan's trick:
> ```python
> def hammingWeight(n):
>     count = 0
>     while n:
>         n &= n - 1     # clear the lowest set bit
>         count += 1
>     return count
> ```

**Complexity:** `O(log n)` (bin), `O(number of 1 bits)` (Kernighan).

---

## 19. Rotate Image (LC 48) · 🟡
Rotate a square matrix 90° clockwise in-place.

```python
def rotate(matrix):
    # 90° CW = transpose + reverse each row
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
```
**Key insight:** two operations: transpose (swap `A[i][j]` with `A[j][i]` for `j > i`) and then reverse each row.
**Complexity:** `O(n²)` time, `O(1)` space.

---

## 20. Spiral Order (LC 54) · 🟡
Read the matrix in spiral order.

```python
def spiralOrder(matrix):
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    out = []
    while top <= bottom and left <= right:
        for c in range(left, right + 1):     # top row, left → right
            out.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1):     # right col, top → bottom
            out.append(matrix[r][right])
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1):   # bottom row, right → left
                out.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):    # left col, bottom → top
                out.append(matrix[r][left])
            left += 1
    return out
```
**Key insight:** four moving boundaries. After each "side" traversal, advance that boundary. The `if` guards prevent double-visiting when the matrix shrinks to a single row or column.
**Complexity:** `O(rows·cols)`.

---

## 21. LRU Cache (LC 146) · 🟡
`get`/`put` in `O(1)`.

```python
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.d = OrderedDict()
    def get(self, key):
        if key not in self.d:
            return -1
        self.d.move_to_end(key)      # mark as recently used
        return self.d[key]
    def put(self, key, value):
        if key in self.d:
            self.d.move_to_end(key)
        self.d[key] = value
        if len(self.d) > self.cap:
            self.d.popitem(last=False)   # evict the least-recently-used
```
**Key insight:** `OrderedDict` is Python's built-in LRU — `move_to_end` reorders, `popitem(last=False)` evicts from the front.
**Complexity:** `O(1)` per op.

---

## 22. Design a Stack With Increment Operations (LC 1381) · 🟡
A stack with `push`, `pop`, and "increment the bottom K."

```python
class MyStack:
    def __init__(self):
        self.s = []
        self.inc = []           # pending increments
    def push(self, x):
        self.s.append(x + (self.inc[-1] if self.inc else 0))
    def pop(self):
        if not self.s:
            return -1
        v = self.s.pop()
        if self.inc and self.inc[-1]:
            if len(self.s) < len(self.inc):
                # apply the "leaked" part of this inc to the rest
                for i in range(len(self.inc)):
                    self.inc[i] += v - self.inc[i]
                self.inc = []
        elif self.inc:
            self.inc.pop()
        return v
    def increment(self, k, val):
        if k >= len(self.s):
            # applies to the whole stack
            if not self.inc:
                self.inc.append(val)
            else:
                for i in range(len(self.inc)):
                    self.inc[i] += val
        else:
            self.inc.insert(0, val * k)
```
> [!note] The clean version:
> ```python
> class MyStack:
>     def __init__(self):
>         self.s = []
>         self.inc = [0]
>     def push(self, x):
>         self.s.append(x + self.inc[-1])
>         self.inc.append(self.inc[-1])
>     def pop(self):
>         if not self.s:
>             return -1
>         v = self.s.pop()
>         self.inc.pop()
>         return v
>     def increment(self, k, val):
>         self.inc[min(k, len(self.s))] += val
> ```
> The idea: `inc[i]` accumulates the "total increment that should apply to position i and below."

**Complexity:** `O(1)` per op.

---

## 23. Number of Segments in a String (LC 434) · 🟢
Count the segments separated by spaces.

```python
def countSegments(s):
    return len(s.split())
```
**Key insight:** Python's `str.split()` (no args) splits on *any whitespace* and collapses runs. `str.split(" ")` doesn't.
**Complexity:** `O(n)`.

---

## 24. Reverse Words in a String (LC 151) · 🟡
Reverse the order of words and strip extra spaces.

```python
def reverseWords(s):
    return " ".join(s.split()[::-1])
```
**Key insight:** `split()` handles multi-space collapsing; `[::-1]` reverses the word list; `" ".join` puts them back together with single spaces.
**Complexity:** `O(n)`.

---

## Self-Test (cover the answers, then reveal)

> [!question] Jump Game II: why do we update `jumps` *when `i == end`*, not when `farthest` advances?
> Because "the number of jumps" is the count of *levels*. Each jump extends the level boundary (`end`) to the current `farthest`. We only count a jump when we've exhausted the current level.

> [!question] Gas Station: why does "total ≥ 0" guarantee a unique answer?
> If the total is non-negative, the gas consumed on the full loop is affordable. The greedy "restart after any negative prefix" finds the unique starting point where the running tank never dips below zero.

> [!question] Candy (LC 135): why *two* passes (L→R and R→L)?
> One pass (L→R) only handles "higher rating than the left neighbor." Descending runs go the other way. A second pass (R→L) catches those. Taking `max(c[i], c[i+1] + 1)` keeps the L→R work from being overwritten.

> [!question] Power of Two: why does `n & (n-1) == 0` work?
> Subtracting 1 from a number flips its lowest set bit (and all lower bits). For a power of two, the lowest set bit *is* the only one, so `n-1` has its complement in that position — `n & (n-1)` clears it to 0.

> [!question] Rotate Image (LC 48): why transpose + reverse, not "rotate in one step"?
> Transpose + reverse is *two independent O(n²) operations* with a simple proof: a transpose flips the main diagonal, and reversing each row flips each row. The composition is a 90° CW rotation. A "one-step" rotation requires tracking 4 cells at a time and is more error-prone.

> [!question] LRU Cache: why is `OrderedDict` the right data structure?
> It's a dict *plus* an insertion-order guarantee. `move_to_end` is `O(1)` (relink), `popitem(last=False)` is `O(1)` (remove the head). A plain dict loses order (until Python 3.7+, where insertion order is preserved but there's no efficient "move to end").

> [!question] Digital root (LC 258): why `1 + (num-1) % 9`?
> A number's digital root equals `num mod 9`, except that multiples of 9 are 9, not 0. The formula `1 + (num-1) % 9` collapses the "9 ≡ 0" corner case (it gives 9 when `num` is a positive multiple of 9, and `num % 9` otherwise). For `num == 0`, the answer is 0.

## Related

- Back to the index: [[LeetCode - Map of Content]].
- **All 9 files cover:** arrays, strings, trees, stacks, binary search, graphs, heaps, DP, and design. If you get all of these, you've covered ~90% of standard interview content.
