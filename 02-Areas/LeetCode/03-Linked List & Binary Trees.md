---
tags: [leetcode, dsa, linked-list, binary-tree, recursion, python]
domain: computer-science
category: 03
count: 24
updated: 2026
status: reference
parent: "[[LeetCode - Map of Content]]"
---

# 03 · Linked List & Binary Trees

> [!abstract] The toolbox in this file
> - **Fast/slow pointers** — detect cycles, find midpoints, reverse in-place.
> - **Dummy head** — a sentinel `Node` before the real head eliminates `head-is-None` special cases.
> - **Tree recursion** — post‑order `return (left, right)` pairs; the caller combines them.
> - **BFS by level** — `collections.deque` + "process current level" loops.
> - **BST property** — every node's left < node < right; used in search, insert, validate.
>
> Python idiom: `Node` is a small class; `list(node.val for node in cur)` is the go‑to extraction pattern.

**Difficulty legend:** 🟢 Easy · 🟡 Medium · 🔴 Hard

---

## 1. Reverse Linked List (LC 206) · 🟢
Reverse a singly‑linked list.

```python
def reverseList(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev      # point back
        prev = head
        head = nxt
    return prev
```
**Key insight:** three pointers (`prev`, `head`, `nxt`) — reverse each link one at a time.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 2. Merge Two Sorted Lists (LC 21) · 🟢
Merge two sorted linked lists into one sorted list.

```python
def mergeTwoLists(l1, l2):
    dummy = Node(0)
    cur = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next, l1 = l1, l1.next
        else:
            cur.next, l2 = l2, l2.next
        cur = cur.next
    cur.next = l1 if l1 else l2   # attach the longer tail
    return dummy.next
```
**Key insight:** **dummy head** — you never special‑case "is this the first node?" because `dummy.next` is always the answer.
**Complexity:** `O(m+n)` time, `O(1)` space.

---

## 3. Linked List Cycle (LC 141) · 🟢
Does the list have a cycle?

```python
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```
**Key insight:** **Floyd's two‑pointer** — the fast pointer laps the slow one iff a cycle exists.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 4. Reorder List (LC 143) · 🟡
`1→2→3→4→5` becomes `1→4→2→5→3`.

```python
def reorderList(head):
    if not head or not head.next:
        return
    # 1. Find the midpoint (fast/slow)
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    # 2. Reverse the second half
    second = reverseList(slow.next)
    slow.next = None
    # 3. Interleave
    first, last = head, second
    while last:
        nxt1, nxt2 = first.next, last.next
        first.next = last
        last.next = nxt1
        first, last = nxt1, nxt2
```
**Key insight:** split at midpoint, reverse the back half, then weave. The "interleave" step is the trick — keep two alternates.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 5. Palindrome Linked List (LC 234) · 🟢
Check if a linked list is a palindrome.

```python
def isPalindrome(head):
    if not head:
        return True
    # collect values, then compare against itself reversed
    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.next
    return vals == vals[::-1]
```
**Key insight:** "dump to list, reverse, compare" — `O(n)` time, `O(n)` space. For `O(1)` space, reverse the second half and compare with the first (the "two‑pointer" trick from LC 141).
**Complexity:** `O(n)` time, `O(n)` space.

---

## 6. Remove Nth Node from End (LC 19) · 🟡
Remove the `n`th node from the end.

```python
def removeNthFromEnd(head, n):
    dummy = Node(0)
    dummy.next = head
    # two pointers, `n` apart
    slow = fast = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next
```
**Key insight:** fast runs `n+1` ahead; when fast hits `None`, slow is just *before* the target. Dummy handles the "remove the head" case.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 7. Rotate Right (LC 61) · 🟡
Rotate the list right by `k` places.

```python
def rotateRight(head, k):
    # measure length, find new tail
    n, cur = 0, head
    while cur:
        n += 1
        cur = cur.next
    if n == 0:
        return head
    k %= n
    # connect tail to head, then cut at position n - k
    tail = head
    for _ in range(n - 1):
        tail = tail.next
    tail.next = head
    new_tail = head
    for _ in range(n - k - 1):
        new_tail = new_tail.next
    head, new_tail.next = new_tail.next, None
    return head
```
**Key insight:** make it a *cycle*, then cut. `k %= n` collapses the loop.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 8. Remove Duplicates from Sorted List (LC 83) · 🟢
Remove adjacent duplicates from a sorted linked list.

```python
def deleteDuplicates(head):
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head
```
**Key insight:** one pointer; skip a node iff it equals its successor.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 9. Remove Duplicates from Sorted List II (LC 82) · 🟡
Remove all nodes that have duplicates, leaving only distinct values.

```python
def deleteDuplicates(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    cur = head
    while cur:
        while cur.next and cur.val == cur.next.val:
            cur = cur.next
        # cur is now the last of its duplicate run (or the only node)
        if prev.next != cur:
            prev.next = cur.next   # skip the whole run
        prev = prev.next
        cur = cur.next
    return dummy.next
```
**Key insight:** track the *run* of equal values; if the run has length > 1, bypass it entirely.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 10. Reverse Nodes in k‑Group (LC 25) · 🔴
Reverse every `k` consecutive nodes.

```python
def reverseKGroup(head, k):
    # count: if fewer than k nodes remain, stop
    count = 0
    cur = head
    while cur and count < k:
        cur = cur.next
        count += 1
    if count < k:
        return head
    # reverse the first k
    prev, nxt = None, head
    for _ in range(k):
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    # attach the rest recursively
    prev.next = reverseKGroup(head, k)
    return prev
```
**Key insight:** the `prev` pointer after reversing `k` nodes is the *new head of this group*. The original head (`head` after the loop) is the next group to process — recurse.
**Complexity:** `O(n)` time, `O(n/k)` space (recursion depth).

---

## 11. Swap Nodes in Pairs (LC 145) · 🟡
Swap adjacent nodes: `1↔2, 3↔4, …`

```python
def swapPairs(head):
    dummy = Node(0)
    dummy.next = head
    cur = dummy
    while cur.next and cur.next.next:
        first, second = cur.next, cur.next.next
        first.next = second.next
        second.next = first
        cur.next = second
        cur = first             # cur is now the "last of the swapped pair"
    return dummy.next
```
**Key insight:** three links per swap. `cur` stays *behind* the pair being swapped.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 12. Binary Tree Inorder Traversal (LC 94) · 🟢
Return the inorder (left‑node‑right) values.

```python
def inorderTraversal(root):
    out, stack = [], []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        out.append(cur.val)
        cur = cur.right
    return out
```
**Key insight:** iterative with a stack — the classic post‑order trick: "always go left, then pop and emit, then go right."
**Complexity:** `O(n)` time, `O(n)` space.

---

## 13. Validate Binary Search Tree (LC 98) · 🟡
Check that the BST invariant holds.

```python
def isValidBST(root):
    def check(node, lo, hi):
        if not node:
            return True
        if not (lo < node.val < hi):
            return False
        return check(node.left, lo, node.val) and check(node.right, node.val, hi)
    return check(root, float("-inf"), float("inf"))
```
**Key insight:** the *range* of valid values shrinks as you descend. Left child must be in `(lo, node.val)`, right in `(node.val, hi)`.
**Complexity:** `O(n)` time, `O(n)` space (recursion).

---

## 14. Convert Sorted List to BST (LC 108) · 🟡
Build a balanced BST from a sorted linked list.

```python
def sortedListToBST(head):
    # find the middle via fast/slow
    if not head:
        return None
    if not head.next:
        return Node(head.val)
    slow, fast = head, head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None
    node = Node(slow.val)
    node.left = sortedListToBST(head)
    node.right = sortedListToBST(slow.next)
    return node
```
**Key insight:** the **middle** of the sorted list is the root (keeps the tree balanced). Recurse on the two halves. `prev` cuts the list so the recursion sees the right half.
**Complexity:** `O(n log n)` time, `O(log n)` space.

---

## 15. Lowest Common Ancestor (LC 236) · 🟡
LCA of two nodes in a *binary tree* (not necessarily a BST).

```python
def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root            # p and q are on *different* sides
    return left or right       # both on one side
```
**Key insight:** post‑order. If both subtrees returned a non‑None, the current node is the LCA. Otherwise pass up the one that's not None.
**Complexity:** `O(n)` time, `O(n)` space.

---

## 16. Diameter of Binary Tree (LC 543) · 🟢
Longest path between any two nodes (count edges).

```python
def diameterOfBinaryTree(root):
    best = 0
    def depth(node):
        nonlocal best
        if not node:
            return 0
        l, r = depth(node.left), depth(node.right)
        best = max(best, l + r)  # path through this node
        return 1 + max(l, r)
    depth(root)
    return best
```
**Key insight:** a *path* that passes through a node has length `left_depth + right_depth`. Track the max across all nodes.
**Complexity:** `O(n)` time, `O(n)` space.

---

## 17. Minimum Depth of Binary Tree (LC 111) · 🟢
Root‑to‑leaf depth.

```python
def minDepth(root):
    if not root:
        return 0
    l, r = minDepth(root.left), minDepth(root.right)
    if root.left and root.right:
        return 1 + min(l, r)
    return 1 + (l or r)    # if one side is None, use the other
```
**Key insight:** a *leaf* is a node with **no** children. If one side is `None`, the answer is the *other* side's depth + 1, not `min(l, r) + 1` (which would be 0 + 1 = 1 even for a non‑leaf).
**Complexity:** `O(n)` time, `O(n)` space.

---

## 18. Binary Tree Level Order Traversal (LC 102) · 🟡
BFS by level; return `[[1],[2,3],[4,5,6,7]]`.

```python
from collections import deque
def levelOrder(root):
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        vals = []
        for _ in range(len(q)):
            node = q.popleft()
            vals.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        out.append(vals)
    return out
```
**Key insight:** "process exactly `len(q)` nodes" is the BFS‑by‑level idiom. The queue holds *the current level's frontier*.
**Complexity:** `O(n)` time, `O(n)` space.

---

## 19. Zigzag Level Order Traversal (LC 103) · 🟡
Same as LC 102 but alternate left‑to‑right vs. right‑to‑left.

```python
from collections import deque
def zigzagLevelOrder(root):
    if not root:
        return []
    out, q, left_to_right = [], deque([root]), True
    while q:
        vals = []
        for _ in range(len(q)):
            node = q.popleft()
            vals.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        out.append(vals if left_to_right else vals[::-1])
        left_to_right = not left_to_right
    return out
```
**Key insight:** same BFS as LC 102; just reverse the row when it's a right‑to‑left pass.
**Complexity:** `O(n)` time, `O(n)` space.

---

## 20. Same Tree (LC 100) · 🟢
Two trees are identical iff their structure and node values match.

```python
def isSameTree(p, q):
    if not p or not q:
        return p is q            # both None -> True; one None -> False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
```
**Key insight:** the `p is q` (identity) trick handles the "both are None" case elegantly.
**Complexity:** `O(n)` time, `O(n)` space.

---

## 21. Symmetric Tree (LC 101) · 🟢
Check if the tree is a mirror of itself.

```python
def isSymmetric(root):
    def mirror(a, b):
        if not a or not b:
            return a is b
        return a.val == b.val and mirror(a.left, b.right) and mirror(a.right, b.left)
    return mirror(root, root)
```
**Key insight:** a "mirror" check is the same as "same tree" but with left‑right crossed: `a.left` vs `b.right`, `a.right` vs `b.left`.
**Complexity:** `O(n)` time, `O(n)` space.

---

## 22. Path Sum (LC 113) · 🟡
All root‑to‑leaf paths that sum to `target`.

```python
def pathSum(root, targetSum):
    out = []
    def walk(node, target, path):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right and node.val == target:
            out.append(path[:])       # snapshot the path
        walk(node.left, target - node.val, path)
        walk(node.right, target - node.val, path)
        path.pop()                   # backtrack
    walk(root, targetSum, [])
    return out
```
**Key insight:** the **snapshot** `path[:]` is critical — otherwise later backtracking corrupts the stored path.
**Complexity:** `O(n)` time, `O(n)` space.

---

## 23. Path Sum II — *path count* (LC 437) · 🟡
Count **all** root‑to‑leaf paths that sum to `target`? No — all paths that sum to `targetSum`, where a path may *start and end anywhere* (not just at a leaf).

```python
from collections import defaultdict
def pathSum(root, targetSum):
    total = 0
    prefix = defaultdict(int)     # prefix-sum value -> how many times seen on current root->node path
    prefix[0] = 1                 # the "empty prefix" so paths starting at root count

    def dfs(node, s):
        nonlocal total
        if not node:
            return
        s += node.val
        # any earlier prefix equal to s - targetSum gives a path summing to targetSum
        total += prefix[s - targetSum]
        prefix[s] += 1
        dfs(node.left, s)
        dfs(node.right, s)
        prefix[s] -= 1            # backtrack: this prefix no longer on the path
    dfs(root, 0)
    return total
```
**Key insight:** exactly the **prefix‑sum** trick from the array version ([[01-Arrays & Two Pointers]] #15), applied to a tree path. `prefix[s − targetSum]` counts how many ancestors give a valid start. Backtracking (`prefix[s] -= 1`) keeps the map correct for sibling subtrees.
**Complexity:** `O(n)` time, `O(n)` space.

---

## 24. Binary Tree Maximum Path Sum (LC 918 / 687) · 🔴
Max sum of any path between two nodes (at most one "bend").

```python
def maxPathSum(root):
    best = float("-inf")
    def gain(node):
        nonlocal best
        if not node:
            return 0
        l = max(gain(node.left), 0)   # negative subtrees contribute nothing
        r = max(gain(node.right), 0)
        best = max(best, node.val + l + r)   # path through this node
        return node.val + max(l, r)         # path going *up* from this node
    gain(root)
    return best
```
**Key insight:** two values per node — (1) best path *through* this node, (2) best path *going up*. Negative branches are skipped (`max(·, 0)`).
**Complexity:** `O(n)` time, `O(n)` space.

---

## Self‑Test (cover the answers, then reveal)

> [!question] Linked list cycle (LC 141): why does the fast pointer catch the slow one in a cycle?
> The fast pointer gains one position per step. In a cycle of length `k`, the gap shrinks by 1 each step, so it closes after at most `k` steps. No cycle → fast hits `None` first.

> [!question] Why is `prev = slow` in `sortedListToBST` a critical detail?
> Without it, the recursive call on the "left half" would include the middle node *and* the right half — a subtle bug. Cutting the list at the midpoint keeps the halves disjoint.

> [!question] LCA (LC 236): why is "both left and right returned non‑None" the exact moment to stop?
> The LCA is the *first* node on the root‑to‑leaf path where `p` and `q` are on *different* sides. Before that, they're in the same subtree (one child returns None). After that, you've gone too far.

> [!question] Minimum depth (LC 111): why is `1 + min(l, r)` wrong when one side is None?
> Because a node with only a left child is *not* a leaf. The path must go all the way to the left subtree's bottom. `min(l, 0)` would give 1 even for a deep tree.

> [!question] Maximum path sum (LC 918): why do we skip negative subtrees?
> A negative gain *from a subtree* would only *decrease* the total. Taking the `max(gain, 0)` step is "start the path here, don't extend through a negative child."

> [!question] In `pathSum` (LC 437), why do we `prefix[s] -= 1` after the recursion?
> Backtracking. `prefix` must reflect *the path from root to the current node only*. If we don't decrement, sibling subtrees see counts from a path they don't share.

## Related

- Next: [[04-Stacks, Queues & Sliding Window]] — the "undo" data structure.
- Back to the index: [[LeetCode - Map of Content]].
- Recursion on trees is just a special case of backtracking; see [[05-Binary Search & Backtracking]].
