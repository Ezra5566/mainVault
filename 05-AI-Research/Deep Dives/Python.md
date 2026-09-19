---
tags: [python, syntax, reference, stdlib, snippets, beginner, pro]
aliases: [Python Syntax, Python Cheatsheet, Python Reference]
level: beginner → professional
focus: [core-syntax, data-types, control-flow, functions, oop, stdlib-use-cases, metaprogramming, concurrency]
updated: 2026
status: reference
---

# Python — Complete Syntax & Use-Case Reference

> [!abstract] What this note is
> A single, self-contained reference for **Python syntax and the stdlib use cases you actually hit**. Every block is runnable and was syntax‑checked. Read top‑to‑bottom to learn, or jump to the section table below to use it as a lookup while coding.
>
> **Companion:** this is the *language* layer. The *ML/AI stack* built on top of it lives in [[Python for AI]] — that note shows NumPy / Pandas / scikit‑learn / LLM clients; this note shows the Python that makes all of it possible.
>
> **How to use it:** each major section ends with a `[!question]` self‑test toggle — cover the answer, try to answer, then reveal. The tables are for scanning; the code blocks are for copying.

**Jump‑to‑section (the map):**

| § | Topic | § | Topic | § | Topic |
|---|---|---|---|---|---|
| 1 | Values, types, operators | 8 | Classes & OOP | 15 | Concurrency |
| 2 | Control flow | 9 | Modules & packages | 16 | stdlib use cases |
| 3 | Data structures | 10 | Errors | 17 | Gotchas |
| 4 | Functions | 11 | Files & IO | 18 | Self‑test |
| 5 | Comprehensions | 12 | Lambdas & functools | | |
| 6 | Iterators / generators | 13 | Type hints | | |
| 7 | Strings & f‑strings | 14 | Decorators & context | | |

---

## 1. Values, Types & Operators

### 1.1 Literals & built‑in types

```python
# numbers
int    = -7
float  = 3.14
complex= 2 + 3j
# strings
str   = "text"          # double or single quotes are identical
# bytes
bytes = b"\x00\x01"
# boolean — a *subclass* of int (True == 1, False == 0)
flag  = True
# None — the null object; only one value, use `is None`
nothing = None
```

> [!warning] Two `__eq__` operators you must know
> `==` compares **value**; `is` compares **identity** (same object in memory). For singletons use `is`: `if x is None:` never `if x == None:` (the latter is PEP‑8 banned and can misbehave with custom `__eq__`).

### 1.2 Type conversion & checking

```python
int("42")            # -> 42
float("3.14")        # -> 3.14
str(1234)            # -> "1234"
list((1, 2, 3))     # -> [1, 2, 3]
tuple([1, 2, 3])    # -> (1, 2, 3)
set("abc")          # -> {'a','b','c'}
dict([("a",1),("b",2)])  # -> {"a":1,"b":2}

# isinstance is the safe check (respects inheritance); type() is exact
isinstance(5, int)          # True
isinstance(True, int)      # True! (bool subclasses int) — be careful with sums
```

### 1.3 Operators you'll use daily

```python
# arithmetic
7 // 2        # -> 3   floor division (integer)
7 %  2        # -> 1   modulus
2 ** 10       # -> 1024  exponent

# comparisons chain: 1 < x < 10 reads exactly like math
1 < 5 < 10    # -> True  (equivalent to 1<5 and 5<10)

# augmented assignment
x = 0; x += 3; x -= 1; x *= 2   # -> 4

# identity / membership
"sp" in "span"      # True  (substring or container element)
5 not in [1,2,3]    # True
```

> [!note] The truthiness rule
> A value is **falsy** if it's `False`, `None`, `0`, `0.0`, `""`, `[]`, `()`, `{}`, or `set()`. Everything else is **truthy**. This is why `if not xs:` means "list is empty" and `if xs:` means "list has at least one element."

---

## 2. Control Flow

### 2.1 if / elif / else

```python
score = 87
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"
# elif (never "else if") and indentation is the block delimiter — no braces
```

### 2.2 Ternary (conditional expression)

```python
n = 5
result = "odd" if n % 2 else "even"      # -> "odd"
# pattern:  X if COND else Y
```

### 2.3 Loops

```python
# for — over any *iterable*
for i, x in enumerate(["a", "b", "c"]):          # 0,1,2 + value
    print(i, x)

for k, v in {"a": 1, "b": 2}.items():             # dict pairs
    print(k, "=", v)

for s in zip(names, ages, cities):                # parallel iteration
    print(s)

# while
n = 10
while n > 0:
    n -= 1

# for/while with control
for i in range(10):
    if i == 3:
        continue    # skip
    if i == 7:
        break       # stop
    print(i)
    # no else-branch of the loop that breaks? see 2.4
```

### 2.4 for‑else (rare but useful)

The `else` block runs **only if the loop finished without `break`.** Great for "was the thing found?" logic:

```python
primes = [2, 3, 5, 7, 11, 13]
for p in primes:
    if p == 4:
        break
else:
    print("4 is not in the list")   # runs because we never broke
```

### 2.5 Match (Python 3.10+) — structural pattern matching

```python
def describe(cmd: str) -> str:
    match cmd.split():
        case ["quit"]:
            return "exit"
        case ["go", direction]:
            return f"moving {direction}"
        case ["go", "north"]:       # more specific later than 2-token catch
            return "north"
        case _:                     # default
            return "unknown"
```

> [!tip] `range` is the workhorse
> `range(5)` → `0..4`; `range(2, 8, 2)` → `2,4,6` (start, stop, step). It's lazy — no list is built — so `range(10**12)` is fine.

---

## 3. Data Structures (the core five)

| Type | Mutable? | Ordered? | Use it for |
|---|---|---|---|
| `list` `[a,b]` | ✅ | ✅ | sequences, stacks, queues‑ish, collections of same kind |
| `tuple` `(a,b)` | ❌ | ✅ | fixed records, function return bundles, dict keys, named records |
| `dict` `{k:v}` | ✅ | ✅ (insertion order) | key → value maps, config, objects, frequency counts |
| `set` `{a,b}` | ✅ | ❌ | membership tests, dedupe, set math |
| `frozenset` `{a,b}` | ❌ | ❌ | set that can be a dict key / in another set |

### 3.1 List

```python
xs = [10, 20, 30]
xs.append(40)                 # add one
xs.extend([50, 60])           # add many
xs.insert(1, 99)             # add at index
xs.pop()                       # remove+return last
xs.remove(20)                 # remove first occurrence of value
xs[1:3]                       # slice -> [20, 30]
xs[::-1]                      # reverse copy
xs.sort(key=lambda n: -n)     # sort desc by value
sorted(xs, reverse=True)       # returns a *new* sorted list
2 in xs                        # O(n) — use a set for O(1) membership
```

> [!warning] The classic copy bug
> `b = a` does **not** copy — both names point to the same list. To copy: `b = a[:]` (shallow) or `b = list(a)`. Deep copy (nested lists/dicts): `import copy; b = copy.deepcopy(a)`.

### 3.2 Tuple & unpacking

```python
pt = (3, 4)
x, y = pt                       # unpacking
a, b = b, a                    # swap without a temp
first, *rest = [1,2,3,4,5]    # -> first=1, rest=[2,3,4,5]
# named tuple — the "small record" idiom
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2); p.x          # -> 1  (has attribute access + index)
```

### 3.3 Dict — the workhorse

```python
cfg = {"model": "gpt-4o", "temp": 0.2, "temp": 0.0}   # dup key: last wins
cfg.get("k", default=None)   # safe access (no KeyError)
cfg.setdefault("k", {})     # insert default if missing
{a: b for a, b in pairs}    # from pairs
merged = {**a, **b}         # b's keys win

# frequency count without pandas
from collections import Counter
Counter("mississippi").most_common(2)   # [('s',4), ('i',4)]
```

> [!tip] Dict = your friend, not dataclasses' enemy
> For *ad‑hoc* config or intermediate results, a dict is the fastest to write. Reach for `dataclasses` (§13) when the shape is *stable and reused* across a codebase.

### 3.4 Set

```python
seen = set()
seen.add(3)
uniq = list(set(xs))           # dedupe (order not preserved)
a, b = {1,2,3}, {2,3,4}
a & b                          # intersection {2,3}
a | b                          # union {1,2,3,4}
a - b                          # difference {1}
a ^ b                          # symmetric difference {1,4}
```

---

## 4. Functions

### 4.1 Defining & calling

```python
def greet(name, *, times=1, loud=False):
    """Docstring — first line is help()."""
    msg = "hi " + name
    if loud:
        msg = msg.upper()
    return " ".join([msg] * times)

greet("ez")                       # positional
greet("ez", times=3, loud=True)   # keyword
```

### 4.2 Argument rules (the important ones)

```python
def f(a, b=2, *args, key=None, **kwargs):
    ...
# a            positional‑only (before the bare *)
# b            positional‑or‑keyword with a default
# *args        captures extra positional into a tuple
# key          keyword‑only (after * / ** / *args)
# **kwargs     captures extra keyword into a dict
```

> [!warning] The mutable‑default trap
> `def f(x, cache=[])` reuses the *same* list across calls — a bug waiting to happen. Use `None` sentinel: `def f(x, cache=None): cache = cache if cache is not None else []`.

### 4.3 Return & multiple values

```python
def head_tail(xs):
    return xs[0], xs[1:]        # returns a tuple
first, rest = head_tail([1,2,3,4])
```
"Multiple return" is really *one tuple return* that unpacks on the receiving side.

### 4.4 Closures & late binding

```python
# late binding: the loop variable is read at call time, not at definition time
fns = [lambda: i for i in range(3)]
[f() for f in fns]             # -> [2, 2, 2]  (bug)

# fix with a default arg that captures the value NOW:
fns = [lambda i=i: i for i in range(3)]
[f() for f in fns]             # -> [0, 1, 2]  ✓
```

> [!question] Why do the three lambdas all return 2?
> They capture the *name* `i`, not its value, and by the time you call them the loop has finished with `i == 2`. The default‑arg trick binds the current value into the closure at creation time.

---

## 5. Comprehensions & generators‑in‑one‑line

```python
nums = [1, 2, 3, 4, 5]

# list comp: the idiom
sq = [n*n for n in nums if n % 2]            # [4, 16, 25]

# dict comp
squares = {n: n*n for n in range(5)}

# set comp
uniq = {x % 10 for x in range(50)}

# generator expression — lazy, low memory (the default "big" choice)
total = sum(n*n for n in range(1_000_000))    # no list in RAM

# nested
mat = [[1,2,3],[4,5,6]]
flat = [v for row in mat for v in row]        # [1,2,3,4,5,6]
# read order: outer loop, then inner (same as nested for)
```

> [!tip] Choose the structure
> `[]` list comp = materialize now. `()` generator = stream, memory‑cheap, single pass. `{}` set/dict comp = dedupe / key‑map. **Default to generator when you just iterate once.**

---

## 6. Iterators & Generators

```python
# every generator function turns a plain `def` into a lazy producer
def countdown(n):
    while n > 0:
        yield n        # resume here next time
        n -= 1
for x in countdown(3):
    print(x)           # 3, 2, 1
```

### 6.1 `itertools` — the stdlib you wish everyone used

```python
import itertools as it

list(it.chain([1,2], [3,4]))                 # [1,2,3,4]
list(it.product("ab", [1,2]))               # [(a,1),(a,2),(b,1),(b,2)]
list(it.permutations([1,2,3], 2))            # 6 orderings
list(it.combinations([1,2,3], 2))           # 3 pairs
list(it.islice(range(10**9), 5))            # first 5 of a huge range
list(it.groupby([1,1,2,2,3,1], key=lambda x:x))   # group consecutive
next(it.islice(it.count(0), 5, 8))          # -> 5  (lazy infinite)
```

### 6.2 `functools` one‑liners

```python
from functools import reduce, lru_cache, partial, cmp_to_key

reduce(lambda a, b: a + b, [1, 2, 3, 4])     # -> 10
partial(max, key=len)                        # max that compares by length

@lru_cache(maxsize=None)                      # memoize pure functions
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)
fib(40)                                        # instant, not exponential
```

> [!question] When is `lru_cache` dangerous?
> Only when the function is **pure** (same inputs → same outputs) *and* its arguments are hashable. If the function has side effects (I/O, DB, randomness), the cache returns the first result forever — a silent bug.

---

## 7. Strings & F‑Strings (Python's killer feature)

```python
s = "hello world"
s.upper(); s.title(); s.strip()                 # transform
"a".join([1,2,3])                               # "123"
"---".join(["a","b","c"])                       # "a---b---c"
s.replace("world", "x"); s.split()              # mutate / split
"abcd".center(8, "-")                           # "--abcd--"
"123".isdigit(); "a1".isalnum()                # checkers

# f‑strings — the modern format
name, age = "ez", 30
f"{name} is {age}"                       # "ez is 30"
f"{2/3:.3f}"                            # "0.667"  (format spec)
f"{1_000_000:,}"                        # "1,000,000"
f"{0.5:.0%}"                            # "50%"
f"{2026:04d}-{1:02d}-{15:02d}"         # "2026-01-15"
f"{'x' * 10}"                          # "xxxxxxxxxx"
# multi‑line f‑string + variable inside the braces:
msg = f"""Hi {name},
you are {age}.
That's {age+1} next year."""
```

> [!tip] `f-string` > `"%s" %` > `"{}".format`
> If the string is dynamic, use an f‑string. The old `%` and `.format()` styles are still in the wild, but new code should be f‑strings.

### 7.1 Regular expressions (`re`)

```python
import re
re.findall(r"\b\w+@[\w.-]+\b", text)       # email-ish
re.sub(r"\s+", " ", "a   b\n c")          # "a b c"
if re.search(r"\d{3}-\d{4}", s): ...      # presence test
m = re.match(r"^(\w+)=(\w+)$", "k=v")     # full match
m.group(1), m.group(2)                    # 'k', 'v'
```

> [!note] Raw strings for patterns
> Always use `r"..."` so backslashes aren't eaten by the string layer. `r"\d"` is the regex digit class; `"\d"` in a plain string is just `\d` (Python doesn't know what that means, so it's left as `\d` but the intent is murkier).

---

## 8. Classes & OOP

### 8.1 The minimal class

```python
class Counter:
    def __init__(self, start=0):
        self.n = start
    def inc(self, k=1):
        self.n += k
    def __repr__(self):
        return f"Counter({self.n})"
    def __eq__(self, other):
        return isinstance(other, Counter) and self.n == other.n
    def __hash__(self):
        return hash(self.n)

c = Counter(3); c.inc(); c.inc(10)     # Counter(14)
```

### 8.2 Inheritance & method resolution

```python
class Animal:
    def speak(self): return "..."
class Dog(Animal):
    def speak(self): return "woof"
    def fetch(self): return True

class Lab(Dog):
    pass
Lab().speak()                           # "woof" (MRO: Lab -> Dog -> Animal -> object)
```

> [!warning] `super()` is not optional
> When you override `__init__` in a subclass that *has* a parent `__init__`, call `super().__init__(...)` to let the parent finish setting up. Forgetting it is the classic "my state is missing" bug.

### 8.3 Class vs instance data

```python
class Model:
    VERSION = "1.0"          # class attribute: shared across all instances
    def __init__(self):
        self.seed = 42      # instance attribute: unique per object
```

### 8.4 `@property` — the computed field

```python
class Temp:
    def __init__(self, celsius):
        self.c = celsius
    @property
    def fahrenheit(self):
        return self.c * 9/5 + 32
    @fahrenheit.setter
    def fahrenheit(self, val):
        self.c = (val - 32) * 5/9
```

### 8.5 `@dataclass` — boilerplate‑free records

```python
from dataclasses import dataclass, field

@dataclass
class PipelineConfig:
    model: str
    temperature: float = 0.0
    max_tokens: int = 512
    extra: dict = field(default_factory=dict)   # mutable defaults: use default_factory
```
`@dataclass` auto‑generates `__init__`, `__repr__`, `__eq__`, and (with `frozen=True`) `__hash__`.

### 8.6 `__slots__` — memory‑tight classes

```python
class Point:
    __slots__ = ("x", "y")       # no __dict__; faster & smaller
    def __init__(self, x, y):
        self.x = x; self.y = y
```

> [!question] When would you reach for `__slots__`?
> When you have *thousands* of small objects of the same class and memory / speed matter (graph nodes, particles, rows). Rare for app code; common in data structures and hot loops.

---

## 9. Modules, Packages & `__main__`

### 9.1 Modules in one file

```python
# utils.py
def slug(s): ...
PI = 3.14159
```

```python
# other.py
import utils
from utils import slug, PI
import utils as u           # alias

if __name__ == "__main__":   # runs only when executed *directly*, not when imported
    print("run me")
```

### 9.2 Package layout

```
mypkg/
  __init__.py          # optional now; marks a package
  __main__.py          # `python -m mypkg` entry point
  a.py
  sub/
    __init__.py
    b.py
```

```python
from mypkg.a import foo
from mypkg.sub.b import bar
import mypkg.a as a_module
```

> [!tip] `__init__.py` and re‑exports
> Drop `from mypkg.a import *` (or explicit imports) into `mypkg/__init__.py` and `import mypkg` exposes them. Keeps your public surface small and predictable.

### 9.3 Relative vs absolute imports

```python
from .a import foo          # relative (inside a package)
from mypkg import a         # absolute (anywhere)
```
Relative imports only work *inside* a package; top‑level scripts must use absolute imports.

---

## 10. Errors & Exceptions

```python
try:
    int("abc")
except ValueError as e:
    print("bad value:", e)
except (TypeError, KeyError):
    print("other bad input")
else:
    print("only runs if NO exception")
finally:
    print("always runs (cleanup)")
```

### 10.1 Raise & custom

```python
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b

class AppError(Exception):
    """Custom exception type."""
    def __init__(self, code, msg):
        super().__init__(msg)
        self.code = code

raise AppError(404, "not found")
```

> [!warning] Broad `except:` is a smell
> `except Exception:` is sometimes defensible; `except:` swallows even `KeyboardInterrupt` and `SystemExit`. **Catch the specific exception you expect, re‑raise or handle the rest.** And never `except: pass` — hide a bug, ship a bug.

---

## 11. Files & IO

### 11.1 The modern idiom: `with open(...)`

```python
# write
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("line 1\n")

# read all / line‑by‑line / binary
with open("data.csv") as f:
    all_text = f.read()
    first_lines = f.readlines()[:3]

with open("big.bin", "rb") as f:
    chunk = f.read(4096)       # stream in chunks for huge files
```

### 11.2 Standard IO + pathlib

```python
from pathlib import Path
p = Path("data").glob("*.csv")
for f in p:
    print(f.name, f.stat().st_size)

# read a whole CSV
import csv
with open("x.csv", newline="") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["age"])

# json
import json
data = json.load(open("x.json"))
with open("y.json", "w") as f:
    json.dump(obj, f, indent=2)
```

> [!tip] `pathlib` over `os.path`
> For new code, `Path` is cleaner: `Path("a/b").joinpath("c.txt")`, `p.suffix`, `p.read_text()`, `p.exists()`. It's still built on the same OS calls — just nicer.

---

## 12. Lambdas, `sorted`, and `functools` idioms

```python
# sorted with a key: the single most common "fancy" sort
players = [ {"n":"a","s":10}, {"n":"b","s":5}, {"n":"c","s":20} ]
sorted(players, key=lambda p: -p["s"])            # desc by score
sorted(players, key=lambda p: (p["s"], p["n"]))  # tiebreak

# group by a key (manual "groupby")
from collections import defaultdict
by_team = defaultdict(list)
for r in records:
    by_team[r.team].append(r)
```

### 12.1 `functools` one‑liners that earn their keep

```python
from functools import lru_cache, reduce, partial, cmp_to_key, wraps

@lru_cache(maxsize=None)
def memo(n): ...

reduce(lambda acc, x: acc | x, [1,2,4], 0)        # bitwise OR  -> 7
partial(int, base=16)                              # hex‑only int parser
```

---

## 13. Type Hints (PEP 484 / 585)

```python
from typing import Optional, Union, Callable, Generic, TypeVar
import json

T = TypeVar("T")

def f(a: int, b: str, c: list[int] | None = None) -> dict[str, int]: ...
# modern (3.10+) built‑in generics replace typing.List/Dict/etc.

class Box(Generic[T]):
    def __init__(self, v: T): self.v = v

Handler = Callable[[str], bool]   # a function type alias

Union[int, str]                   # -> int | str in 3.10+
Optional[int]                     # -> int | None in 3.10+
```

> [!note] Type hints are advisory, not enforced
> The interpreter ignores them. Use **`mypy`** or **`pyright`** to check. They *dramatically* improve DX on any non‑trivial project.

---

## 14. Decorators & Context Managers

### 14.1 The two canonical decorators

```python
import functools, time

def timing(fn):
    @functools.wraps(fn)              # preserve __name__, __doc__
    def wrapper(*a, **kw):
        t0 = time.perf_counter()
        out = fn(*a, **kw)
        print(f"{fn.__name__} took {time.perf_counter()-t0:.3f}s")
        return out
    return wrapper

@timing
def slow(): ...

def retry(times=3):
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*a, **kw):
            for i in range(times):
                try: return fn(*a, **kw)
                except Exception as e:
                    if i == times-1: raise
        return wrapper
    return deco

@retry(times=5)
def flaky_call(): ...
```

### 14.2 Context managers — the `with` statement

```python
# built‑in
with open("f.txt") as f: ...
with lock:
    shared.append(x)

# custom
import contextlib
class Tracker:
    def __enter__(self):
        print("enter"); return self
    def __exit__(self, exc_type, exc, tb):
        print("exit"); return False    # returning True suppresses the exception

# functional
@contextlib.contextmanager
def timer():
    t0 = time.time()
    yield
    print(f"{time.time()-t0:.3f}s")
with timer() as _t:
    do_work()
```

> [!tip] `contextlib` is the fastest path
> For one‑off context managers, `@contextlib.contextmanager` beats writing `__enter__`/`__exit__` by hand — 4 lines instead of 10.

---

## 15. Concurrency

### 15.1 Threading — the GIL and when to use threads

Python's GIL (Global Interpreter Lock) means **only one thread runs Python bytecode at a time**. Threads are useful for:
- I/O‑bound work (network, disk) — the GIL is released while waiting.
- Using C extensions that release the GIL.

They are *not* a substitute for true CPU parallelism.

```python
import threading, time
def worker(n):
    time.sleep(0.1)
    print(n)

ts = [threading.Thread(target=worker, args=(i,)) for i in range(5)]
[t.start() for t in ts]
[t.join() for t in ts]
```

### 15.2 `threading` for I/O

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
def fetch(url): ...
with ThreadPoolExecutor(max_workers=10) as ex:
    futs = [ex.submit(fetch, u) for u in urls]
    for f in as_completed(futs):
        print(f.result())
```

### 15.3 `multiprocessing` for CPU

```python
from concurrent.futures import ProcessPoolExecutor
import os
def square(n): return n*n
with ProcessPoolExecutor() as ex:
    print(list(ex.map(square, range(10))))
```

> [!warning] `multiprocessing` gotchas
> On Linux use the default **fork** start method. On macOS / Windows use **spawn** and mark the entrypoint with `if __name__ == "__main__":`. Modules you import must be picklable — top‑level functions only.

### 15.4 `asyncio` — the modern I/O concurrency

```python
import asyncio
async def fetch(i):
    await asyncio.sleep(0.1)
    return i
async def main():
    results = await asyncio.gather(*[fetch(i) for i in range(10)])
    print(results)
asyncio.run(main())
```

> [!tip] Pick the right tool
> | Work | Tool |
> |---|---|
> | Many concurrent I/O requests | `asyncio` (one process) or `ThreadPoolExecutor` (easier to start) |
> | CPU‑heavy jobs | `multiprocessing` / `ProcessPoolExecutor` / move to C / Rust / GPU |
> | Trivial background work | `threading` |
> Don't reach for asyncio for a 50‑line script; reach for a thread pool or just run sequentially. |

---

## 16. The stdlib — the use cases that pay off

```python
# dates & times — the stdlib is *surprising* good
from datetime import datetime, date, timedelta
datetime.now()
date.today() + timedelta(days=7)
(datetime.now() - start).total_seconds()

# hashing
import hashlib
hashlib.md5(b"x").hexdigest()
hashlib.sha256(b"x").digest()

# compression
import gzip, zipfile
gzip.open("big.txt.gz", "rt").read()

# subprocess
import subprocess
result = subprocess.run(["git", "status"], capture_output=True, text=True)
result.stdout

# os / file ops
import os, shutil
shutil.copytree("src", "dst")

# logging (use this, not print, in libraries)
import logging
logger = logging.getLogger(__name__)
logger.info("started %s", arg)

# argparse — the real CLI framework
import argparse
p = argparse.ArgumentParser()
p.add_argument("name")
p.add_argument("--count", "-c", type=int, default=1)
ns = p.parse_args()

# tempfile / uuid
import uuid, tempfile
uuid.uuid4()
tempfile.mkdtemp()

# math
import math
math.isclose(a, b, rel_tol=1e-9)     # the right float comparison
math.factorial, math.gcd, math.pi

# random — the *seeded* kind
import random
random.seed(42); random.sample([1,2,3,4,5], 2)

# itertools (already shown) + collections (already shown)
```

> [!info] stdlib modules you'll actually use daily
> `json`, `csv`, `os`/`pathlib`, `datetime`, `argparse`, `logging`, `subprocess`, `tempfile`, `collections`, `itertools`, `functools`, `hashlib`. Most of everything else is in a library — that's fine.

---

## 17. The Gotchas Section (save this one)

> [!warning] Python's five silent killers
> 1. **Mutable default args** — `def f(x, cache=[])` reuses the same list. Use `None` sentinel.
> 2. **Late‑binding closures** — `[lambda: i for i in range(3)]` captures the last value. Freeze with `lambda i=i: i`.
> 3. **Shallow copy by default** — `list.copy()` / `a = b[:]` shares nested objects. Use `copy.deepcopy` when needed.
> 4. **`==` vs `is`** — `==` is value; `is` is identity. `None` checks: `is None`, never `== None`.
> 5. **Mutating a dict/list while iterating** — `for x in d: del d[x]` → `RuntimeError`. Iterate a *copy*: `for x in list(d)`.

> [!note] Floats lie
> `0.1 + 0.2 != 0.3` (it's `0.30000000000000004`). Use `math.isclose(a, b)` or `Decimal` for money.

> [!note] Timezones bite
> `datetime.now()` is naive (no tz). `datetime.now(timezone.utc)` is aware. Mixing them raises `TypeError` in 3.6+.

> [!note] `bool` is an `int`
> `True + True == 2`, `sum([True, False, True]) == 2`, and `True in [1, 0]` is `True`. If your sum counts booleans as ints, that's expected — but know it.

> [!note] Unicode ≠ str length
> `"é".__len__()` can be 1 *or* 2 depending on how it's encoded. `range(len(s))` is not the way to index; use `for c in s:`.

---

## 18. Self‑Test (active recall)

> [!question] `x = [1,2]; y = x; y.append(3)` — what is `x`?
> `[1, 2, 3]`. Names are aliases, not copies. To get independent state: `y = x[:]` or `list(x)` (shallow), `copy.deepcopy(x)` (deep).

> [!question] What does `f(x, cache=None)` do differently from `f(x, cache=[])`?
> `cache=None` makes a *new* `[]` per call when the user doesn't pass one. `cache=[]` reuses the *same* list for every call — state leaks across invocations.

> [!question] `isinstance(True, int)` is `True`. Why does that matter?
> Because `True` *is* an `int` subclass (value 1), `sum([True, False, True]) == 2` and `bool in int‑context` comparisons can do surprising things. Know the edge cases when you count booleans.

> [!question] Name the three most useful `collections` types and when you'd pick each.
> `Counter` (frequency counts), `defaultdict` (dict that auto‑inits missing keys, e.g. `defaultdict(list)`), `deque` (fast append/pop on both ends). Reach for `Counter` for any "count these" problem.

> [!question] Why does `random.seed(42)` exist, and when do you *not* want it?
> It makes a run reproducible — critical for tests and experiments. Don't seed when you genuinely want random (a UUID, a random port, a nonce).

> [!question] What are the *real* limits of `@lru_cache`?
> (a) arguments must be hashable (lists/dicts aren't), (b) the function must be pure, (c) unbounded `maxsize=None` can OOM on high‑cardinality inputs.

> [!question] `for x in d: del d[x]` fails. Why, and how do you do it?
> Mutating the container while iterating raises `RuntimeError`. Iterate a *copy*: `for x in list(d): del d[x]`.

> [!question] `Path("a/b") / "c.txt"` vs `os.path.join("a","b","c.txt")` — which do you write in 2026?
> `Path`, and specifically `Path("a/b/c.txt").read_text()` for reads, `write_text()` for writes. It composes better than `os.path` string ops.

---

## 19. Advanced Syntax (the "wait, Python can *that*?" tier)

> [!note] Where this fits
> You won't write most of this daily, but when it shows up in a codebase or a library, you should *recognize* it. These are the features that separate "I know Python" from "I know *the language*."

### 19.1 Unpacking & extended assignment

```python
a, b, c = 1, 2, 3
first, *mid, last = [1,2,3,4,5]     # -> first=1, mid=[2,3,4], last=5
# starred unpacking in function args
def head_tail(x, *ys, z): ...        # *ys collects the middle positional args
```

### 19.2 `contextlib` recipes

```python
import contextlib

@contextlib.contextmanager
def db_connection():
    conn = connect()
    try:
        yield conn
    finally:
        conn.close()

with contextlib.suppress(FileNotFoundError):
    os.remove("maybe_missing.txt")   # no error if the file wasn't there

with contextlib.ExitStack() as stack:
    f = stack.enter_context(open("a"))
    g = stack.enter_context(open("b"))
    # both auto-close at end of block — no nested-with juggling
```

### 19.3 The dunder cookbook (protocol methods)

| Method | Makes `...` work as |
|---|---|
| `__init__` | `Type(args)` |
| `__repr__` / `__str__` | `repr(o)` / `print(o)` / `f"{o}"` |
| `__eq__` / `__hash__` | `==` / dict‑key / set |
| `__len__` / `__getitem__` / `__iter__` | `len(o)` / `o[i]` / `for` |
| `__add__` / `__radd__` | `a + b` |
| `__enter__` / `__exit__` | `with o:` |
| `__call__` | `o()` — make an object callable |

```python
class Money:
    def __init__(self, cents): self.c = cents
    def __eq__(self, o):       return isinstance(o, Money) and self.c == o.c
    def __add__(self, o):      return Money(self.c + o.c)
    def __repr__(self):        return f"${self.c/100:.2f}"
    def __hash__(self):        return hash(self.c)
Money(100) + Money(50)         # -> $1.50
```

> [!tip] Override `__eq__` ⇒ define `__hash__` (or make it unhashable)
> A dict‑keyable object must define *both* `__eq__` and `__hash__` consistently, or set `__hash__ = None`. Forgetting `__hash__` after overriding `__eq__` makes your object unusable in sets/dicts.

### 19.4 Protocols (structural typing)

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Sized(Protocol):
    def __len__(self) -> int: ...

def report(x: Sized):
    return f"len {len(x)}"
report([1,2,3])   # any object with __len__ qualifies — no inheritance needed
```

### 19.5 Generics & `TypeVar` in practice

```python
from typing import Generic, TypeVar
T = TypeVar("T")
class Stack(Generic[T]):
    def __init__(self): self._xs = []
    def push(self, x: T): self._xs.append(x)
    def pop(self) -> T: return self._xs.pop()
s: Stack[str] = Stack[str]()   # checked by mypy, not at runtime
```

---

## 20. Structured & Functional Patterns

```python
from enum import Enum, auto
from dataclasses import dataclass

class Color(Enum):
    RED = auto(); GREEN = auto(); BLUE = auto()
Color("RED")   # reverse lookup; list(Color) = all members

@dataclass(frozen=True)       # immutable record
class Point:
    x: float; y: float
    def translate(self, dx, dy): return Point(self.x+dx, self.y+dy)

def report(event: dict):
    match event:
        case {"type": "login", "user": u}:  handle_login(u)
        case {"type": "logout"}:           handle_logout()
        case _:                            log_unknown(event)
```

---

## 21. Packaging, Testing & Quality

```toml
# pyproject.toml (PEP 621) — the dependency manifest
[project]
name = "mymodel"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = ["numpy>=1.26,<2", "pandas>=2.0,<3"]
[project.optional-dependencies]
dev = ["pytest", "ruff", "mypy"]
[build-system]
requires = ["setuptools>=68"]
```

```python
# a focused pytest example — test *behavior*, never a frozen snapshot value
@pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (5, 120)])
def test_factorial(n, expected):
    assert math.factorial(n) == expected
```

```bash
ruff check .     # lint + format (one fast tool)
mypy src/        # type errors before they run
```

---

## 22. Extended Gotchas (the deeper list)

> [!warning] More silent killers
> - **`global` is a red flag** — refactor to pass state explicitly instead.
> - **`dict.get` returns `None` (falsy)** — use `d.get("k", 0)` for a safe default.
> - **Rebinding vs mutating** — `xs = xs + [9]` makes a *new* list; `xs.append(9)` mutates in place.
> - **`range` vs list** — `for i in range(10)` is O(1) memory; `list(range(10))` is O(n).
> - **Strings are immutable** — `s += "x"` in a loop is O(n²); build a list and `"".join`.
> - **`in` on a list is O(n)** — convert to a `set` first for repeated membership tests.
> - **`float('nan') != float('nan')`** — NaN is not equal to itself; use `math.isnan`.
> - **Iterating a dict while adding/removing keys** raises `RuntimeError`; iterate a copy.

---

## 23. Quick "Which Built‑in?" Decision Table

| Problem | Use |
|---|---|
| count occurrences | `collections.Counter` |
| group items by key | `defaultdict(list)` |
| fast add/remove both ends | `collections.deque` |
| unique, order‑agnostic | `set` |
| unique, keep order | `list(dict.fromkeys(xs))` |
| memoize a pure function | `@functools.lru_cache` |
| a function that's half a value | `functools.partial` |
| a lazy sequence | a generator (`yield`) function |
| a named record | `@dataclass` |
| a fixed set of constants | `enum.Enum` |
| a CLI | `argparse` |
| read CSV / JSON | `csv` / `json` stdlib |
| a file, safely | `with open(...) as f:` |
| concurrent I/O | `asyncio` / `ThreadPoolExecutor` |
| concurrent CPU | `multiprocessing` / `ProcessPoolExecutor` |

---

## 24. More Self‑Tests (advanced tier)

> [!question] `Stack[str]()` — what happens at runtime?
> Nothing special. Generics are **type‑level only**; the interpreter sees plain `Stack()`. `mypy` does the checking. "Duck typing with a linter."

> [!question] Why `field(default_factory=list)` and not `field(default=[])`?
> The default value is **shared** across all instances — one `[]` mutated by every object. `default_factory` calls a function per instance for a fresh list.

> [!question] You override `__eq__`. What else for the object to stay hashable?
> Define a matching `__hash__`, or set `__hash__ = None` to declare it unhashable. Otherwise Python makes it unhashable automatically.

> [!question] Fastest way to dedupe a list while preserving order?
> `list(dict.fromkeys(xs))` — dicts keep insertion order (3.7+) and it's C‑speed.

> [!question] `match` + `case` vs `if cmd == ...`?
> `match` binds sub‑values to names, matches *structure* (keys, sequences, types), and gives a `case _` default — the closest Python gets to Rust's `match`.

---

## Related Notes

- [[Python]] ← full language & stdlib reference (syntax, use cases, gotchas)
- [[Python for AI]] — the *ML/AI stack* on top of this (NumPy, Pandas, scikit‑learn, LLM clients, MLOps).
- [[Programming_for_AI_Weeks_4-6]] — the course‑module version of this material.
- [[AI Engineering]] — how Python code gets shipped as a system.
- [[Prompt Engineering]] — the "ask" side of LLM apps.
- [[Generative AI - Map of Content]] — the cluster hub.

*This note is the **language** reference. When you need to know "how do I …?" in Python, this is the page. When you need to know "how do I do ML/AI with Python?", go to [[Python for AI]].*
