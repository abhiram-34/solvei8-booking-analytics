# Solvei8 Assignment – Report

## Objective

To create an end-to-end solution for hotel booking data analysis and intelligent question answering using LLMs.

---

## Implementation Overview

### 1. **Data Processing**
- Cleaned missing values in fields like `children`, `agent`, `company`.
- Added new columns: `total_nights`, `revenue`.

### 2. **Analytics**
- Monthly revenue trends via `reservation_status_date`
- Cancellation rate visualization
- Top countries by bookings
- Lead time distribution

### 3. **RAG System**
- Used `SentenceTransformer` for embeddings.
- Stored in FAISS index.
- Used Falcon-RW-1B model for natural language answers.
- Retrieved top 5 matching records for every question.

### 4. **API Development**
- FastAPI used to create endpoints:
  - `/analytics`: returns analytics summary from `analytics_summary.json`
  - `/ask`: returns LLM answer based on user query

---

## Challenges Faced

- **Resource constraints**: Falcon-RW-1B was CPU-heavy; optimized with `max_new_tokens=80`.
- **Model size**: Avoided committing large files by using `.gitignore`.
- **Data formatting**: Careful prompt construction was needed for usable LLM answers.

---

## Result

- API works with structured and natural queries.
- Fast response for `/analytics`; ~5-7s for `/ask`.
- RAG with Falcon-RW-1B gives decent context-based answers on CPU.

---

