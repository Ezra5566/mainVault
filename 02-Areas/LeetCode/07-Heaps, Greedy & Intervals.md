---
tags: [leetcode, dsa, heap, greedy, intervals, heapq, python]
domain: computer-science
category: 07
count: 20
updated: 2026
status: reference
parent: "[[LeetCode - Map of Content]]"
---

# 07 · Heaps, Greedy & Intervals

> [!abstract] The toolbox in this file
> - **Min‑heap** via `heapq` — Python's *only* built‑in heap. Max‑heap = push negated values.
> - **Top‑K** — "K largest/smallest" is always "min‑heap of size K" (or `heapq.nlargest`).
> - **Lazy deletion** — push, mark‑dead, skip on pop (used in median‑of‑stream, "find the Kth smallest").
> - **Greedy** — "always pick the locally best move" is provably optimal on interval scheduling, minimum‑cost, merge tasks.
> - **Sweep line** — sort events by x, process left‑to‑right. The interval‑overlap family all uses it.
>
> The single most useful Python idiom here: `heapq` is a **min‑heap**, so a *max*‑heap is `heapq` on `(-value, id)`.

**Difficulty legend:** 🟢 Easy · 🟡 Medium · 🔴 Hard

---

## 1. Kth Largest Element in an Array (LC 215) · 🟡
Find the k‑th largest value.

```python
import heapq
def findKthLargest(nums, k):
    # Approach 1: min-heap of size k (keeps the k largest seen so far)
    h = []
    for x in nums:
        if len(h) < k:
            heapq.heappush(h, x)
        elif x > h[0]:
            heapq.heapreplace(h, x)      # push x and pop the root in one step
    return h[0]
```
> [!tip] There are three good answers:
> 1. **Heap of size k** above: `O(n log k)`.
> 2. **`heapq.nlargest(k, nums)[k-1]`**: `O(n log k)` but C‑speed.
> 3. **Quickselect** (randomized partition): `O(n)` expected. The interview "wow" answer.

**Complexity:** `O(n log k)` with the heap.

---

## 2. Top K Frequent Elements (LC 347) · 🟡
The k most frequent elements.

```python
import heapq
from collections import Counter
def topKFrequent(nums, k):
    c = Counter(nums)
    # min-heap over (count, value) — the "k most frequent" are the k tops
    h = []
    for val, cnt in c.items():
        heapq.heappush(h, (cnt, val))
        if len(h) > k:
            heapq.heappop(h)
    return [v for _, v in h]
```
**Key insight:** a min‑heap of size `k` over `(count, value)` keeps only the `k` highest counts. Alternatively, `Counter.most_common(k)` does it in one line.
**Complexity:** `O(n + u log k)` where `u` = number of unique values.

---

## 3. Merge k Sorted Lists (LC 23) · 🔴
Merge `k` sorted lists into one.

```python
import heapq
def mergeKLists(lists):
    # push (val, list_index, element_index); compare by val only
    pq = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(pq, (lst[0].val, i, 0))
    dummy = Node(0)
    cur = dummy
    while pq:
        val, i, j = heapq.heappop(pq)
        cur.next = lists[i][j]
        cur = cur.next
        if j + 1 < len(lists[i]):
            heapq.heappush(pq, (lists[i][j + 1].val, i, j + 1))
    return dummy.next
```
**Key insight:** put the *head* of each list in the heap. Pop the smallest, push its successor. The heap always holds one candidate per list. The `(val, i, j)` tuple avoids comparing `ListNode`s (which Python can't order).
**Complexity:** `O(N log k)` where `N` = total number of nodes.

---

## 4. K Closest Points to Origin (LC 973) · 🟡
The k closest points (by squared distance).

```python
import heapq
def kClosest(points, k):
    # max-heap (negated) of the k closest so far; root is the kth-closest
    h = [(-p[0] * p[0] - p[1] * p[1], p) for p in points[:k]]
    heapq.heapify(h)
    for p in points[k:]:
        dist = -(p[0] * p[0] + p[1] * p[1])
        if dist > h[0][0]:                # p is closer than the current worst
            heapq.heapreplace(h, (dist, p))
    return [p for _, p in h]
```
**Key insight:** a **max‑heap of size k** over the (negated) squared distance. The root is the k‑th closest; anything more distant gets discarded. Negating is the Python "max‑heap" trick.
**Complexity:** `O(n log k)`.

---

## 5. Task Scheduler (LC 621) · 🟡
Minimum time to finish tasks with a cooldown `n` between identical tasks.

```python
def leastInterval(tasks, n):
    from collections import Counter
    c = Counter(tasks)
    max_cnt = max(c.values())                       # how many copies of the most frequent
    n_max = sum(1 for v in c.values() if v == max_cnt)   # how many tasks share that count
    # The most frequent task(s) dominate: each "block" takes n slots
    # The last block only needs `n_max` slots (no cooldown after the last)
    return max(len(tasks), (max_cnt - 1) * (n + 1) + n_max)
```
**Key insight:** **greedy counting**. The bottleneck is the most‑frequent task. If it appears `max_cnt` times, it creates `max_cnt − 1` full "cooldown blocks" of length `n + 1`, plus one final block of `n_max` tasks. Compare with "just do them all" (`len(tasks)`).
**Complexity:** `O(n)` time.

---

## 6. Min Cost to Hire K Workers (LC 857) · 🔴
Hire exactly `k` workers with minimum total cost, respecting `quality_i` and `wage_i` ratios.

```python
import heapq
def mincostToHireWorkers(quality, wage, k):
    # Sort by wage/quality ratio. Iterating in this order, when we've selected `k`
    # workers, the *current* worker has the largest ratio — so every selected worker's
    # wage is "capped" at ratio_current * quality, and the total cost is
    #     ratio_current * sum(qualities)
    workers = sorted(zip(wage, quality), key=lambda wq: wq[0] / wq[1])
    q_heap = []        # max-heap of qualities (stored negated)
    q_sum = 0
    ans = float("inf")
    for w, q in workers:
        heapq.heappush(q_heap, -q)
        q_sum += q
        if len(q_heap) > k:                 # keep only k; drop the largest quality
            q_sum += heapq.heappop(q_heap)   # pop is negative, so this subtracts
        if len(q_heap) == k:
            ans = min(ans, q_sum * (w / q))  # current worker is the "priciest" one
    return ans
```
**Key insight:** iterate workers in *increasing* `wage/quality` ratio. At each step the running `k`-worker group's cost is `current_ratio × Σqualities`; the max‑heap drops the largest quality so we always keep the cheapest `k`. `q_sum += heapq.heappop(q_heap)` (the pop is negated) correctly *subtracts* the dropped quality.
**Complexity:** `O(n log n)` (sort) + `O(n log k)` (heap).

---

## 7. Median of a Data Stream (LC 295) · 🟡
A stream; answer "the median so far" online.

```python
import heapq
class MedianFinder:
    def __init__(self):
        self.small = []    # max-heap of the LOWER half (negated)
        self.large = []    # min-heap of the UPPER half
    def addNum(self, num):
        # keep `small` <= `large` and sizes differ by at most 1
        heapq.heappush(self.small, -num)
        if self.small and self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
```
**Key insight:** two heaps, the top of each is the median (or the two middle values). Keeping `small` (max‑heap, negated) at most one bigger than `large` gives `O(1)` median.
**Complexity:** `O(log n)` per `addNum`, `O(1)` per `findMedian`.

---

## 8. Reorganize String (LC 791) · 🟡
Already in [[02-Strings & Hashing]] #24 — the **max‑heap of frequencies** pattern. See there.

---

## 9. Find K Pairs with Smallest Sums (LC 373) · 🟡
The `k` smallest‑sum pairs from two sorted arrays.

```python
import heapq
def kSmallestPairs(nums1, nums2, k):
    h = [(nums1[0] + nums2[0], 0, 0)]
    out = []
    seen = set()
    while h and len(out) < k:
        s, i, j = heapq.heappop(h)
        out.append([nums1[i], nums2[j]])
        # the next two candidates: advance i or j (but not both, to avoid dupes)
        if i + 1 < len(nums1):
            heapq.heappush(h, (nums1[i + 1] + nums2[j], i + 1, j))
        if j + 1 < len(nums2):
            heapq.heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
    return out
```
**Key insight:** start from `(0,0)`; each popped pair can extend by `i+1` or `j+1`. The "seen" set prevents revisiting `(i+1, j+1)` from two paths.
**Complexity:** `O(k log k)`.

---

## 10. Find the Duplicate Number (LC 287) · 🟡
Find the duplicate in `n + 1` numbers in `1..n` without modifying the array.

```python
def findDuplicate(nums):
    # Floyd's cycle detection (tortoise and hare) — treat nums[i] as the "next" pointer
    slow = nums[0]
    fast = nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    # find the entry point of the cycle
    p1 = 0
    p2 = slow
    while p1 != p2:
        p1 = nums[p1]
        p2 = nums[p2]
    return p1
```
**Key insight:** the `nums[i] → nums[nums[i]]` walk forms a *cycle* that starts at the duplicate (Floyd's theorem). No hash, no mutation, `O(n)` time.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 11. Meeting Rooms (LC 252) · 🟢
No two meetings overlap.

```python
def canAttendMeetings(intervals):
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True
```
**Key insight:** sort by start; each meeting must start *after* the previous one ends.
**Complexity:** `O(n log n)`.

---

## 12. Meeting Rooms II (LC 253) · 🟡
Minimum number of rooms needed.

```python
import heapq
def minMeetingRooms(intervals):
    # sweep line: events (time, +1 start, -1 end); keep running count
    events = []
    for s, e in intervals:
        events.append((s, 1))
        events.append((e, -1))
    events.sort()
    rooms = cur = 0
    for _, delta in events:
        cur += delta
        rooms = max(rooms, cur)
    return rooms
```
> [!tip] A heap version: push the *end time* of each meeting; when a new meeting starts, pop every room that freed up before it. The heap size is the answer.

**Complexity:** `O(n log n)`.

---

## 13. Meeting Rooms III (LC 2413) · 🔴
Always assign the *earliest‑available* room; find the room used most.

```python
def mostBooked(intervals, nRooms):
    import heapq
    intervals.sort()
    # (earliest_free_time, room_id)
    rooms = list(range(nRooms))
    heapq.heapify(rooms)
    counts = [0] * nRooms
    for s, e in intervals:
        if rooms[0][0] <= s:
            # the earliest room is already free
            ft, r = heapq.heappop(rooms)
        else:
            # must reuse the room that frees up the earliest (rooms[0])
            ft, r = rooms[0]
        counts[r] += 1
        heapq.heappush(rooms, (e, r))
    # if ties, the lowest-index room wins
    return counts.index(max(counts))
```
**Key insight:** a *min‑heap over `(free_time, room)`*. When the earliest room isn't free, the problem says "reuse the one that *will* free earliest" — that's just the current heap root.
**Complexity:** `O(n log n)`.

---

## 14. Non‑overlapping Intervals (LC 435) · 🟡
Fewest removals to make intervals non‑overlapping.

```python
def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])     # sort by END
    keep, last_end = 0, float("-inf")
    for s, e in intervals:
        if s >= last_end:
            keep += 1
            last_end = e
    return len(intervals) - keep
```
**Key insight:** **sort by end time** and greedily keep an interval whenever its start is past the last kept end. Fewer removals = keep the maximum. This is the classic "activity selection" greedy.
**Complexity:** `O(n log n)`.

---

## 15. Insert Interval (LC 57) · 🟡
Insert `newInterval` into a sorted list, merging overlaps.

```python
def insert(intervals, newInterval):
    res = []
    i = 0
    # 1. Add all intervals that end before the new one starts
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        res.append(intervals[i]); i += 1
    # 2. Merge with every interval that overlaps
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval = [min(newInterval[0], intervals[i][0]),
                       max(newInterval[1], intervals[i][1])]
        i += 1
    res.append(newInterval)
    # 3. Add all remaining intervals
    while i < len(intervals):
        res.append(intervals[i]); i += 1
    return res
```
**Key insight:** three phases — "before," "merge," "after." The merge grows `newInterval`'s endpoints.
**Complexity:** `O(n)` time (plus the initial sort).

---

## 16. Merge Intervals (LC 56) · 🟡
Merge all overlapping intervals.

```python
def merge(intervals):
    if not intervals:
        return []
    intervals.sort()
    out = [intervals[0]]
    for s, e in intervals[1:]:
        if s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return out
```
**Key insight:** sort by start; each interval either merges with the last (overlaps) or starts a new one.
**Complexity:** `O(n log n)`.

---

## 17. Minimum Number of Arrows to Burst Balloons (LC 452) · 🟡
Minimum points (arrows) to burst all balloons (intervals).

```python
def findMinArrowShots(points):
    points.sort(key=lambda x: x[1])     # by the END (the "tight" side)
    if not points:
        return 0
    arrows = 1
    last_end = points[0][1]
    for s, e in points[1:]:
        if s > last_end:
            arrows += 1
            last_end = e
    return arrows
```
**Key insight:** same as LC 435 but count *arrows* instead of *removals*. Greedy: burst the tightest (earliest‑ending) cluster with one arrow at its right end.
**Complexity:** `O(n log n)`.

---

## 18. Minimum Interval to Include Each Query (LC 1874) · 🟡
For each query, the length of the smallest interval that *contains* the query value.

```python
import heapq
def minInterval(intervals, queries):
    # "contains q" means start <= q <= end. Sort queries; sweep intervals by start;
    # a min-heap of (end, length) holds the current candidates; drop ends < q.
    intervals.sort()
    starts = [iv[0] for iv in intervals]
    qorder = sorted(range(len(queries)), key=lambda i: queries[i])
    ans = [-1] * len(queries)
    heap = []           # (end, length), min-heap over `end`
    j = 0
    for qi in qorder:
        q = queries[qi]
        while j < len(intervals) and starts[j] <= q:
            s, e = intervals[j]
            heapq.heappush(heap, (e, e - s + 1))
            j += 1
        while heap and heap[0][0] < q:     # interval ended before q -> can't contain it
            heapq.heappop(heap)
        if heap:
            ans[qi] = heap[0][1]            # shortest length among what's left
    return ans
```
**Key insight:** "contains `q`" means `start ≤ q ≤ end`. Sort queries ascending; as each query grows, every interval whose `start ≤ q` becomes a *candidate*. A min‑heap over `(end, length)` lets us drop candidates that ended before `q` and read the smallest length in `O(1)`.
**Complexity:** `O((n + m) log n)`.

---

## 19. Interval Scheduling (Max Non‑overlapping) — *the greedy you should always know*
Given `intervals`, maximum number of *mutually* non‑overlapping meetings.

```python
def maxMeetings(intervals):
    intervals.sort(key=lambda x: x[1])     # by END time
    count, last_end = 0, float("-inf")
    for s, e in intervals:
        if s >= last_end:
            count += 1
            last_end = e
    return count
```
**Key insight:** the **activity‑selection** greedy — always pick the meeting that *ends earliest*, then skip all that conflict. Provable optimal.
**Complexity:** `O(n log n)`.

---

## 20. Find the Town Judge (LC 994) · 🟢
The "trusts everyone, is trusted by all, trusts no one" person.

```python
def findJudge(n, trust):
    out_deg = [0] * (n + 1)   # how many each person trusts
    in_deg = [0] * (n + 1)    # how many trust each person
    for a, b in trust:
        out_deg[a] += 1
        in_deg[b] += 1
    for p in range(1, n + 1):
        if out_deg[p] == 0 and in_deg[p] == n - 1:
            return p
    return -1
```
**Key insight:** the judge has **out‑degree 0** (trusts nobody) and **in‑degree `n−1`** (everyone else trusts them).
**Complexity:** `O(n + m)`.

---

## Self‑Test (cover the answers, then reveal)

> [!question] Top K frequent: why a *min*‑heap of size `k` (not a max‑heap of size `k`)?
> A min‑heap's root is the *smallest* of the `k` largest we've kept. Every time we see a bigger count, we can `heapreplace` it in. The root always holds the k‑th element.

> [!question] Meeting Rooms II: why does "sort by end, greedy keep" give the *minimum* removals?
> Keeping the *earliest‑ending* compatible interval maximizes the room left for later intervals. It's the activity‑selection optimality argument — you can always transform any optimal solution into the greedy one by swapping in earlier‑ending choices.

> [!question] Task Scheduler (LC 621): why `(max_cnt - 1) * (n + 1) + n_max`?
> The `max_cnt - 1` blocks of length `n+1` are the "busy" rounds where the most‑frequent task runs *and* cooldowns. The last round needs only `n_max` slots (one per task that shares the top frequency — no cooldown *after* the last task).

> [!question] Median of a data stream: why two heaps and not a balanced BST?
> Python has no built‑in balanced BST. Two heaps give `O(log n)` insert and `O(1)` median with a few lines. The invariant is "`small` holds the *lower* half, `large` the *upper* half, sizes differ by at most 1."

> [!question] Non‑overlapping Intervals (LC 435): why sort by **end** time, not start time?
> "Earliest end first" maximizes the room for later intervals. "Earliest start first" can greedily pick a long early interval that blocks many short later ones. The *end* is the binding constraint.

> [!question] Find the Town Judge (LC 994): why check both out‑degree and in‑degree?
> One check alone is ambiguous. A person who's trusted by everyone might also trust someone (out‑degree > 0) — not a judge. A person who trusts nobody might not be trusted by everyone (in‑degree < n−1) — not a judge. Both.

## Related

- Next: [[08-Dynamic Programming]] — the "state machine" that solves everything else.
- Back to the index: [[LeetCode - Map of Content]].
- The **sweep line** pattern (sort events, walk left→right) is the heart of this file and of graph coloring, interval coverage, etc.
