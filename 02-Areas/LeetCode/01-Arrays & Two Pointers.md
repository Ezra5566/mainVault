---
tags: [leetcode, dsa, arrays, two-pointers, python]
domain: computer-science
category: 01
count: 26
updated: 2026
status: reference
parent: "[[LeetCode - Map of Content]]"
---

# 01 · Arrays & Two Pointers

> [!abstract] The toolbox in this file
> - **Two pointers:** one from each end, or one slow + one fast, to replace an `O(n²)` nested loop with `O(n)`.
> - **Prefix sums:** turn "sum of a subarray" from `O(n)` into `O(1)` after a `O(n)` build.
> - **In‑place / rotation:** swap in the array itself, no extra `O(n)` space.
> - **Fenwick / running‑sum:** maintain a cumulative value as you scan.
>
> If a problem says "subarray" + "sum/product/minimum," reach for these three tools *before* nesting loops.

**Difficulty legend:** 🟢 Easy · 🟡 Medium · 🔴 Hard

---

## 1. Two Sum (LC 1) · 🟢
**Given** `nums` and a `target`, return the *indices* of the two numbers that add to `target` (exactly one solution).

```python
def twoSum(nums, target):
    seen = {}                      # value -> index we've passed
    for i, x in enumerate(nums):
        need = target - x          # if `need` is already in seen, we're done
        if need in seen:
            return [seen[need], i]
        seen[x] = i
```
**Key insight:** don't check every pair (`O(n²)`). As you scan, ask "has the *complement* `target−x` appeared before?" — that's an `O(1)` dict lookup. This is the canonical **hash‑map** template.
**Complexity:** `O(n)` time, `O(n)` space.

---

## 2. Remove Duplicates from Sorted Array (LC 26) · 🟢
Sorted array; remove in‑place so duplicates are gone. Return the count.

```python
def removeDuplicates(nums):
    if not nums:
        return 0
    write = 1                       # next slot for a NEW value
    for x in nums[1:]:
        if x != nums[write - 1]:    # differs from last unique value
            nums[write] = x
            write += 1
    return write
```
**Key insight:** two pointers — `write` only advances when we find a value that differs from the last one we kept. The array stays sorted and unique in the first `write` slots.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 3. Remove Element (LC 27) · 🟢
Remove every occurrence of `val`, return the new length (in‑place).

```python
def removeElement(nums, val):
    write = 0
    for x in nums:
        if x != val:
            nums[write] = x
            write += 1
    return write
```
**Key insight:** same "slow/fast pointer" move — copy every kept element to the left.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 4. Search Insert Position (LC 35) · 🟢
In a sorted array, return the index of `target`, or where it *would* be inserted (first index `>= target`).

```python
def searchInsert(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:                  # classic lower-bound binary search
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
```
**Key insight:** "insert position" = **lower bound** = `bisect_left` territory. `lo` ends at the first position that's `>= target`.
**Complexity:** `O(log n)` time, `O(1)` space.

---

## 5. Plus One (LC 66) · 🟢
Digits of a number as a list; add 1 and return the new digit list.

```python
def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += 1
        if digits[i] < 10:          # no carry -> done
            return digits
        digits[i] = 0               # carry: 9 became 0
    return [1] + digits             # carry overflowed past the front
```
**Key insight:** scan right‑to‑left; a `9` becomes `0` and carries. If every digit was `9`, the answer is `1` followed by zeros.
**Complexity:** `O(n)` time, `O(1)` (ignoring the new leading slot).

---

## 6. Climbing Stairs (LC 70) · 🟢
Ways to climb `n` stairs taking 1 or 2 at a time — this is Fibonacci.

```python
def climbStairs(n):
    a, b = 1, 1                     # ways(0)=1, ways(1)=1
    for _ in range(n):
        a, b = b, a + b
    return a
```
**Key insight:** `ways(n) = ways(n-1) + ways(n-2)`; keep just the last two values (`O(1)` space instead of a full DP array).
**Complexity:** `O(n)` time, `O(1)` space.

---

## 7. Merge Sorted Array (LC 88) · 🟢
Merge `nums2` into `nums1` (which has `k` trailing slots). `nums1` and `nums2` are both sorted.

```python
def merge(nums1, m, nums2, n):
    p1, p2, tail = m - 1, n - 1, m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[tail] = nums1[p1]; p1 -= 1
        else:
            nums1[tail] = nums2[p2]; p2 -= 1
        tail -= 1
    # any leftovers in nums2 still need copying (nums1 leftovers already in place)
    while p2 >= 0:
        nums1[tail] = nums2[p2]; p2 -= 1; tail -= 1
```
**Key insight:** merge **from the back** so we never clobber `nums1`'s still‑to‑be‑used left side. Fill `tail` downward.
**Complexity:** `O(m+n)` time, `O(1)` space.

---

## 8. Best Time to Buy and Sell Stock (LC 121) · 🟢
Max profit from one buy‑then‑sell. Sell must be after buy.

```python
def maxProfit(prices):
    low = float("inf")
    best = 0
    for p in prices:
        low = min(low, p)          # cheapest so far
        best = max(best, p - low)  # best profit if I sell today
    return best
```
**Key insight:** at each day, the best sell‑here assumes you *bought* at the cheapest prior price. One pass, two scalars.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 9. Two Sum II (Sorted Array) (LC 167) · 🟢
Sorted array, return **1‑based** indices of two numbers summing to `target`.

```python
def twoSum2(numbers, target):
    lo, hi = 0, len(numbers) - 1
    while lo < hi:
        s = numbers[lo] + numbers[hi]
        if s == target:
            return [lo + 1, hi + 1]
        if s < target:
            lo += 1                # need a bigger sum -> move left pointer up
        else:
            hi -= 1                # need a smaller sum -> move right pointer down
    return []
```
**Key insight:** because the array is **sorted**, one value being too small means the *left* one should grow — not arbitrary. This is the reason two‑pointers works here; it fails on unsorted arrays.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 10. Majority Element (LC 169) · 🟢
Element appearing more than `n/2` times; return it.

```python
def majorityElement(nums):
    cand, run = None, 0
    for x in nums:
        if run == 0:
            cand, run = x, 1
        elif x == cand:
            run += 1
        else:
            run -= 1
    return cand                    # guaranteed by the > n/2 condition
```
**Key insight:** **Boyer‑Moore** voting — minority elements cancel the majority; whatever survives is the candidate. (The problem guarantees one exists; if you need to be defensive, verify in a second pass.)
**Complexity:** `O(n)` time, `O(1)` space.

---

## 11. Majority Element II (LC 229) · 🟡
Elements appearing more than `n/3` times; return them.

```python
def majorityElement(nums):
    c1 = c2 = 0                    # two candidates + two running counts
    n1 = n2 = None
    for x in nums:
        if x == n1:
            c1 += 1
        elif x == n2:
            c2 += 1
        elif c1 == 0:
            n1, c1 = x, 1
        elif c2 == 0:
            n2, c2 = x, 1
        else:
            c1 -= 1; c2 -= 1
    # verify: count each candidate and keep only those with > n/3
    res = []
    for v in {n1, n2}:
        if v is not None and nums.count(v) > len(nums) / 3:
            res.append(v)
    return res
```
**Key insight:** generalize Boyer‑Moore to `k` slots; you can only have *two* elements that appear more than `1/3` each.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 12. Missing Number (LC 268) · 🟢
Numbers `0..n` with one missing; find it.

```python
def missingNumber(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)   # expected sum - actual
```
**Key insight:** the sum of `0..n` is `n(n+1)/2`. That's a closed form; one pass for the actual sum.
**Alternative:** XOR `i ^ nums[i]` — same idea, no overflow worries.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 13. Reverse String (LC 344) · 🟢
Reverse a character array in‑place.

```python
def reverseString(s):
    i, j = 0, len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1; j -= 1
```
**Key insight:** swap from both ends moving inward. `i < j` (not `<=`) avoids a pointless middle swap when `n` is odd.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 14. Reverse Vowels in a String (LC 345) · 🟢
Reverse only the vowels in a string; keep consonants in place.

```python
def reverseVowels(s):
    vowels = set("aeiouAEIOU")
    lst = list(s)
    i, j = 0, len(lst) - 1
    while i < j:
        while i < j and lst[i] not in vowels:
            i += 1
        while i < j and lst[j] not in vowels:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1; j -= 1
    return "".join(lst)
```
**Key insight:** classic two‑pointer with a *predicate* — pointers skip non‑vowels until they meet a vowel on both sides, then swap.
**Complexity:** `O(n)` time, `O(n)` space for the list.

---

## 15. Subarray Sum Equals K (LC 560) · 🟡
Count subarrays summing to `K`.

```python
def subarraySum(nums, k):
    from collections import defaultdict
    count = defaultdict(int)
    count[0] = 1                    # a subarray starting at index 0
    seen = 0                       # running (prefix) sum
    ans = 0
    for x in nums:
        seen += x
        ans += count[seen - k]      # if prefix(i) - prefix(j) == k, this window qualifies
        count[seen] += 1
    return ans
```
**Key insight:** `sum(a..b) = prefix(b+1) - prefix(a)`. Pre‑compute "how many prefixes have value `v`"; when the running prefix is `s`, windows ending here with sum `k` are those where the prefix *before* was `s−k`.
**Complexity:** `O(n)` time, `O(n)` space (dict of prefix‑sum counts).

---

## 16. Shortest Unordered Continuous Subarray (LC 581) · 🟡
Shortest subarray that, when sorted, sorts the entire array.

```python
def findUnsortedSubarray(nums):
    n = len(nums)
    lo, hi = n, -1
    # right pointer: anything left of it that's smaller than some later element
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] < nums[i]:
                lo = min(lo, i); hi = max(hi, j)
    return 0 if lo > hi else hi - lo + 1
```
The classic **two‑pass** version is `O(n)`:
```python
def findUnsortedSubarray(nums):
    lo, hi, right_min, left_max = len(nums), -1, float("inf"), float("-inf")
    for i in range(len(nums)):
        right_min = min(right_min, nums[i])
        if nums[i] > right_min:
            lo = i
    for i in range(len(nums) - 1, -1, -1):
        left_max = max(left_max, nums[i])
        if nums[i] < left_max:
            hi = i
    return 0 if lo > hi else hi - lo + 1
```
**Key insight:** a broken element at position `i` is either "there's a smaller element to its right" (left‑to‑right scan) or "there's a larger element to its left" (right‑to‑left scan). Take the leftmost `lo` and rightmost `hi` that satisfy.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 17. Duplicate and Missing (LC 645) · 🟡
In `1..n`, exactly one number is duplicated and one is missing. Find both.

```python
def findErrorNums(nums):
    from collections import Counter
    c = Counter(nums)
    dup = miss = 0
    for v in range(1, len(nums) + 1):
        if c[v] == 2:
            dup = v
        elif c[v] == 0:
            miss = v
    return [dup, miss]
```
A **math** version (no dict):
```python
def findErrorNums(nums):
    n = len(nums)
    s1 = sum(nums)
    s2 = sum(x * x for x in nums)
    e = (n * (n + 1) // 2) - s1                # = miss - dup
    d = (n * (n + 1) * (2 * n + 1) // 6) - s2  # = miss^2 - dup^2
    miss_plus_dup = d // e                     # = miss + dup
    dup = (miss_plus_dup - e) // 2
    miss = (miss_plus_dup + e) // 2
    return [dup, miss]
```
**Key insight:** `sum` and `sum of squares` give you two equations in two unknowns; solve for `dup` and `miss` algebraically. `e = miss − dup` and `d = miss² − dup² = (miss−dup)(miss+dup)`, so `miss+dup = d/e`.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 18. Subarray Product Less Than K (LC 713) · 🟡
Count contiguous subarrays with product `< k` (positive ints).

```python
def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0
    prod, left, ans = 1, 0, 0
    for right, x in enumerate(nums):
        prod *= x
        while prod >= k:
            prod //= nums[left]
            left += 1
        ans += right - left + 1   # every subarray ending at `right` with a left in [left, right] works
    return ans
```
**Key insight:** sliding window. Once the product is too big, shrink from the left until it's under `k`. For the current `right`, `right − left + 1` subarrays ending there all satisfy the constraint.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 19. Find Pivot Index (LC 724) · 🟢
Index `i` where `sum(left of i) == sum(right of i)`.

```python
def pivotIndex(nums):
    total = sum(nums)
    left = 0
    for i, x in enumerate(nums):
        if left == total - left - x:
            return i
        left += x
    return -1
```
**Key insight:** keep a running `left` sum; `right = total − left − x`. Compare on the fly.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 20. Reshape Matrix (LC 881) · 🟢
Reshape an `m×n` matrix to `r×c`, or return the original if shape is impossible.

```python
def matrixReshape(mat, r, c):
    m, n = len(mat), len(mat[0])
    if m * n != r * c:
        return mat
    flat = [v for row in mat for v in row]
    return [flat[i*c:(i+1)*c] for i in range(r)]
```
**Key insight:** reshape is literally "flatten then slice into rows."
**Complexity:** `O(mn)` time, `O(mn)` space.

---

## 21. Running Sum of 1‑d Array (LC 1480) · 🟢
Return the prefix sums of an array.

```python
def runningSum(nums):
    out = []
    s = 0
    for x in nums:
        s += x
        out.append(s)
    return out
```
**Key insight:** prefix sums are a *new* array, not in‑place. `O(n)` time, `O(n)` space (the new list).
**Complexity:** `O(n)` time, `O(n)` space.

---

## 22. Find Minimum in Rotated Sorted Array (LC 153) · 🟡
A sorted array was rotated at some unknown pivot. Find the minimum in `O(log n)`.

```python
def findMin(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1          # the min is to the right of mid
        else:
            hi = mid             # mid <= hi, the min is at mid or to its left
    return nums[lo]
```
**Key insight:** binary search, but compare the *middle* with the *right*. If the middle is bigger than the right, the pivot is to the right. No duplicates.
**Complexity:** `O(log n)` time, `O(1)` space.

---

## 23. Rotate Array (LC 189) · 🟡
Rotate `nums` right by `k` steps in‑place.

```python
def rotate(nums, k):
    n = len(nums)
    k %= n
    def rev(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1; r -= 1
    rev(0, n - 1)                # 1. reverse the whole
    rev(0, k - 1)               # 2. reverse the first k
    rev(k, n - 1)               # 3. reverse the rest
```
**Key insight:** the "reverse the whole, then reverse the two pieces" trick. `ab|cd` → `ba|dc` → `cd|ab`.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 24. Minimum Size Subarray Sum (LC 209) · 🟡
Shortest contiguous subarray with sum `>= target` (positive integers).

```python
def minSubArrayLen(s, nums):
    best = float("inf")
    left = 0; total = 0
    for right, x in enumerate(nums):
        total += x
        while total >= s:       # shrink from the left while still >= target
            best = min(best, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if best == float("inf") else best
```
**Key insight:** sliding window. Because all values are positive, the moment `total >= s` we can only *shrink* from the left and improve the window.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 25. Find All Numbers Disappeared in an Array (LC 448) · 🟡
`n` elements in `1..n`; some appear twice, some once. Return the missing ones.

```python
def findDisappearedNumbers(nums):
    for x in nums:
        idx = abs(x) - 1
        nums[idx] = -abs(nums[idx])    # mark index (value-1) as "seen"
    return [i + 1 for i in range(len(nums)) if nums[i] > 0]
```
**Key insight:** **index‑as‑flag** trick. Since values are in `[1..n]`, the value `x` flags position `x−1`. Flip the sign. Anything still positive → that index is missing.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 26. Squared Sorted Array (LC 977) · 🟢
Given a sorted array (may contain negatives), return the squares sorted.

```python
def sortedSquares(nums):
    n = len(nums)
    out = [0] * n
    lo, hi, i = 0, n - 1, n - 1
    while lo <= hi:
        a, b = nums[lo] ** 2, nums[hi] ** 2
        if a > b:
            out[i] = a; lo += 1
        else:
            out[i] = b; hi -= 1
        i -= 1
    return out
```
**Key insight:** the largest square is always at one of the two ends (the one with larger absolute value). Fill `out` from the back, advancing whichever end was bigger.
**Complexity:** `O(n)` time, `O(n)` space.

---

## Self‑Test (cover the answers, then reveal)

> [!question] Two‑pointers on *sorted* arrays works for Two Sum II. Why does it *fail* on unsorted arrays?
> Because the monotonicity that lets us "decide" which pointer to move (left if too small, right if too big) depends on the array being sorted. Unsorted → use a hash map (Two Sum LC 1) instead.

> [!question] What's the time/space of `subarraySum` (LC 560)?
> `O(n)` time, `O(n)` space for the prefix‑sum count dict.

> [!question] Why can LC 209 (min subarray sum) use a sliding window but not every "subarray" problem can?
> Because all elements are **positive**. The invariant "if total ≥ target, we can shrink from the left and keep it valid" fails when there are negatives.

> [!question] Describe the "index‑as‑flag" trick (LC 448).
> Since values are in `[1..n]`, the value `x` tells you which *position* was seen: `nums[x−1]`. Flip the sign of that slot; any slot still positive after the pass is a missing number. `O(1)` space instead of a set.

> [!question] Boyer‑Moore majority element — why does the "survivor" have to be the actual majority?
> Every non‑majority element cancels with a majority element at most `n/2` times (there are strictly more of the majority). Any cancellation leaves strictly more majority. So the survivor is the majority element.

> [!question] Rotated sorted array min (LC 153): why do we compare `nums[mid]` to `nums[hi]` and not `nums[lo]`?
> `nums[mid] > nums[hi]` means the min is in the *right* half (the drop happened before `mid`). If `nums[mid] <= nums[hi]`, the min is at `mid` or to its left. Comparing to `lo` gives ambiguous cases when the rotation crosses `lo`.

## Related

- Next: [[02-Strings & Hashing]] — the hash‑map template returns, plus KMP & Z‑function.
- Back to the index: [[LeetCode - Map of Content]].
- The Python idioms (dict, set, slice, comprehension) are explained in [[05-AI-Research/Deep Dives/Python]].
