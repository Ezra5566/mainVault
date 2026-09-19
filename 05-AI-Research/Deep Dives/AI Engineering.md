---
tags: [ai-engineering, mlops, llm, rag, references]
aliases: [ML Engineering, MLOps Deep Dive]
updated: 2026
status: reference
---

# AI Engineering

> [!abstract] What this note is
> A working reference for what an **AI engineer** actually builds, how AI systems are designed end‑to‑end, and the lifecycle that takes a model from notebook to production. Written for a student building real skills and a professional keeping a mental model of the full stack.
>
> The three companion deep dives: [[Prompt Engineering]] (the *ask*), [[Python for AI]] (the *code*), and this note (the *ship*). Hub: [[Generative AI - Map of Content]].

---

## 1. What is AI Engineering?

**Machine learning** is the science of building models that learn from data. **AI engineering** is the craft of turning that science into reliable, maintainable *systems* that run in the world: they ingest live data, serve predictions at low latency, recover from failure, and keep getting better as they age.

The two are different jobs and different mindsets:

| Researcher / ML Scientist | AI / ML Engineer |
|---|---|
| Asks "what is the best model?" | Asks "how does this ship and stay up?" |
| Optimize for accuracy on a benchmark | Optimize for cost, latency, reliability |
| Works in notebooks, isolated | Works in pipelines, infrastructure, teams |
| Success = a new SOTA number | Success = the system is up and cheap |

**AI engineering** sits between data science and software engineering. It covers four overlapping concerns:

1. **Data engineering** — getting clean, versioned, representative data to the model.
2. **Model engineering** — training, choosing, or calling a model (traditional ML *or* an LLM API).
3. **System engineering / MLOps** — the infrastructure that trains, serves, monitors, and deploys models.
4. **Product engineering** — the UX, API surface, and evaluation that make the capability useful to a real user.

> A useful litmus test: an *ML scientist* improves the model; an *AI engineer* makes the model usable, affordable, and dependable. In a small team one person does all four; in a large org they split.

---

## 2. The Full AI/ML Lifecycle

```
        ┌──────────────────────────────────────────────────────────┐
        │ 1. Problem framing & data strategy                       │
        │ 2. Data collection, cleaning, feature engineering       │
        │ 3. Baseline + model selection                            │
        │ 4. Training & validation                                 │
        │ 5. Evaluation & error analysis                           │
        │ 6. Deployment / serving                                  │
        │ 7. Monitoring & drift detection                          │
        │ 8. Retrain / update loop                                 │
        └────────────  feedback from 7 & 8 feeds 1 & 2  ───────────┘
```

The loop is the point. Most production failures are not "the model is wrong"; they are "nobody noticed the data distribution changed." Steps 6–8 are where AI engineering earns its name.

### 2.1 Problem framing
Before touching data, define:
- The **decision** the system enables (not "predict X" but "decide Y using X").
- The **cost of error** — a false positive vs a false negative can be wildly asymmetric (spam filter vs fraud detector vs medical triage).
- The **data you can legally and practically get.** The dataset, not the algorithm, usually caps the ceiling.
- A **baseline** — a dumb rule or heuristic you must beat. If you can't beat "pick the most common class," your model adds no value.

### 2.2 Data & feature engineering
- **Data quality** beats model cleverness. A robust, ugly model on clean data outperforms a clever model on dirty data.
- **Feature engineering** (classical ML): derive inputs the model needs (ratios, lags, one‑hots, embeddings). In the LLM era, "features" often become *prompts and retrieval context* instead of hand‑built columns.
- **Versioning & reproducibility**: log the exact dataset + code + config + seed for every run. Tools: DVC, LakeFS, Delta Lake, MLflow; a plain git + snapshot also works.

### 2.3 Model selection
- Classical: linear models, trees/forests, gradient boosting, SVM, k‑NN, neural nets.
- LLM‑based: use an API model, an open‑weight model you fine‑tune, or a small task‑specific model.
- **Decision rule:** start with the simplest thing that works (gradient boosting or a good baseline LLM). Escalate to the more complex option only when it measurably helps.

---

## 2.5 A Worked End‑to‑End Example (a RAG QA assistant)

The most common LLM system. Trace it once, top to bottom, and the whole field clicks.

```python
import hashlib, json
from openai import OpenAI
from transformers import pipeline

client = OpenAI()
embedder = pipeline("feature-extraction", model="sentence-transformers/all-MiniLM-L6-v2")

def embed(text: str) -> list[float]:
    return embedder(text, normalize_embeddings=True)[0].data.tolist()

# --- 1. INDEX (offline): chunk the docs, embed, store ---
def build_index(docs: list[dict]) -> dict:
    chunks = []
    for d in docs:
        for i in range(0, len(d["text"]), 400):
            c = d["text"][i:i+400]
            chunks.append({
                "source": d["source"],
                "text": c,
                "vec": embed(c),
                "id": hashlib.md5(c.encode()).hexdigest()[:8],
            })
    return chunks  # in production: write to FAISS / pgvector / Chroma

# --- 2. RETRIEVE: top-k by cosine similarity ---
def cosine(a, b) -> float:
    return sum(x*y for x, y in zip(a, b))

def retrieve(query: str, chunks: list[dict], k: int = 5) -> list[dict]:
    qv = embed(query)
    return sorted(chunks, key=lambda c: cosine(qv, c["vec"]), reverse=True)[:k]

# --- 3. GENERATE: prompt the LLM with the context, demand JSON ---
def answer(query: str, chunks: list[dict]) -> dict:
    ctx = retrieve(query, chunks)
    context_block = "\n".join(f"- [{c['source']}] {c['text'][:200]}" for c in ctx)
    prompt = (
        "Answer using ONLY the context below. If the answer is not in the "
        "context, reply with {\"answer\": null}. Return JSON: "
        f'{{"answer": str, "citations": [source names].}}\n'
        f"Context:\n{context_block}\nQuestion: {query}"
    )
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.0,
        response_format={"type": "json_object"},
        messages=[{"role": "system", "content": "You are a careful support bot."},
                  {"role": "user", "content": prompt}],
    )
    return json.loads(resp.choices[0].message.content)

result = answer("When do registrations close?", chunks)
print(result)   # {"answer": "...", "citations": ["regs.pdf"]}
```

> [!tip] Notice every AI‑engineering concept from §1–§3 in 40 lines
> Chunking + embeddings = **retrieval** (the "give it your knowledge" trick). The JSON response format + `if null` instruction = **structured output + a guardrail against hallucination**. `temperature=0.0` = **determinism**. Swapping the model string is the **model router**. Add a cache key on `query` and you've added the **cost lever**. That's the whole LLM-app in one file.

> [!question] Why demand JSON and "reply null if not in context"?
> Because otherwise the model **confabulates** — it answers from its own memory and invents a registration date. Forcing "only use this, else null" is the single highest-leverage prompt constraint for RAG. See [[Prompt Engineering]] §3.9.

---

## 3. MLOps — the engineering layer

**MLOps** = DevOps applied to machine‑learning systems. The recurring problems it solves:

### 3.1 Reproducibility
- Lock: code (git SHA), data (version + row count / hash), dependencies (lockfile), random seeds, and hardware/library versions.
- A run must be re‑creatable. If it isn't, it isn't a result, it's an anecdote.

### 3.2 Model serving
Two main patterns:

| Pattern | How | Best for |
|---|---|---|
| **Realtime** | A model endpoint (REST/gRPC) scores one request in milliseconds | Fraud checks, personalization, recommendation ranking |
| **Batch** | A scheduled job scores thousands of records offline, writes to a store | Churn models, nightly lead scoring, large LLM annotation jobs |

Serving infrastructure:
- **REST/gRPC endpoints** behind an API gateway (FastAPI is the common Python choice).
- **Model containers** (ONNX, TorchServe, Triton, or a Docker image around inference code).
- **Caching** of repeated / expensive calls — big for LLM cost control.
- **Autoscaling** tied to request load; a small GPU pool + request queue is far cheaper than always‑on capacity.

### 3.3 Monitoring (the part everyone skips until it hurts)
- **Data drift** — input distribution moving away from training (concept drift, population shift).
- **Model drift** — prediction distribution or quality degrading even on stable data.
- **System health** — latency percentiles (p50/p95/p99), error rates, token/cost burn, GPU utilization.
- **Guardrails for LLM apps** — rate of refusals, hallucination‑flagged answers, prompt‑injection attempts, PII leakage into logs.

Tooling: Evident, MLflow, Weights & Biases, Prometheus + Grafana for system metrics; a human review queue for high‑stakes outputs.

**Drift, in code** (compare live input stats to the training distribution):

```python
import numpy as np
def drift_report(train: np.ndarray, live: np.ndarray, eps: float = 1e-9) -> dict:
    return {
        "mean_shift": abs(live.mean() - train.mean()),          # > eps? suspect drift
        "std_ratio":  live.std() / (train.std() + eps),        # spread changing?
        "n_live":     len(live),
    }
# in a scheduled job: alert when mean_shift > 0.2 * train.std()
```

The human rule: when a metric decays **gradually**, it's almost always drift, not a model bug. Check the data *first*.

### 3.4 CI/CD for ML
- **Model CI**: every code change re‑runs a regression suite of metrics + golden datasets; no deploy if it degrades.
- **Continuous training (CT)**: a trigger (new data, scheduled, or metric drop) kicks off retraining, which must pass the same gates before it's promoted.
- **A/B / shadow traffic** in production: run the new model in *shadow* (score, don't act) or in a small live bucket before full rollout.

---

## 4. LLM Engineering (the modern branch of AI engineering)

Since 2023, "AI engineer" frequently means *LLM application engineer*. The stack looks different from classical MLOps:

```
User ──> App layer (prompt, tool calls, guardrails)
            │
            ▼
   Retrieval / RAG (vector store, re‑rank, citations)
            │
            ▼
   LLM (API or self‑hosted, sized to the job)
            │
            ▼
   Structured output / validation ──> Action (write, code, call tool)
```

Core building blocks (each has its own deep dive — see [[Prompt Engineering]] and [[AI Fundamentals]]):
- **Prompt engineering** — control of what the model is told to do. See [[Prompt Engineering]].
- **RAG (retrieval‑augmented generation)** — give the model your private, current knowledge so it can answer with citations instead of guessing.
- **Tool / function calling** — let the model call your code, search, and APIs; the model plans, your tools act.
- **Agents** — multi‑step loops where the model decides which tool to call, observes the result, and continues.
- **Fine‑tuning vs. prompting** — prompting + RAG + tools covers most cases; fine‑tune only when you need a *behavior/style* change at low latency and you have high‑quality examples.

**Cost/latency/quality are the LLM engineer's three dials.** You change one by moving the model size, by caching, by reducing tokens, or by batching — and you always trade off against the others.

> [!info] Which block do you actually build? (default to the *least* that works)
> | Need | Start with | Escalate to |
> |---|---|---|
> | Answer from *your* docs | **RAG** (prompt + retrieve) | RAG + reranker, then fine‑tune the retriever |
> | Use *my* data/tools/APIs | **Tool calling** | multi‑step **agent** |
> | Change *style/behavior* cheaply | **Prompting** (few‑shot) | **Fine‑tune** (LoRA) |
> | Many identical, cheap calls | **Small model + cache** | route hard cases to a big model |
>
> The default answer to "which LLM do I use?" is: **prompt + RAG + tools first.** Fine‑tuning is a *last* resort — it's the most expensive block to run and maintain, and the least portable.

**Tool calling, in 15 lines** (the model plans, your code acts):

```python
TOOLS = [{
  "type": "function",
  "function": {
    "name": "get_order_status",
    "description": "Look up a customer's order by order_id",
    "parameters": {
      "type": "object",
      "properties": {"order_id": {"type": "string"}},
      "required": ["order_id"],
    },
  },
}]

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    tools=TOOLS,
    messages=[{"role": "user", "content": "What's going on with order #A100?"}],
)
msg = resp.choices[0].message
if msg.tool_calls:                       # model wants to act, not just chat
    tc = msg.tool_calls[0]
    args = json.loads(tc.function.arguments)     # {"order_id": "A100"}
    result = get_order_status(**args)           # YOU run the real function
    # feed `result` back into a second call so the model can narrate it
```

The discipline: **only expose the tools you actually want called**, and validate the model's arguments before acting — the model is untrusted input to your tools.

---

## 5. Evaluation — how you know it works

Never deploy on vibes. Build an **evaluation harness** before shipping:

- **Classical ML**: hold‑out metrics — accuracy/precision/recall/F1 for classification, RMSE/MAE for regression, AUC‑ROC, lift over a baseline.
- **LLM apps**: a mix of
  - **Unit tests on prompts** (golden input → expected property, not exact string),
  - **Reference‑based metrics** (ROUGE, BLEU, BERTScore) where a gold answer exists,
  - **LLM‑as‑judge** for open‑ended quality (calibrate the judge against human ratings first),
  - **Human review** for the highest‑stakes outputs.
- **Error analysis** is the skill: read the 20–50 worst outputs, cluster *why* they failed, and fix the biggest category first. It beats sweeping metric improvements.

**Regression testing** matters: keep a frozen eval set so you can prove a prompt or model change didn't silently break old behavior.

---

## 6. System design interview lens (for the professional)

When asked to "design an AI system," structure the answer in layers and be explicit about trade‑offs:

1. **Data** — source, size, labeling, refresh cadence, privacy/consent.
2. **Model** — offline‑trained vs. API; batch vs. realtime; what's the acceptable latency?
3. **Serving** — API gateway, auth, rate limits, caching, autoscaling, cost model.
4. **Feedback loop** — how do labels/outcomes flow back? Who approves changes?
5. **Failure modes** — what happens on timeout, on bad data, on a poisoned prompt? Design the guardrails.
6. **Metrics** — business metric *and* model metric *and* system SLOs.

Name the constraints up front (latency budget, $/1k requests, accuracy floor, uptime SLO). A good answer spends half its time on the *failure and monitoring* story — that's what separates an engineer from a notebook.

---

## 7. The AI Engineer Skill Stack (at a glance)

- **Languages**: Python (see [[Python for AI]]); SQL for data; basic TypeScript/JS for front‑ends; some Bash.
- **Data**: NumPy/Pandas, SQL, Parquet/Delta, data versioning.
- **ML**: scikit‑learn, PyTorch or TensorFlow, Hugging Face.
- **LLM apps**: prompt engineering, RAG, vector stores (FAISS/pgvector), LangChain/LlamaIndex or bare APIs.
- **Infra**: Docker, an API gateway (FastAPI), a cloud (AWS/GCP), CI/CD, observability (Prometheus/Grafana/W&B/MLflow).
- **Soft skills**: error‑driven debugging, cost awareness, communicating uncertainty, writing evals before claims.

See [[AI Engineer Roadmap]] for the time‑boxed, milestone‑based version of this.

---

## 8. Common Failure Modes (a professional's checklist)

- **Leakage** — training data peeking into evaluation (temporal leaks, duplicated rows, target‑encoded features). Your metric lies.
- **Data drift** — the world changed; the model didn't. Symptom: steady silent decay in precision/recall.
- **Metric misalignment** — optimizing the number instead of the decision (accuracy on a 99%‑majority class is worthless).
- **Over‑fitting the benchmark** — a model tuned to pass *your* eval but brittle out of distribution.
- **Un‑monitored LLM** — a prompt or model update silently changes behavior; no regression suite catches it.
- **Cost shock** — unbounded LLM usage, no caching, no truncation; a viral moment bills you into the thousands.
- **Security** — prompt injection, secret leakage into logs, no auth on a public model endpoint.

---

## 8b. Self‑Test (active recall)

> [!question] A fraud model's precision has quietly dropped from 90% to 61% over 3 months. No code changed. What did you do first, and why?
> Checked the **data** for drift, not the model. Gradual decay + unchanged code = the world moved (new fraud patterns, new users). Recompute input stats vs training; retrain on fresh data. (See §3.3 "gradual decay = drift, check data first.")

> [!question] Your LLM app is 10× over budget. Name four levers, cheapest first.
> (1) **Cache** repeated/near‑repeated calls; (2) **truncate** context to the minimum tokens; (3) **route** easy calls to a smaller model; (4) **batch** where latency allows. Each trades off against quality or latency — see §8.

> [!question] Why do you run a new model in *shadow traffic* before full rollout?
> It scores requests **without acting** on them — you can compare its output against the live model on real traffic and catch degradation *before* users feel it. It's the cheap‑to‑fail rollout step.

> [!question] One‑line difference between an ML *scientist* and an AI *engineer*?
> The scientist improves the **model**; the engineer makes it **usable, affordable, and dependable** (the MLOps layer: serving, monitoring, cost, reliability).

---

## Related Notes
- [[Prompt Engineering]]
- [[Python for AI]]
- [[AI Fundamentals]]
- [[AI Engineer Roadmap]]
- [[Generative AI - Map of Content]]

*Created as a detailed reference; expand the linked deep dives for prompt and Python specifics.*
