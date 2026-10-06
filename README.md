# ⚡ KURIPPU — Turn Documents into Actions

> **AI-Powered Document Intelligence & Action Extraction Workspace**  
> Automatically extract actionable tasks, deadlines, milestones, assignees, and key decisions from PDFs, Word documents, text files, and images.

---

## ✨ Features

- **📄 Document Intelligence**: Upload PDFs, DOCX, TXT, or images (up to 50MB) and parse structured or unstructured content.
- **🤖 Multi-Stage Action Extraction**: Uses OpenAI / Gemini / Heuristic pipelines to detect explicit and implicit tasks, assignees, and deadlines.
- **🎯 Human-in-the-Loop Confirmation**: AI suggests tasks with confidence ratings; users review, edit, and confirm actions before execution.
- **🔍 "Why This Action?" Explainability**: Displays the exact sentence and page context from which an action item was inferred.
- **📊 Visual Kanban & Deadlines**: Organize tasks across To Do, In Progress, and Completed, or filter by smart deadlines.
- **📅 Interactive Action Calendar**: Month view populated with extracted event dates and upcoming deadlines.
- **📈 Real-Time Analytics**: Action completion velocity, priority distribution, and weekly throughput charts.
- **🔔 Reminders & Notifications**: Scheduled reminder engine and in-app alert center.
- **🔎 Unified Workspace Search**: Instant semantic and keyword search across documents, actions, team members, and dates.
- **🎨 Vibrant Multi-Color UI**: Electric neon palettes, glassmorphic cards, and customizable aesthetic wallpaper support.

---

## 🛠️ Tech Stack

### **Backend**
- **Framework**: Python 3.10+ / FastAPI (Async REST APIs)
- **Database**: SQLite (SQLAlchemy ORM + Alembic migrations)
- **AI / LLM Integration**: OpenAI API (`gpt-4o-mini`, `gpt-4o`), Google Gemini API, fallback heuristic extractor
- **Document Processing**: `PyPDF2`, `python-docx`, `pdfplumber`, `Pillow`
- **Authentication**: JWT tokens (Bearer) + bcrypt password hashing

### **Frontend**
- **Framework**: React 18 + Vite + TypeScript
- **Styling**: TailwindCSS + Custom CSS Design System
- **State Management**: Zustand + React Query (TanStack Query)
- **Icons & Animation**: Lucide React + Framer Motion
- **Data Visualization**: Recharts

---

## 🚀 Getting Started

### 1. Prerequisites
- **Python**: 3.10 or higher
- **Node.js**: 18.0 or higher
- **Git**

---

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# On Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY or GEMINI_API_KEY

# Run database migrations and seed data
python -m app.seed_data

# Start FastAPI server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The backend API will run at `http://localhost:8000` (Interactive Swagger docs: `http://localhost:8000/docs`).

---

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start Vite development server
npm run dev
```

The frontend will run at `http://localhost:5173`.

---

## 🔒 Security & Privacy

- All document files and SQLite database entries are user-scoped with strict access controls.
- API keys are stored exclusively in backend environment files (`.env`) and never exposed to client applications.
- Permanent deletion cascades across files, extracted chunks, actions, and audit logs.

---

## 📄 License

This project is licensed under the MIT License.
