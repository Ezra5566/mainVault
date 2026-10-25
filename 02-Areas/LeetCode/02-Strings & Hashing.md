---
tags: [leetcode, dsa, strings, hashing, two-pointers, python]
domain: computer-science
category: 02
count: 24
updated: 2026
status: reference
parent: "[[LeetCode - Map of Content]]"
---

# 02 · Strings & Hashing

> [!abstract] The toolbox in this file
> - **Frequency counting** with `collections.Counter` / `defaultdict` — anagram, ransom-note, palindrome tests.
> - **Two pointers from the ends** — palindrome checking, palindromic substrings.
> - **Sliding window over characters** — longest substring, minimum window.
> - **Encoding/decoding** — run-length, nested decode, Roman.
> - **In‑place string moves** — treat `str` as immutable: copy to a `list`, mutate, `"".join`.
>
> In Python, `str` is immutable. If you must mutate character-by-character, do `lst = list(s)`, work on `lst`, then `"".join(lst)`.

**Difficulty legend:** 🟢 Easy · 🟡 Medium · 🔴 Hard

---

## 1. Valid Palindrome (LC 7) · 🟢
A string is a palindrome ignoring non‑alphanumerics and case.

```python
def isPalindrome(s):
    lo, hi = 0, len(s) - 1
    while lo < hi:
        while lo < hi and not s[lo].isalnum():
            lo += 1
        while lo < hi and not s[hi].isalnum():
            hi -= 1
        if s[lo].lower() != s[hi].lower():
            return False
        lo += 1; hi -= 1
    return True
```
**Key insight:** two pointers skip junk characters and compare case‑insensitively. One pass, `O(n)` time.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 2. Valid Anagram (LC 242) · 🟢
`s` is an anagram of `t` iff they have the same letter counts.

```python
from collections import Counter
def isAnagram(s, t):
    return Counter(s) == Counter(t)   # counts must match AND lengths equal
```
**Key insight:** `Counter` builds a frequency map; equality of the two maps *and* equal lengths means the letters match exactly.
**Manual version:** one dict, `+1` for `s`, `-1` for `t`; at the end every value must be `0`.
**Complexity:** `O(n)` time, `O(1)` space (at most 26 keys).

---

## 3. Group Anagrams (LC 49) · 🟡
Group strings that are anagrams of each other.

```python
from collections import defaultdict
def groupAnagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))      # anagrams share the same sorted form
        groups[key].append(s)
    return list(groups.values())
```
**Key insight:** the *sorted* string is a canonical key for the anagram class (or a 26‑letter frequency tuple for `O(n·k)` without sorting).
**Complexity:** `O(n·k log k)` time, `O(n·k)` space, where `k` is the max string length.

---

## 4. First Unique Character in a String (LC 387) · 🟢
Index of the first character that appears exactly once.

```python
from collections import Counter
def firstUniqChar(s):
    c = Counter(s)
    for i, ch in enumerate(s):        # first (by position) with count 1
        if c[ch] == 1:
            return i
    return -1
```
**Key insight:** count first, then scan in original order — the *position* is what makes it "first."
**Complexity:** `O(n)` time, `O(1)` space.

---

## 5. Ransom Note (LC 383) · 🟢
Can you form `ransomNote` from the letters of `magazine`?

```python
from collections import Counter
def canConstruct(ransomNote, magazine):
    m = Counter(magazine)
    for ch in ransomNote:
        if m[ch] <= 0:
            return False
        m[ch] -= 1
    return True
```
**Key insight:** drain `magazine`'s letters as you "spend" them on `ransomNote`. Any letter you can't pay for → `False`.
**Complexity:** `O(len(ransomNote) + len(magazine))` time, `O(1)` space.

---

## 6. Valid Palindrome II (LC 680) · 🟢
Can you remove **at most one** character to make it a palindrome?

```python
def validPalindrome(s):
    lo, hi = 0, len(s) - 1
    while lo < hi:
        if s[lo] != s[hi]:
            # try dropping left char, or dropping right char
            return is_pal(s, lo + 1, hi) or is_pal(s, lo, hi - 1)
        lo += 1; hi -= 1
    return True

def is_pal(s, lo, hi):
    while lo < hi:
        if s[lo] != s[hi]:
            return False
        lo += 1; hi -= 1
    return True
```
**Key insight:** two pointers. The *first* mismatch tells you the only two candidates to drop (`s[lo]` or `s[hi]`). Check each once.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 7. Palindrome Permutation (LC 880) · 🟢
Can the characters be rearranged into a palindrome?

```python
from collections import Counter
def canPermutePalindrome(s):
    odd = sum(1 for v in Counter(s).values() if v % 2 == 1)
    return odd <= 1    # at most one char can be the center
```
**Key insight:** a palindrome has at most *one* character with an odd count (the middle one). Even length → zero odds.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 8. Minimum Window Substring (LC 76) · 🔴
Shortest window of `s` containing every character of `t` (with multiplicity).

```python
from collections import Counter, defaultdict
def minWindow(s, t):
    need = Counter(t)
    missing = len(t)          # how many t-characters still unmet
    lo = start = end = 0
    for hi, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        if missing == 0:     # window [lo, hi] covers t
            while need[s[lo]] < 0:   # shrink past extra chars
                need[s[lo]] += 1
                lo += 1
            if end - lo < hi - lo + 1 or end == 0:
                start, end = lo, hi
            lo += 1          # move past the current valid window
            need[s[lo - 1]] += 1
            missing += 1
    return s[start:end + 1]
```
**Key insight:** sliding window tracking how many `t`‑chars are still missing. When `missing == 0`, shrink `lo` to find the *minimal* window, then slide forward.
**Complexity:** `O(|s| + |t|)` time, `O(alphabet)` space.

---

## 9. Longest Common Prefix (LC 14) · 🟢
Longest prefix shared by every string in a list.

```python
def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
        if not prefix:
            break
    return prefix
```
**Key insight:** start with the first string as the candidate prefix and trim it until every other string has it as a prefix.
**Complexity:** `O(S)` time where `S` is the total number of characters.

---

## 10. Decode String (LC 394) · 🟡
`3[a]2[bc]` → `aaabcbcb`. Nested encodings.

```python
def decodeString(s):
    stack = []             # holds (previous_result, repeat_count)
    cur_num = 0
    cur_str = ""
    for ch in s:
        if ch.isdigit():
            cur_num = cur_num * 10 + int(ch)
        elif ch == "[":
            stack.append((cur_str, cur_num))
            cur_str, cur_num = "", 0
        elif ch == "]":
            prev, repeat = stack.pop()
            cur_str = prev + cur_str * repeat
        else:
            cur_str += ch
    return cur_str
```
**Key insight:** a **stack** for the nesting. On `[`, push what we've built so far and the multiplier; on `]`, pop and combine `prev + inner * repeat`.
**Complexity:** `O(2^d)` worst case (d nesting depth) output length; `O(n)` linear otherwise.

---

## 11. String to Integer (atoi) (LC 8) · 🟡
Parse a string to a 32‑bit integer, handling whitespace, sign, overflow.

```python
def myAtoi(s):
    s = s.lstrip()
    sign = 1
    i = 0
    if i < len(s) and s[i] in "+-":
        sign = -1 if s[i] == "-" else 1
        i += 1
    num = 0
    for ch in s[i:]:
        if not ch.isdigit():
            break
        num = num * 10 + int(ch)
        if num >= 2**31:      # clamp early to avoid overflow
            break
    num *= sign
    return max(-2**31, min(2**31 - 1, num))
```
**Key insight:** skip whitespace, read one optional sign, then digits until a non‑digit. Clamp to the 32‑bit range.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 12. Integer to Roman (LC 12) · 🟡
Convert an integer to a Roman numeral.

```python
def intToRoman(num):
    vals = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"),  (90,  "XC"), (50,  "L"), (40,  "XL"),
        (10,  "X"),  (9,   "IX"), (5,   "V"), (4,  "IV"),
        (1,   "I"),
    ]
    out = []
    for v, sym in vals:
        while num >= v:       # greedy: take as many of this value as possible
            num -= v
            out.append(sym)
    return "".join(out)
```
**Key insight:** a **greedy** subtraction over the ordered value/symbol pairs, including the "subtractive" ones (40 = XL, 90 = XC, …).
**Complexity:** `O(1)` time (bounded by the input range), `O(1)` space.

---

## 13. Roman to Integer (LC 13) · 🟢
Convert a Roman numeral string to an integer.

```python
def romanToInt(s):
    val = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    total = 0
    for i, ch in enumerate(s):
        nxt = val[s[i+1]] if i + 1 < len(s) else 0
        total += -val[ch] if val[ch] < nxt else val[ch]
    return total
```
**Key insight:** if the current value is *smaller* than the next, it's a subtractive pair (e.g., `IV` → −1+5). Add accordingly.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 14. Next Permutation (LC 31) · 🟡
Rearrange into the next lexicographic permutation in‑place; if none, sort ascending.

```python
def nextPermutation(nums):
    n = len(nums)
    i = n - 2
    # 1. find the rightmost "descent": nums[i] < nums[i+1]
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]   # 2. swap with rightmost bigger
    nums[i + 1:] = reversed(nums[i + 1:])      # 3. reverse the suffix (smallest)
```
**Key insight:** find the last position that can still increase, swap it with the smallest element to its right that's bigger, then reverse the (descending) suffix to get the smallest tail.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 15. Add Binary (LC 67) · 🟢
Add two binary strings.

```python
def addBinary(a, b):
    i, j = len(a) - 1, len(b) - 1
    carry, out = 0, []
    while i >= 0 or j >= 0 or carry:
        s = carry
        if i >= 0:
            s += int(a[i]); i -= 1
        if j >= 0:
            s += int(b[j]); j -= 1
        out.append(str(s % 2))
        carry = s // 2
    return "".join(reversed(out))
```
**Key insight:** add from the right with a carry, exactly like manual binary addition.
**Complexity:** `O(max(|a|,|b|))` time, `O(1)` extra (output aside).

---

## 16. Implement strStr() (LC 28) · 🟡
Find the index of `needle` in `haystack` (or −1).

```python
def strStr(haystack, needle):
    if not needle:
        return 0
    return haystack.find(needle)   # built-in KMP under the hood
```
A **manual KMP** (what the interview wants):
```python
def strStr(haystack, needle):
    if not needle:
        return 0
    def build_lps(pat):
        lps = [0] * len(pat)
        length = 0
        i = 1
        while i < len(pat):
            if pat[i] == pat[length]:
                length += 1; lps[i] = length; i += 1
            elif length:
                length = lps[length - 1]
            else:
                lps[i] = 0; i += 1
        return lps
    lps = build_lps(needle)
    i = j = 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1; j += 1
        if j == len(needle):
            return i - j
        elif i < len(haystack) and haystack[i] != needle[j]:
            if j:
                j = lps[j - 1]
            else:
                i += 1
    return -1
```
**Key insight:** KMP precomputes the **longest proper prefix‑suffix** (LPS) array so on a mismatch you resume from `lps[j−1]` instead of restarting — avoiding the `O(n·m)` worst case.
**Complexity:** `O(n + m)` time, `O(m)` space.

---

## 17. Isomorphic Strings (LC 205) · 🟢
Two strings are isomorphic if there's a *one‑to‑one* mapping between their characters.

```python
def isIsomorphic(s, t):
    s2t, t2s = {}, {}
    for a, b in zip(s, t):
        if s2t.get(a, b) != b or t2s.get(b, a) != a:
            return False
        s2t[a] = b
        t2s[b] = a
    return True
```
**Key insight:** maintain **two** maps (both directions). A collision in either direction breaks the bijection — `foo` vs `bar` is the classic counter‑example.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 18. Longest Repeating Character Replacement (LC 424) · 🟡
Most replacements (≤ `k`) to make the longest block of one repeated char.

```python
def characterReplacement(s, k):
    from collections import Counter
    best, freq = 0, Counter()
    left = 0
    for right in range(len(s)):
        freq[s[right]] += 1
        # window is valid if (window_len - most_common) <= k
        if (right - left + 1) - max(freq.values()) > k:
            freq[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
```
**Key insight:** sliding window where "valid" means *at most* `k` characters differ from the most frequent one. Note `best` is updated before shrinking — this is a known trick.
**Complexity:** `O(n · 26)` time (or `O(n)` if you track the max), `O(1)` space.

---

## 19. Maximum Repeating Substring (LC 967) · 🟢
Largest `k` such that `p` repeated `k` times is a substring of `s`.

```python
def maxRepeating(sequence, word):
    target = word
    count = 0
    while target in sequence:
        target += word
        count += 1
    return count
```
**Key insight:** keep appending `word` until the concatenated string no longer appears in `sequence`. (Bounded by `len(sequence)/len(word)`, so it's fast.)
**Complexity:** `O((n/m)²)` time in the worst case.

---

## 20. Longest Substring of One Vowel (LC 2681) · 🟢
Longest contiguous substring containing **only** vowels.

```python
def maxVowels(word):
    best = cur = 0
    vowels = set("aeiou")
    for ch in word:
        cur = cur + 1 if ch in vowels else 0
        best = max(best, cur)
    return best
```
**Key insight:** run of consecutive vowels; reset to `0` on a consonant, track the longest run.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 21. Shuffle String (LC 1528) · 🟢
Reorder characters of `s` given by the index list `indices`.

```python
def shuffleString(s, indices):
    n = len(s)
    out = [""] * n
    for i, ch in enumerate(s):
        out[indices[i]] = ch
    return "".join(out)
```
**Key insight:** the character at position `i` of `s` moves to `indices[i]` in the answer.
**Complexity:** `O(n)` time, `O(n)` space.

---

## 22. Count Number of Homogenous Substrings (LC 1658) · 🟡
Count contiguous substrings where all characters are the same (mod `10^9+7`).

```python
def countHomogenous(s):
    MOD = 10**9 + 7
    total, run = 0, 0
    for i, ch in enumerate(s):
        run = run + 1 if i > 0 and s[i-1] == ch else 1
        total = (total + run) % MOD
    return total
```
**Key insight:** a run of length `r` contributes `r·(r+1)/2` homogenous substrings; the running `run` counter accumulates them on the fly.
**Complexity:** `O(n)` time, `O(1)` space.

---

## 23. Shortest Palindrome (LC 214) · 🔴
Prepend the fewest characters to make `s` a palindrome.

```python
def shortestPalindrome(s):
    rev = s[::-1]
    # longest suffix of s that is a prefix of rev
    for i in range(len(s)):
        if s.startswith(rev[i:]):
            return rev[:i] + s
    return rev + s
```
**Key insight:** the answer is "the part of the reverse that isn't already covered by the longest palindromic prefix of `s`." A KMP/Z‑function version does this in `O(n)`.
**Complexity:** `O(n²)` naive; `O(n)` with the prefix function.

---

## 24. Reorganize String (LC 791) · 🟡
Reorder `s` so no two adjacent characters are the same (or `""` if impossible).

```python
def reorganizeString(s):
    import heapq
    from collections import Counter
    if max(Counter(s).values()) > (len(s) + 1) // 2:
        return ""                  # one char too frequent to interleave
    freq = [(-c, ch) for ch, c in Counter(s).items()]
    heapq.heapify(freq)            # max-heap on (-count, char)
    prev, res = 0, ""
    while freq:
        cnt, ch = heapq.heappop(freq)
        cnt += 1                    # take one
        res += ch
        if prev:
            heapq.heappush(freq, prev)   # put back the char we used last
        prev = (cnt, ch) if cnt < 0 else None
    return res
```
**Key insight:** **interleave the two most frequent** using a max‑heap; skip the character you just used (the `prev` slot). If any character's count exceeds `(n+1)//2`, no valid arrangement exists.
**Complexity:** `O(n log k)` time where `k` is the alphabet size.

---

## Self‑Test (cover the answers, then reveal)

> [!question] Two‑pointer palindrome (LC 7): why do we advance *both* pointers on a mismatch, not just one?
> We only advance one when the character is *not* alnum (we're skipping it). On a real mismatch of two alnums, we return `False` immediately — the palindrome property is already broken.

> [!question] Why does `str.startswith(prefix)` with a *shrinking* prefix find the LCP?
> If some string in the list lacks the current prefix, *trim one char* and retry. The prefix can only shrink monotonically, so the first length where all strings still match it is the LCP.

> [!question] In KMP, what does the LPS table actually store?
> For each position `i`, `lps[i]` = length of the longest proper prefix of `pat[0..i]` that is also a suffix. It tells you how many characters you can "keep matched" after a mismatch.

> [!question] Boyer‑Moore‑style "most frequent" in `characterReplacement` (LC 424): why does `best` update *before* we shrink?
> The invariant is "at most `k` chars differ from the most frequent." `max(freq.values())` can only grow as the window widens, so the *widest valid* window for each `right` is recorded *before* the `left` shrink. The `best` value lags by at most one, but the answer is correct.

> [!question] Reorganize String — why is `(n+1)//2` the frequency cap?
> The most frequent character needs a slot at every other position (1, 3, 5, …). There are `(n+1)//2` such slots. If any character needs more, it's impossible.

> [!question] atoi (LC 8): what do we do when `num` overflows 32 bits?
> We **clamp** to `[−2³¹, 2³¹−1]`. Most interviews expect the "return the clamped value" behavior, not an exception.

## Related

- Next: [[03-Linked List & Binary Trees]] — pointer manipulation + recursion on trees.
- Back to the index: [[LeetCode - Map of Content]].
- Hashing patterns (Counter, defaultdict) are documented in [[05-AI-Research/Deep Dives/Python]] §"Stdlib Use Cases."
