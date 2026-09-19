# Generative AI (Weeks 8–9)

**Why this module matters:** 2026 learners expect hands‑on experience with large language models, prompt engineering, and AI‑driven assistants. This module bridges theory to production‑ready projects.

## Core Topics
- **Large Language Models (LLMs)**
  - Architecture overview (Transformer decoder stack)
  - Temperature, top‑k / top‑p sampling
  - Model sizing (parameter counts) and compute budgets

- **Prompt Engineering**
  - Crafting effective prompts
  - Few‑shot vs. zero‑shot examples
  - Chaining prompts (self‑refine, tool‑use)

- **Retrieval‑Augmented Generation (RAG)**
  - Embedding vectors & similarity search
  - Indexing domain‑specific corpora
  - Combining retrieval with generation

- **Embeddings & Vector Stores**
  - How embeddings capture semantic meaning
  - FAISS / Milvus / simple SQLite‑based stores
  - Updating and versioning embeddings

- **Fine‑tuning & Parameter‑Efficient Tuning**
  - Full‑model fine‑tuning vs. LoRA / adapters
  - Dataset preparation (instruction tuning)
  - Evaluation of fine‑tuned models

- **AI Agents**
  - Autonomous planning loops
  - Tool‑use primitives (search, calculator, database query)
  - Multi‑agent collaboration basics

- **Tooling & Deployment**
  - Python API wrappers (e.g., HuggingFace `transformers`, `langchain`, `llama‑index`)
  - API endpoints (FastAPI, Flask) for serving models
  - Simple Docker containers for reproducible serving

## Hands‑On Project: Build a University Assistant Chatbot
1. **Scope**
   - Answer FAQs about courses, deadlines, registration, and campus resources.
   - Use a retrieval pipeline over the university’s public PDFs/wiki.
   - Generate responses with a small open‑source LLM (e.g., Mistral‑7B or Llama‑3‑8B).

2. **Steps**
   - **Data Collection**: Scrape/ingest relevant documents → chunk → embed.
   - **Vector Store**: Index embeddings with FAISS.
   - **Retrieval**: At query time, fetch top‑k chunks and pass to the LLM.
   - **Prompt Design**: Prepend system instructions and few‑shot examples.
   - **Fine‑tuning (optional)**: Train on a curated set of Q&A pairs for the university domain.
   - **API Layer**: Wrap the pipeline in a `/chat` endpoint.
   - **Frontend (optional)**: Simple Streamlit or Gradio UI for interaction.

3. **Evaluation**
   - **Automated**: BLEU / ROUGE against a held‑out answer key.
   - **Human**: Conduct a small user study (accuracy, clarity, satisfaction).
   - **Deployability**: Verify Docker image size, latency, and cost per query.

4. **Deliverables**
   - GitHub repository with notebooks, Dockerfile, and README.
   - Short video/demo (≤3 min) showing a user query and response.
   - Documentation: data sources, embedding index size, inference cost estimate.

> **Tip:** Keep the model size modest (<10 B parameters) to stay within typical university GPU budgets. Use quantization (e.g., 4‑bit) if needed.

---

> **Cluster hub:** see [[Generative AI - Map of Content]] for the full AI/ML map of content and study path.
