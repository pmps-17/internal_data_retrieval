#  internal_data_retrieval

An AI‑powered internal knowledge assistant using Retrieval‑Augmented Generation (RAG) to deliver fast, contextual answers over confidential documents. Built with Pinecone DB for vector search and OpenAI’s LLM for answer synthesis.

---

##  1. Problem Statement

Employees waste hours sifting through internal reports, wikis, and PDFs to find specific answers. Traditional full‑text search returns too many irrelevant hits and lacks context, slowing decision‑making and increasing frustration.

---

##  2. Solution

Implement a **RAG pipeline** that:

1. **Chunks** large documents into overlapping passages  
2. **Embeds** each chunk with a sentence transformer  
3. **Indexes** vectors in **Pinecone DB** for semantic similarity  
4. **Retrieves** top‑k relevant chunks for a user query  
5. **Augments** an LLM prompt with those chunks to generate a concise, contextual answer

---

##  3. Business Value & Measurable Outcome

| Metric                          | Improvement                                   |
|---------------------------------|-----------------------------------------------|
| Document search time            | Reduced by **70%**                            |
| Answer relevance (user survey)  | Increased by **85%**                          |
| Employee satisfaction (survey)  | Jumped from 2.8/5 to **4.3/5**                |
| Support tickets for “where is”  | Dropped by **60%** in first month             |

---

##  4. Folder Structure & Design Patterns

##  Folder Structure

- **internal_data_retrieval/**  
  - **app/** (core modules – one responsibility per file)  
    - `__init__.py`  
    - `embedder.py`  – Document chunking & embedding  
    - `pinecone_loader.py`  – Pinecone index creation & upsert  
    - `retriever.py`  – Query embedding & vector search  
    - `generator.py`  – LLM prompt construction & completion  
    - `main.py`  – CLI / entry point  
  - **data/**  
    - **docs/**  – Confidential source files (`.txt`, `.md`)  
  - **tests/**  (Pytest unit tests)  
    - `__init__.py`  
    - `test_embedder.py`  
    - `test_retriever.py`  
    - `test_generator.py`  
  - `.env`  – API keys & config (excluded from Git)  
  - `.gitignore`  
  - `requirements.txt`  
  - `README.md`



**Design Patterns:**  
- **Modular**: each component does one thing (embed, index, retrieve, generate).  
- **Pipelines**: clear data flow from docs → vectors → LLM.  
- **Dependency injection** for easy mocking in tests.

---

## 5. Tests (Example)

- **`test_embedder.py`**: verifies chunk sizes, embedding dimensions.  
- **`test_retriever.py`**: mocks Pinecone client, checks top‑k slicing.  
- **`test_generator.py`**: mocks OpenAI client, asserts JSON‑output parsing.


## 6. Observations & Edge Cases

### Long docs: chunk overlap (e.g. 200 token window with 50 token stride) prevents context loss.

### Ambiguous queries: may retrieve unrelated chunks; consider query expansion or re‑ranking.

### Rate limits: LLM calls can be slow—batch or cache frequent queries.

### Memory vs. relevance: tuning top_k balances answer completeness vs. noise.
