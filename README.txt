
Solvei8 Booking Analytics & LLM-QA System
===========================================
Project Objective
-------------------
Build a system that processes hotel booking data to provide:
- Analytical insights (revenue, cancellations, lead time, geography)
- Natural language question answering (QA) using Retrieval-Augmented Generation (RAG) and LLMs

This project was submitted for the Solvei8 AI/ML Internship Assignment on 13/04/2025.

Project Structure
--------------------
solvei8-booking-analytics/
├── api/             # FastAPI app with /analytics and /ask endpoints
├── rag/             # Embedding, retrieval, LLM-based QA
├── data/            # Dataset, embeddings, analytics summary
├── notebooks/       # Jupyter notebooks for exploration and testing
├── tests/           # Evaluation scripts and test cases
├── requirements.txt
└── README.txt

Technologies Used
---------------------
- Python 3.11
- FastAPI – API development
- Pandas – data processing
- Matplotlib/Seaborn – analytics visualization
- FAISS – similarity search
- SentenceTransformers – embeddings
- Falcon-RW-1B (HuggingFace) – local LLM for QA
- Jupyter Notebooks – data exploration

How to Run the Project
--------------------------
1. Clone the repository:
    git clone https://github.com/yourusername/solvei8-booking-analytics.git
    cd solvei8-booking-analytics

2. Create and activate a virtual environment:
    python -m venv .venv
    .\.venv\Scripts\activate

3. Install dependencies:
    pip install -r requirements.txt

4. Run the FastAPI server:
    uvicorn api.main:app --reload

5. Open API Docs:
    http://127.0.0.1:8000/docs

Example Query
----------------
POST /ask
{
  "question": "What is the average ADR of bookings in Portugal?"
}

Response:
{
  "answer": "The average price of a hotel booking in Portugal is around 120 depending on hotel type."
}

Analytics Available
-----------------------
- Monthly revenue trends
- Cancellation rate
- Country-wise booking distribution
- Booking lead time histogram
- Average nights per hotel type

Performance Evaluation
--------------------------
| Endpoint     | Avg Response Time |
|--------------|-------------------|
| /analytics   | ~0.2 seconds      |
| /ask         | ~5–7 seconds (CPU with Falcon-RW-1B) |

License
----------
This project is for the Solvei8 AI/ML Internship Assignment. For educational and demonstration purposes only.

Acknowledgements
-------------------
- Solvei8 (https://solvei8.com/)
- HuggingFace – Falcon-RW-1B model
- Kaggle Dataset – Hotel Booking Demand
