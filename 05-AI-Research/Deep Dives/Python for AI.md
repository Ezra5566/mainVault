---
tags: [python, numpy, pandas, sklearn, mlops, references]
aliases: [Python for ML, Python AI Stack]
updated: 2026
status: reference
---

# Python for AI

> [!abstract] What this note is
> A working reference for the *specific* Python an AI/ML engineer actually uses daily — from the core language to the numerics stack, the ML/LLM libraries, the tooling that makes a project reproducible, and the code patterns that survive review. Python is the language of AI, so depth here is depth in the field.
>
> Companion deep dives: [[AI Engineering]] (the *ship*), [[Prompt Engineering]] (the *ask*). Hub: [[Generative AI - Map of Content]].

---

## 1. Why Python Is the AI Language

- **Readable and fast to write** — you iterate on experiments, so language overhead must be low.
- **A single ecosystem owns the numerics** — NumPy, Pandas, SciPy underpin nearly everything above.
- **Dynamic + typed** — you can prototype fast *and* add type hints when a module gets reused.
- **Bridges to fast runtimes** — the real compute happens in C/CUDA; Python is the driver. (The slowness of pure Python is not the bottleneck in an ML pipeline; tensor math runs in compiled backends.)

The practical split: **Python for orchestration, NumPy/PyTorch/TensorFlow for the heavy math, a compiler for anything latency‑critical.**

---

## 2. The Core Language You'll Use Constantly

### 2.1 Data structures that matter
- **Lists / tuples** — features, sequences. Tuples for immutable records.
- **Dicts** — the workhorse: config, feature maps, JSON, model parameters (`model.state_dict()` is a dict).
- **Sets** — dedup, membership checks.
- **List/dict comprehensions** — write them; they're the idiom. `{k: v for k,v in ... if ...}` beats a loop.

### 2.2 Functions, arguments, and defaults
- Positional vs keyword, default values, `*args`/`**kwargs`.
- **Immutable defaults are safe** (`def f(x, opts=None)` → `opts = opts or {}`), because a mutable default is shared across calls.

```python
def predict(row, cfg=None):
    cfg = cfg or {}          # safe default
    return model(row, temperature=cfg.get("temperature", 0.0))
```

### 2.3 Classes / OOP (you will meet them in every framework)
- A **model**, a **pipeline**, an **agent**, a **dataset** are all classes. Understand `__init__`, methods, and when a plain function is simpler than a class.
- **Inheritance** shows up (subclassing `torch.nn.Module`, a base `Pipeline`), but prefer **composition** (small, testable pieces) over deep hierarchies.

### 2.4 Python specifics that bite
- **Late‑binding closures** in loops — capture loop vars correctly (`for i in range(n): f = lambda: i` captures the *last* `i`; use `default=` to freeze).
- **`None` vs falsy** — `0`, `""`, `[]` are all falsy; check `is None` when a value of `0`/empty is meaningful.
- **Floats** — `0.1 + 0.2 != 0.3`; use tolerance (`math.isclose`) for comparisons.
- **Immutability of strings/tuples**, **in‑place vs rebind** for lists/dicts.

---

## 3. The Numerics Stack (the actual "AI Python")

### 3.1 NumPy
The foundation. Vectors/matrices are `ndarray`s; *all* linear algebra in AI is expressed this way.

```python
import numpy as np
x = np.array([[1, 2, 3],
              [4, 5, 6]])          # shape (2, 3)
x.T                                  # transpose
A @ B                               # matrix multiply (matmul)
np.dot(w, x)                        # dot product
y = A @ w + b                        # a forward linear layer, in one line
```

Concepts to be fluent in: **shape, dtype, broadcasting** (the rules that let a `(2,3)` matrix meet a `(3,)` vector without explicit loops), **vectorization** (do the whole array at once — 10× faster than a Python loop, and the point of NumPy), **axis** (which dimension an operation reduces over).

**Broadcasting, the one thing to internalize:** operations align arrays by *shape* from the back. A `(3,)` vector broadcasts against every row of a `(2,3)` matrix — that's how a single layer's weights + bias apply to a whole batch at once:

```python
import numpy as np
W = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])      # shape (2, 3): 2 examples, 3 features
b = np.array([0.1, 0.2, 0.3])        # shape (3,):    one bias per feature
X = W + b                            # (2,3) + (3,) -> (2,3), no loop
z = W @ np.array([0.1, 0.2, 0.3])    # (2,3) @ (3,)  -> (2,), one output per example

# vectorization: compute per-row norms without a Python for-loop
row_norms = np.linalg.norm(W, axis=1)   # shape (2,)
# rule of thumb: if you find yourself writing `for` over array rows, NumPy has an op for it
```

> [!tip] The whole "batch" idea is broadcasting
> A "batch of 1000 examples" is just a `(1000, 3)` array. Every layer op broadcasts the same weights over all 1000 rows — that's why a single line of Python can process a whole batch on the GPU.

See [[linear_algebra_vectors]] and [[matrices]] for the math underneath; NumPy is the syntax for it.

### 3.2 Pandas
Tables of *labeled* data — the natural shape of datasets (rows = examples, columns = features).

```python
import pandas as pd
df = pd.read_csv("data/train.csv")
df.describe()                       # quick statistics
df.groupby("class").mean()         # aggregates per class
df["feat"] = df["a"] / (df["b"] + 1e-9)   # feature engineering
X = df[cols].values                 # to a NumPy array for the model
```

Fluency target: **load → clean (missing, outliers, types) → feature‑engineer → split → hand to NumPy/ML lib.** Know when Pandas is *too slow* (large data → use Polars or Dask).

### 3.3 SciPy
Sparse matrices (`scipy.sparse` — most real data is sparse), optimization (`scipy.optimize`), statistics.

### 3.4 scikit‑learn — the classical ML baseline
The first thing to reach for before a neural net:

```python
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import accuracy_score, f1_score

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)
print(f1_score(y_test, model.predict(X_test)))
```

Fluency: the **`fit` / `predict` / `score`** API is *the* interface — PyTorch and most frameworks mirror it.

---

## 4. The LLM / Generative Side

### 4.1 Talking to a model in Python
The two main paths:
- **API** (OpenAI, Anthropic, local servers): a small client call.

```python
import json
from openai import OpenAI
client = OpenAI()

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    temperature=0.0,                     # deterministic for extraction
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": "You extract fields. Reply JSON only."},
        {"role": "user",     "content": text},
    ],
)
data = json.loads(resp.choices[0].message.content)   # parse + validate
```

- **Self‑hosted / open‑weight** (`transformers`, `llama.cpp`, `vLLM`):

```python
from transformers import pipeline
gen = pipeline("text-generation", model="mistral-7b")
out = gen("classroom: " + question, max_new_tokens=128)
```

Both patterns: **build the prompt, call the model, parse/validate the output, retry on failure.** See [[Prompt Engineering]] and [[AI Engineering]] §4 for the surrounding system.

### 4.2 Jupyter for exploration
An AI project starts in a **notebook**: load data, eyeball it, prototype a model, plot results. When it works, *extract the logic into `.py` modules* — a notebook is for exploration, a package is for reuse. (Keep the notebook thin; keep the real code in importable files.)

---

### 4.3 A Fully‑Worked Pipeline (copy this and run it)

This is the *shape* of a real AI project in one file — classical baseline + an LLM comparison, with the reproducibility habits built in. It's the §8 first project, written out so you can actually run it.

```python
# pipeline.py  —  data -> baseline -> LLM compare -> evaluate
import json, random, hashlib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score

SEED = 42                      # reproducible runs start with a fixed seed
random.seed(SEED); np.random.seed(SEED)

def load_and_split():
    df = pd.read_csv("data/support_tickets.csv")
    # clean: fill missing, engineer one feature
    df["n_words"] = df["text"].str.split().str.len()
    X = df[["n_words", "priority_int"]]
    y = (df["category"] == "urgent").astype(int)
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, random_state=SEED,
                                              stratify=y, test_size=0.2)
    return X_tr, X_te, y_tr, y_te

def run_baseline():
    X_tr, X_te, y_tr, y_te = load_and_split()
    rf = RandomForestClassifier(n_estimators=200, random_state=SEED)
    rf.fit(X_tr, y_tr)
    pred = rf.predict(X_te)
    print(f"[baseline]  RF  f1 = {f1_score(y_te, pred):.3f}")
    return rf

def run_llm(tickets, model="gpt-4o-mini"):
    # a structured, validated LLM call on a sample — see [[Prompt Engineering]] §5
    from openai import OpenAI
    client = OpenAI()
    out = []
    for t in tickets.sample(50, random_state=SEED)["text"]:
        prompt = ('Classify as urgent or not. Reply ONLY JSON: '
                  '{"urgent": bool, "why": str}. Text: ' + t)
        r = client.chat.completions.create(
            model=model, temperature=0.0,
            response_format={"type": "json_object"},
            messages=[{"role": "user", "content": prompt}])
        out.append(json.loads(r.choices[0].message.content))
    return out   # cost/latency/quality vs the baseline is the whole exercise

if __name__ == "__main__":
    run_baseline()
    print("[llm] run the LLM sample in a notebook cell and compare")
```

> [!tip] Why this file matters more than any single concept
> It shows the **seams** between every layer: Pandas loads/cleans, scikit‑learn builds the baseline, the LLM call adds the "is it worth it?" comparison, and `SEED` + `random_state` + a pinned model name make the run reproducible. When you understand *where each piece hands off to the next*, you can debug any of them in isolation.

> [!question] This code uses `random_state` / `SEED` in three places. What breaks if you delete all of it?
> Your results no longer reproduce: the split changes, the forest uses a different random draw, the LLM sample is different. You lose the ability to say "this run is a result" — it becomes an anecdote. Fixed randomness is what separates an experiment from a fluke.

---

## 5. Project Tooling — What Makes It Reproducible

This is where a hobby project becomes engineering.

- **Environment management** — pick one and be consistent:
  - `venv` / `pip` + a lockfile (lightweight, default),
  - `uv` (fast modern pip/venv replacement),
  - `conda` / `micromamba` (when you need compiled science packages across the whole env).
- **Dependencies** — `pyproject.toml` (PEP 621 metadata + build config). Pin or bound your versions; an unpinned `numpy` is a landmine.
- **Reproducible runs** — fix the **seed** (`random`, `np.random`, `torch.manual_seed`), log the exact dataset version, code SHA, and library versions. A run you can't recreate is not a result.
- **Testing** — `pytest`. Test the *logic* (data transforms, prompt builders, output validators), not the model's exact output. A golden‑set test on your LLM prompt is a regression test (see [[Prompt Engineering]] §6).
- **Lint/type/format** — `ruff` (lint + format in one) and `mypy` (type checking). Type hints on public functions catch bugs before they run.
- **Experiment tracking** — `mlflow` or W&B: log every run's hyperparameters, metrics, and artifacts so "which run was that?" is answerable.
- **Versioning** — `git` for code; `DVC` / LakeFS for *data* (it's too big for git).

---

## 6. Code Patterns an AI Engineer Actually Writes

### 6.1 A configurable, typed pipeline
```python
from dataclasses import dataclass

@dataclass
class PipelineConfig:
    model: str
    temperature: float = 0.0
    max_tokens: int = 512
    top_k_docs: int = 5

def run(doc: str, cfg: PipelineConfig = PipelineConfig()) -> dict:
    ctx = retrieve(doc, top_k=cfg.top_k_docs)      # RAG
    prompt = build_prompt(doc, ctx, cfg)
    out = call_llm(prompt, model=cfg.model, temp=cfg.temperature)
    return validate(out)                            # structured output
```

### 6.2 Data‑loading as a class (the standard interface)
```python
from collections.abc import Iterable

class TicketDataset(Iterable):
    def __init__(self, df):
        self.source = df
    def __iter__(self):
        for row in self.source.itertuples(index=False):
            yield transform(row)      # feature engineering happens here, one row at a time
```

### 6.3 Fail‑fast validation at the boundaries
- Validate *inputs* (schemas, ranges) and *LLM outputs* (JSON + Pydantic) immediately.
- Retry structured outputs once or twice on parse failure, with the error in the message.
- Log PII‑stripped versions; never log the raw secret‑containing prompt.

### 6.4 Caching to control cost
```python
@cache_by(lambda p: p.model + p.prompt_hash)   # your own memoization
def call_llm(prompt): ...
```
See [[AI Engineering]] §8 for the cost levers.

---

## 7. Mapping the Python World Onto the Class

| Topic | Where it lives in this vault |
|---|---|
| Data structures, functions, OOP, APIs, first libraries | [[Programming_for_AI_Weeks_4-6]] |
| Linear algebra (vectors, matrices, shape) | [[linear_algebra_vectors]], [[matrices]] |
| Calculus (the "why" of gradients) | [[calculus_basics]] |
| Probability / statistics | [[probability_and_statistics]] |
| The ML algorithms themselves | [[Machine_Learning_Core_Module]], [[Deep_Learning_Weeks_6-8]] |
| Generative models, LLMs, RAG, agents | [[Generative_AI_Weeks_8-9]], [[AI Engineering]], [[Prompt Engineering]] |

This note is the **code layer** that connects all of them: NumPy expresses the linear algebra, scikit‑learn/PyTorch express the ML, and the LLM client patterns express the generative stack.

---

## 8. A "First Project" to Tie It Together

A single build that uses *all* of the above:

1. **Data (Pandas)** — load a CSV of, e.g., support tickets.
2. **Clean + features (Pandas/NumPy)** — handle missing values, engineer a sentiment flag.
3. **Baseline (scikit‑learn)** — a LogisticRegression or RandomForest classifier; report `f1_score` with cross‑validation.
4. **LLM comparison (transformers/OpenAI client)** — have a small LLM label the same tickets with a structured JSON prompt; compare cost, latency, and accuracy vs the baseline.
5. **Evaluate** — a golden set + an error analysis of the 20 worst.
6. **Ship it** — a FastAPI endpoint wrapping the chosen model, Docker‑ized, with a CI test on the eval set and a caching layer for cost.

Steps 1–3 prove classical ML; step 4 introduces the LLM trade‑offs; steps 5–6 are the AI‑engineering discipline. That single project is a portfolio piece (see [[AI Portfolio Strategy]] and [[Industry_Skills_Resume_Portfolio]]).

---

## 9. Self‑Test (active recall)

> [!question] You wrote a Python `for` loop over 100,000 rows to add a feature. A reviewer says it's too slow. What's the Python‑idiomatic fix?
> **Vectorize with Pandas/NumPy:** `df["feat"] = df["a"] / (df["b"] + 1e-9)` does the whole column at once in compiled C, not a Python loop. Rule of thumb: if you're looping over *rows*, there's almost always a vectorized op for it.

> [!question] `x = np.array([[1,2,3],[4,5,6]])`. What's `x.T.shape`, and what does `x @ x.T` give you?
> `x.T.shape` is `(3, 2)`. `x @ x.T` is a `(2, 2)` matrix — dot each row against every row (a Gram / similarity matrix). This is exactly how you get pairwise similarities between examples.

> [!question] scikit‑learn's `model.fit(X, y)` then `model.predict(X)` — what do you do to *check* it's any good before trusting it?
> `train_test_split`, then fit on train, predict on **test**, and report a *metric* (`f1_score`, `accuracy_score`, `RMSE`) — and compare it to a dumb baseline. A model that can't beat "guess the majority class" adds no value.

> [!question] Why do you keep a `requirements`/`pyproject` lockfile *and* a data version (DVC) for an ML project?
> Because a result depends on **both** the code *and* the data. Pinning only the code means a re‑run on today's data can differ from last week's. "Which dataset did this run use?" must be answerable.

> [!question] You're choosing `venv+pip`, `uv`, or `conda` for a project that needs a GPU‑accelerated library. What drives the choice?
> Not ideology — **reproducibility and the ecosystem**. `uv` for fast, lightweight pinning; `conda`/`micromamba` when you need compiled science packages and a whole‑env snapshot; `venv` for the default. Pick one and stay consistent so a teammate can recreate your env.

---

## Related Notes
- [[Python]] ← full language & stdlib reference (syntax, use cases, gotchas)
- [[AI Engineering]]
- [[Prompt Engineering]]
- [[Programming_for_AI_Weeks_4-6]]
- [[AI Fundamentals]]
- [[Generative AI - Map of Content]]

*The code companion to [[Prompt Engineering]] (the "ask") and [[AI Engineering]] (the "ship").*
