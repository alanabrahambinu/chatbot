# ⚖️ Legal AI Assistant

### AI-Powered Legal Research, Document Analysis & Question Answering

A web-based Legal AI Assistant designed to help users explore legal documents, ask legal questions, and retrieve relevant information through an interactive chatbot interface.

The application combines a **FastAPI backend**, a responsive web frontend, and document-based retrieval techniques to support legal research and educational use.

## ✨ Features

- **AI-Powered Legal Question Answering** — Ask questions about legal concepts, constitutional provisions, and uploaded reference documents.
- **Document-Based Research** — Uses legal reference materials stored in the backend's `data/` directory.
- **PDF Document Support** — Process legal PDFs for document-based question answering.
- **Source References** — Designed to provide supporting document references for retrieved information.
- **Conversation History** — Access previous conversations through the chat interface.
- **Document Library** — View available reference documents.
- **Optional Document Upload** — Add documents through the interface where supported.
- **Responsive User Interface** — Professional legal-themed chatbot design.
- **Local Development** — Run the application on your computer for development and testing.

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Backend | Python, FastAPI |
| Frontend | HTML, CSS, JavaScript |
| API Server | Uvicorn |
| Document Processing | PDF parsing and text processing |
| AI Integration | Document retrieval and language-model-based answering |
| Database | SQLite |
| Testing | Pytest |
| Version Control | Git and GitHub |

## 📁 Project Structure

```text
legal-chatbot/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── data/
│   │   └── constitution.pdf
│   └── tests/
│       └── test_app.py
├── frontend/
│   └── index.html
├── .gitignore
└── README.md
```

Virtual environments, local databases, caches, and other generated files are excluded from Git using `.gitignore`.

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/alanabrahambinu/chatbot.git
cd chatbot/backend
```

### 2. Create a Python virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
```

### 3. Install dependencies

```powershell
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 4. Add legal reference documents

Place the legal PDF documents you want the application to use inside:

```text
backend/data/
```

The repository includes `constitution.pdf` as an initial reference document.

### 5. Start the backend

From the `backend` directory:

```powershell
.\venv\Scripts\python.exe -m uvicorn app:app --reload --port 8000
```

The API runs at:

```text
http://127.0.0.1:8000
```

### 6. Open the application

Visit:

```text
http://127.0.0.1:8000/app
```

Alternatively, open `frontend/index.html` through a local development server if the frontend is configured to communicate with the backend.

## 💬 Example Questions

Try asking the chatbot:

1. What is Article 21 of the Indian Constitution?
2. Explain the Fundamental Rights guaranteed by the Indian Constitution.
3. What is the difference between Article 14 and Article 15?
4. Explain the constitutional right to education.
5. What does Article 32 of the Indian Constitution provide?

The quality and coverage of responses depend on the available reference documents and the configured AI components.

## 🧪 Testing

Run backend tests from the `backend` directory:

```powershell
.\venv\Scripts\python.exe -m pytest tests -v
```

Tests should be reviewed and expanded as new features are introduced.

## 🔮 Future Enhancements

- Support for additional legal document formats
- Improved semantic search and retrieval accuracy
- More detailed document citations
- Multi-document legal research
- Legal document summarization
- Better conversation management
- Authentication and user-specific workspaces
- Cloud deployment
- Expanded legal knowledge sources

## ⚠️ Disclaimer

This project is intended for **educational, research, and development purposes only**.

AI-generated responses may contain inaccuracies or omit relevant legal details. Always verify legal information against authoritative legal sources and consult a qualified legal professional when appropriate.

The current application is intended for local testing and should not be used to store or process confidential legal documents without appropriate security controls.

## 👨‍💻 Developer

**Alan Abraham Binu**

GitHub: [alanabrahambinu](https://github.com/alanabrahambinu)

## 📄 Project Status

**Development / Local Testing**

The application is under active development, with ongoing improvements planned for document retrieval, answer quality, usability, and legal research capabilities.
