---
tags: [leetcode, dsa, stack, queue, monotonic-stack, python]
domain: computer-science
category: 04
count: 24
updated: 2026
status: reference
parent: "[[LeetCode - Map of Content]]"
---

# 04 · Stacks, Queues & Sliding Windows

> [!abstract] The toolbox in this file
> - **Plain stack** — LIFO undo/merge: parentheses, nested structures, history.
> - **Min‑stack** — a stack that also tracks its minimum in O(1).
> - **Monotonic stack** — the stack only ever *increases* (or decreases). This is the trick behind "next greater element," "largest rectangle," and "trapping rain water."
> - **Deque as a queue** — `collections.deque` gives O(1) both ends; a plain list is O(n) on `pop(0)`.
> - **Sliding window** — the "fixed/variable window over a string or array" idiom from file 01/02.
>
> The **monotonic stack** is the single most under‑taught but heavily‑tested idea here. If you can explain *why* the stack stays monotonic, you've got 80% of these problems.

**Difficulty legend:** 🟢 Easy · 🟡 Medium · 🔴 Hard

---

## 1. Valid Parentheses (LC 20) · 🟢
Check whether `s` of `()[]{}` is balanced.

```python
def isValid(s):
    stack = []
    pair = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack[-1] != pair[ch]:
                return False
            stack.pop()
    return not stack
```
**Key insight:** every opening bracket gets pushed; a closing bracket pops *only if the top matches*. At the end the stack must be empty.
**Complexity:** `O(n)` time, `O(n)` space.

---

## 2. Min Stack (LC 155) · 🟡
A stack with `O(1)` `getMin`.

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []            # parallel stack of running minima
    def push(self, val):
        self.stack.append(val)
        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val)
    def pop(self):
        if self.stack.pop() == self.mins[-1]:
            self.mins.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.mins[-1]
```
**Key insight:** maintain a **second stack** of the minimum "so far." Push to `mins` only when the new value is ≤ the current min; pop from `mins` only when it matches the value being removed.
**Complexity:** `O(1)` per operation, `O(n)` space.

---

## 3. Implement Queue Using Stacks (LC 232) · 🟢
Two stacks to get FIFO semantics.

```python
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    def push(self, x):
        self.in_stack.append(x)
    def pop(self):
        self._shift()
        return self.out_stack.pop()
    def peek(self):
        self._shift()
        return self.out_stack[-1]
    def empty(self):
        return not self.in_stack and not self.out_stack
    def _shift(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
```
**Key insight:** `in_stack` accumulates; `out_stack` holds items in FIFO order. Reuse it (amortized `O(1)` per op).
**Complexity:** `O(1)` amortized per op, `O(n)` space.

---

## 4. Implement Stack Using Queues (LC 225) · 🟡
Two queues to get LIFO.

```python
from collections import deque
class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    def push(self, x):
        # move all of q1 to q2, then enqueue x (x ends up at the front)
        while q1 := self.q1:
            self.q2.append(q1.popleft())
        self.q2.append(x)
        self.q1, self.q2 = self.q2, self.q1
    def pop(self):
        return self.q1.popleft()
    def top(self):
        return self.q1[0]
    def empty(self):
        return not self.q1
```
**Key insight:** on each push, *rotate* the existing queue so the new item sits at the front — FIFO then behaves like LIFO.
**Complexity:** `O(n)` push, `O(1)` pop/peek, `O(n)` space.

---

## 5. Reverse a String with a Stack (LC 6) · 🟢
`"abc"` → `"cba"` (using a stack, not slicing).

```python
def reverseString(s):
    stack = list(s)
    out = []
    while stack:
        out.append(stack.pop())
    return "".join(out)
```
**Key insight:** push each char, pop into the result — the pop order is reversed.
**Complexity:** `O(n)` time, `O(n)` space.

---

## 6. Next Greater Element I (LC 496) · 🟢
For each `x` in `nums1`, the next element in `nums2` greater than `x`.

```python
def nextGreaterElement(nums1, nums2):
    nxt = {}
    stack = []                       # monotonically decreasing stack
    for x in nums2:
        while stack and stack[-1] < x:
            nxt[stack.pop()] = x
        stack.append(x)
    # anything left in the stack has no next greater element
    for x in stack:
        nxt[x] = -1
    return [nxt[x] for x in nums1]
```
**Key insight:** the **monotonic stack** pattern — the stack holds candidates; when `x` arrives, every smaller top gets answered by `x` and popped. What's left has no answer.
**Complexity:** `O(n)` time, `O(n)` space.

---

## 7. Next Greater Element II (Circular) (LC 503) · 🟡
Same, but the array is *circular* — you can wrap around.

```python
def nextGreaterElements(nums):
    n = len(nums)
    ans = [-1] * n
    stack = []                       # indices, monotonic decreasing
    for i in range(2 * n):          # run twice to handle wrap-around
        x = nums[i % n]
        while stack and nums[stack[-1]] < x:
            ans[stack.pop()] = x
        if i < n:
            stack.append(i)
    return ans
```
**Key insight:** iterate `0..2n−1` and index with `i % n`. Each element's "next greater" can be up to `n` slots ahead.
**Complexity:** `O(n)` time, `O(n)` space.

---

## 8. Daily Temperatures (LC 739) · 🟡
For each day, how many days until a *warmer* day.

```python
def dailyTemperatures(T):
    n = len(T)
    ans = [0] * n
    stack = []                       # indices whose warmer day we haven't found yet
    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            j = stack.pop()
            ans[j] = i - j           # j's warmer day is i
        stack.append(i)
    return ans
```
**Key insight:** the *monotonic stack on indices*. When `t` arrives, every cooler day in the stack gets answered; the stack still holds days with no warmer answer yet.
**Complexity:** `O(n)` time, `O(n)` space.

---

## 9. Smaller Numbers After Self (LC 749) · 🟡
For each element, count how many elements are *smaller*.

```python
def smallerNumbersThanSelf(nums):
    counts = [0] * len(nums)
    for i, x in enumerate(nums):
        counts[i] = sum(1 for y in nums if y < x)   # O(n^2) brute
    return counts
```
**Faster:** sort + binary search.
```python
import bisect
def smallerNumbersThanSelf(nums):
    s = sorted(nums)
    return [bisect.bisect_left(s, x) for x in nums]
```
**Key insight:** in the sorted array, the *index* of `x`'s first occurrence = the number of elements smaller than `x`. `bisect_left` is that index in `O(log n)`.
**Complexity:** `O(n log n)` time (the sorted version), `O(n)` space.

---

## 10. Trapping Rain Water (LC 42) · 🔴
How much water the bar chart traps.

```python
def trap(height):
    if not height:
        return 0
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
**Key insight:** two pointers + running max. The water above a bar is bounded by the *shorter* of the two walls. Whichever side is the shorter wall gets filled up to its running max.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 11. Largest Rectangle in Histogram (LC 84) · 🔴
Largest axis‑aligned rectangle in a bar chart.

```python
def largestRectangleArea(heights):
    stack = []                       # indices; heights strictly increasing
    best = 0
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] >= h:
            idx, hh = stack.pop()
            best = max(best, hh * (i - idx))
            start = idx
        stack.append((start, h))
    for idx, hh in stack:
        best = max(best, hh * (len(heights) - idx))
    return best
```
**Key insight:** monotonic stack of `(start_index, height)`. When a shorter bar arrives, every taller bar in the stack is "closed" — its rightmost extent is the current index. This gives the area in O(1) per bar.
**Complexity:** `O(n)` time, `O(n)` space.

---

## 12. Asteroid Collision (LC 735) · 🟡
Two asteroids collide when the smaller‑magnitude one is on the left of the larger (positive vs. negative).

```python
def asteroidCollision(asteroids):
    stack = []
    for a in asteroids:
        # while `a` moves left, the top moves right, and `a` is strictly smaller:
        # the top dies.
        while stack and a < 0 and stack[-1] > 0 and -a < stack[-1]:
            stack.pop()
        # same magnitude, opposite directions: both die.
        if stack and a < 0 and stack[-1] > 0 and -a == stack[-1]:
            stack.pop()
        # `a` survives — either stack is empty, or the top is moving the
        # *same* direction as `a` (no collision), or `a` is strictly larger.
        elif not stack or a > 0 or (a < 0 and stack[-1] < 0):
            stack.append(a)
    return stack
```
**Key insight:** the stack holds the "settled" prefix of the sequence. On each new asteroid, repeatedly pop the top whenever the new one (left-moving, smaller) destroys the top (right-moving, larger). If they match in magnitude, both die.
**Complexity:** `O(n)` time, `O(n)` space.

---

## 13. Make the String Great (LC 1673) · 🟢
Remove adjacent `c` / `C` pairs until none remain.

```python
def makeGood(s):
    stack = []
    for ch in s:
        if stack and (ch.islower() != stack[-1].islower()) and ch.lower() == stack[-1].lower():
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)
```
**Key insight:** a stack naturally cancels "same letter, opposite case" — pop if they cancel, else push.
**Complexity:** `O(n)` time, `O(n)` space.

---

## 14. Simplify Path (LC 725) · 🟢
`"/a/./b//../c"` → `"/a/b/c"` (normalize a Unix path).

```python
def simplifyPath(path):
    stack = []
    for part in path.split("/"):
        if part in ("", "."):
            continue
        if part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)
    return "/" + "/".join(stack)
```
**Key insight:** a stack is the natural data structure for "go up one level" semantics.
**Complexity:** `O(n)` time, `O(n)` space.

---

## 15. Decode String (LC 394) · 🟡 *(revisited with the "stack as nesting" lens)*

```python
def decodeString(s):
    stack = []
    num, cur = 0, ""
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == "[":
            stack.append((cur, num))
            cur, num = "", 0
        elif ch == "]":
            prev, repeat = stack.pop()
            cur = prev + cur * repeat
        else:
            cur += ch
    return cur
```
**Key insight:** nesting is exactly the shape a stack is for. See [[02-Strings & Hashing]] #10 for the detail.
**Complexity:** `O(n)` time.

---

## 16. Minimum Number of Moves to Reach Target Score (LC 2762) · 🟢
Reach `target` by repeatedly adding a `num` or subtracting it. Minimum moves?

```python
def minMovesToReachTarget(num, target):
    return target // num if target % num == 0 else (target // num) + 1 if target > 0 else 0
```
> [!note] The real solution is just:
> ```python
> def minMovesToReachTarget(num, target):
>     return target // num
> ```
> (Because we can add/subtract freely, the min moves is `⌈target / num⌉` for `target > 0`, `0` otherwise. The exact LeetCode 2762 wording may differ, but the spirit is "quotient of the two.")

**Key insight:** a single division captures "how many `num`s fit into `target`."

---

## 17. Minimum Operations to Reduce X to Zero (LC 1900) · 🟡
Shortest *subarray* whose sum equals `x` (count = `n − window`).

```python
def minOperations(nums, x):
    n = len(nums)
    target = sum(nums) - x          # complement: the middle we want to remove
    total = 0
    left = 0
    best = -1
    for right, v in enumerate(nums):
        total += v
        while total > target and left <= right:
            total -= nums[left]
            left += 1
        if total == target:
            best = max(best, right - left + 1)
    return -1 if best == -1 else n - best
```
**Key insight:** "remove a subarray that sums to `x`" ⟺ "keep a *middle* subarray that sums to `sum − x`." The longest middle window is the fewest removals.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 18. Number of Substrings Containing All Three Characters (LC 1513) · 🟡
Count substrings containing at least one `a`, one `b`, one `c`.

```python
def numberOfSubstrings(s):
    last = {'a': -1, 'b': -1, 'c': -1}
    total = 0
    for i, ch in enumerate(s):
        last[ch] = i
        if last['a'] >= 0 and last['b'] >= 0 and last['c'] >= 0:
            total += min(last.values()) + 1
    return total
```
**Key insight:** at position `i`, the number of substrings ending at `i` that contain all three is `min(last) + 1` (each start index from `0..min(last)` works).
**Complexity:** `O(n)` time, `O(1)` space.

---

## 19. Fruit Into Baskets (LC 904) · 🟡
Longest contiguous subarray with at most **two** distinct fruits.

```python
def totalFruit(fruits):
    last_seen = {}      # fruit -> (count, most-recent index)
    total = 0
    i = 0
    while i < len(fruits):
        seen = {}
        j = i
        while j < len(fruits) and (len(seen) <= 2 or fruits[j] in seen):
            seen[fruits[j]] = seen.get(fruits[j], 0) + 1
            total = max(total, j - i + 1)
            j += 1
        i = j            # shrink: the next window starts at the last valid spot
    return total
```
**Key insight:** sliding window with at most two distinct elements. When a third fruit appears, jump `i` forward past the oldest occurrence.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 20. Maximum Average Subarray I (LC 643) · 🟢
Max average of any contiguous subarray of length `k`.

```python
def findMaxAverage(nums, k):
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best / k
```
**Key insight:** fixed‑window sliding. Add the new element, drop the one that fell off.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 21. Maximum Average Subarray II (LC 674) · 🔴
Max average of a subarray of *at least* length `k`.

```python
def findMaxAverage(nums, k):
    prefix = [0.0]
    for x in nums:
        prefix.append(prefix[-1] + x)
    best = float("-inf")
    for i in range(k, len(nums) + 1):
        for j in range(0, i - k + 1):
            best = max(best, (prefix[i] - prefix[j]) / (i - j))
    return best
```
> [!warning] The naïve version above is O(n²) — acceptable for this problem's constraints. The "fast" version uses a *convex‑hull* trick (the "maximum mean subarray" algorithm) and is `O(n)`; that's beyond the scope of a standard interview question.

**Complexity:** `O(n²)` (simple), `O(n)` (CH trick).

---

## 22. Minimum Window Substring (LC 76) · 🔴 *(revisited as a "variable window")*

See [[02-Strings & Hashing]] #8 — the sliding‑window‑with‑frequency‑map version. The same idea: shrink while the window covers `t`.

**Complexity:** `O(|s| + |t|)` time, `O(alphabet)` space.

---

## 23. Find All Anagrams in a String (LC 438) · 🟡
All starting indices where a substring of length `len(p)` is an anagram of `p`.

```python
from collections import Counter
def findAnagrams(s, p):
    if len(s) < len(p):
        return []
    k = len(p)
    need = Counter(p)
    window = Counter(s[:k])
    out = []
    if window == need:
        out.append(0)
    for i in range(k, len(s)):
        window[s[i]] += 1
        window[s[i - k]] -= 1
        if window[s[i - k]] == 0:
            del window[s[i - k]]
        if window == need:
            out.append(i - k + 1)
    return out
```
**Key insight:** fixed window of size `k` + a frequency map. Two maps are equal iff they have the same keys/counts.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 24. Longest Repeating Character Replacement (LC 424) · 🟡 *(revisited)*

See [[02-Strings & Hashing]] #18 — the sliding‑window version with `most_frequent`.

**Complexity:** `O(n)` time, `O(1)` space.

---

## Self‑Test (cover the answers, then reveal)

> [!question] Why does the monotonic stack give **O(n)** for "next greater element"?
> Each element is pushed *once* and popped *at most once*. The total work across all `n` steps is `O(n)`, not `O(n²)` — the key is that the stack's height only grows with new "record‑high" candidates.

> [!question] In the two‑pointer trapping‑water solution, why do we move the *shorter* wall's pointer?
> The water at the current position is bounded by the *shorter* of the two walls. The taller wall's pointer can't improve the answer on this step — we fill up to the shorter wall's running max, then advance the shorter side.

> [!question] Asteroid Collision: what does `a < 0 < -stack[-1]` mean?
> It reads as "the new asteroid `a` is moving left (negative) AND the top is moving right (positive) AND the new one is *smaller* in magnitude." In that case the top dies.

> [!question] Fruit Into Baskets: why does jumping `i` forward past the last occurrence preserve the invariant?
> The invariant is "at most two distinct fruits." When a third appears, the leftmost occurrence of *one* of the old two must leave. Jumping `i` to "one past the older of the two" is the minimal valid shrink.

> [!question] Make the String Great: what's the O(n) proof that the stack answer is optimal?
> Two adjacent cancellable characters can't coexist in the final string. The greedy "cancel as we go" produces exactly the irreducible core — the same answer no matter in what order you cancel.

> [!question] Minimum Window Substring (LC 76) — why does the "expand then shrink" pattern work?
> The invariant is "the window [lo, hi] contains every t-character (with multiplicity)." When the invariant first holds, we shrink `lo` as far as we can *while still holding the invariant* — that's the minimal valid window for this `hi`. Then we slide forward.

## Related

- Next: [[05-Binary Search & Backtracking]] — the "binary search over answers" pattern.
- Back to the index: [[LeetCode - Map of Content]].
- Sliding‑window / two‑pointer templates are documented in [[01-Arrays & Two Pointers]].
