# DocuMind-AI

***This repository can also serve as a fallback if you’re not using the Docker image***

Welcome to **DocuMind-AI**, a hackathon-born project designed to revolutionize the way you interact with your personal document library. No more losing your place or struggling to connect ideas across files—pick up exactly where you left off with a seamless, intelligent reading experience.

***imp : the keys need to be hardcoded in certain files for the app to run***
Those files are:
- client/src/components/RightSideBar.jsx (gemini api key)
- client/src/components/AdobePdfViewer.jsx (client id adobe) - 38c90a9c49bd4c5b8e96702b40b5ca75
also can be generated from https://acrobatservices.adobe.com/dc-integration-creation-app-cdn/main.html?api=pdf-embed-api ***keep Application Domain as localhost***
- server/routers/tts.py (azure key&region and gemini api key)

---

## Key Features

### Your Personal Library, Enhanced
- User-friendly dashboard displaying your entire PDF collection.
- Tracks your reading progress for seamless resumption.
- Automatically retrains the model when PDFs are added or removed.

### Offline Relevance Model
- Handles large, complex documents efficiently.
- Instantly scans your document library for the most relevant sections.
- Feeds only the crucial information to the LLM for accurate insights.

### Efficient and Grounded Insights
- Minimizes LLM API calls by sending only relevant snippets.
- Lightning-fast processing after initial training.
- Ensures all insights are grounded directly in your uploaded documents.

### Beyond Text-to-Speech
- Converts insights into natural, podcast-like audio.
- Uses an LLM to craft engaging, human-like scripts from summaries.

### Professional and Intuitive UI/UX
- Two main panes in the interface:
  - **Left Pane:** Quick-access document outline.
  - **Right Pane:** Dynamically displays relevant sections and insights.
- Smooth navigation with a professional action bar.
- Hidden scrollbars for a clean look (`index.css` tweak).

---

## Getting Started

Follow these instructions to set up the project locally.

### Backend Setup
The backend is built with Python and FastAPI. Using a virtual environment is recommended.

1. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\Activate.ps1  # Windows PowerShell
   # OR
   source venv/bin/activate    # macOS/Linux 
2. **Navigate to the backend directory:**
   ```bash
   cd server
2. **Install the required Python packages:**
   ```bash
   pip install -r requirements.txt
2. **Run the backend server with uvicorn:**
Uvicorn is a high-performance server that's great for running FastAPI applications, which is what the backend uses.
   ```bash
   uvicorn main:app --reload --port 8080

### Frontend Setup
The frontend is a React application created with Vite. We're using Tailwind CSS for a modern, utility-first styling approach.

1. **Initialize the React app with Vite (if not already done):**
   Follow the prompts to choose react as your framework.
   ```bash
   npm create vite@latest
3. **Install Tailwind CSS:**
   Follow the official Tailwind CSS documentation for installation with Vite: https://tailwindcss.com/docs/installation/using-vite.
4. **Navigate to the frontend directory:**
   ```bash
   cd client
2. **Install the necessary dependencies:**
   ```bash
   npm install
2. **Run the development server::**
   ```bash
   npm run dev
