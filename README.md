# DocuMind-AI

Welcome to DocuMind-AI, a project born from a hackathon to revolutionize how you interact with your personal document library. Forget about losing your place or struggling to connect ideas across different files. Our system lets you pick up exactly where you left off, providing a seamless and intelligent reading experience. This repository is your direct access point, serving as a reliable fallback if you're not using the Docker image.

Key Features
DocuMind-AI is built on an innovative pipeline designed to be both powerful and efficient, ensuring you get the most out of your documents without unnecessary delays or costs.

Your Personal Library, Enhanced: The central hub of our application is a user-friendly dashboard that displays your entire PDF collection. The system remembers your reading progress, so you can always resume working on any document exactly where you left it. When you add new PDFs or remove old ones, the model automatically retrains itself, ensuring your insights are always up-to-date.

Offline Relevance Model: To tackle the challenge of large, complex documents, we've implemented a dedicated, offline model. When you select a piece of text, this model instantly scans your entire document library to find the most relevant sections. This is a game-changer because it prevents the large language model (LLM) from being overwhelmed by a massive amount of data, ensuring stability and accuracy. It acts as the perfect pre-filter, providing only the most crucial information to the LLM for insight generation.

Efficient and Grounded Insights: By feeding the LLM only the relevant snippets found by our offline model, we keep API calls to a minimum. This not only makes the process lightning fast—especially after the initial training—but also ensures that every insight is directly grounded in the documents you've uploaded. The same data pipeline is used to generate text for the next feature, further boosting efficiency.

Beyond Text-to-Speech: We don't just convert text to audio. Our system uses an LLM to craft an engaging, natural-sounding script from the generated insights. This transforms a simple summary into a compelling, podcast-like experience, perfect for on-the-go learning or review.

Professional and Intuitive UI/UX: The user interface is designed with a sleek, professional aesthetic. The main view features two dedicated panes: the left pane provides a quick-access outline of your document, while the right pane dynamically displays the relevant sections and insights. Both are controlled by a professional, iOS-level action bar, making navigation fluid and effortless. The frontend also features a hidden scrollbar for a cleaner look, achieved with a simple addition in the index.css file.

Getting Started
Follow these instructions to set up the project locally.

Backend Setup
The backend is built with Python. We highly recommend using a virtual environment to manage dependencies and avoid conflicts.

Create and Activate a Virtual Environment:

python -m venv venv
venv\Scripts\Activate.ps1

Navigate to the backend directory:

cd server

Install the required Python packages:

pip install -r requirements.txt

Run the backend server with uvicorn:
Uvicorn is a high-performance server that's great for running FastAPI applications, which is what the backend uses.

uvicorn main:app --reload --port 8000

Frontend Setup
The frontend is a React application created with Vite. We're using Tailwind CSS for a modern, utility-first styling approach.

Initialize the React app with Vite:
npm create vite@latest

Follow the prompts to choose react as your framework.

Install Tailwind CSS:
Follow the official Tailwind CSS documentation for installation with Vite: https://tailwindcss.com/docs/installation/using-vite.

Navigate to the frontend directory:
cd client

Install the necessary dependencies:

npm install

Run the development server:

npm run dev
