from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from fastapi.background import BackgroundTasks
from pydantic import BaseModel
from typing import List, Dict
from pathlib import Path
import os
import requests
from backends.tts.generate_audio import azure_tts

# Azure & Gemini keys
os.environ["AZURE_REGION"] = "centralindia"
os.environ["AZURE_KEY"] = "EMZ41PCfxu9WwsX3d7KgS7Wouen1gFv9hvPqr6wyTXawoVMNA8cEJQQJ99BHACGhslBXJ3w3AAAYACOGlhbB"
os.environ['GEMINI_API_KEY'] = "AIzaSyCYjerPTOhkooTo920mDV5P2MZEp8xkVrk"

router = APIRouter(prefix="/v1/audio", tags=["TTS"])

class AudioRequest(BaseModel):
    text: Dict  

def generate_script_from_llm(text: dict) -> List[Dict]:
    try:
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise Exception("GEMINI_API_KEY not set")

        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
        headers = {"Content-Type": "application/json", "X-goog-api-key": api_key}
        prompt = f"Generate an engaging, natural-sounding audio script for a overview start with no introduction nothing like this is the output or something just pour knowledge from the first word and engagement. The script must be based *exclusively* on the following JSON insights data just change the wordings it should not sound as tts of the given text. Do not introduce any external information or generic knowledge. The script should summarize the key points, highlight any contradictions or counterpoints, and connect concepts as outlined in the data. Structure the script for easy listening and to maintain user engagement. The tone should be informative and professional, not conversational, dramatic, or humorous. Focus on presenting the insights and connections clearly and concisely. Here is the JSON data: {text}"

        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        for attempt in range(2):  # Try twice
            try:
                print(f"[LLM] Sending request to Gemini (attempt {attempt + 1})...")
                resp = requests.post(url, headers=headers, json=payload, timeout=25)
                resp.raise_for_status()
                generated_text = resp.json()["candidates"][0]["content"]["parts"][0]["text"]
                return [{"speaker": "sp1", "text": generated_text}]
            except Exception as e:
                print(f"[LLM] Attempt {attempt + 1} failed: {e}")
                if attempt == 1:
                    return [{"speaker": "sp1", "text": "Error generating script."}]
    except Exception as e:
        print(f"[LLM] Error generating script: {e}")
        return [{"speaker": "sp1", "text": "Error generating script."}]

def delete_file(path: Path):
    try:
        if path.exists():
            path.unlink()
            print(f"[Cleanup] Deleted temporary file: {path}")
    except Exception as e:
        print(f"[Cleanup] Failed to delete file {path}: {e}")

@router.post("/")
def create_audio(req: AudioRequest):
    # print("[API] Received request:", req.text)
    script_turns = generate_script_from_llm(req.text)
    full_text = " ".join([t["text"] for t in script_turns])
    # print("[API] Full text to synthesize:", repr(full_text))

    try:
        media_dir = Path("storage/media")
        media_dir.mkdir(parents=True, exist_ok=True)
        temp_file = media_dir / "output.mp3"
        background_tasks = BackgroundTasks()
        background_tasks.add_task(delete_file, temp_file)
        print("[API] Calling Azure TTS...")
        azure_tts("en-US-DavisNeural", full_text, os.environ["AZURE_REGION"], os.environ["AZURE_KEY"], temp_file)
        print("[API] Audio file created at:", temp_file)
    except Exception as e:
        print(f"[API] TTS failed: {e}")
        raise HTTPException(status_code=500, detail=f"TTS failed: {e}")

    print("[API] Returning FileResponse with cleanup...")
    return FileResponse(
        path=temp_file,
        media_type="audio/mpeg",
        filename="output.mp3",
        background=background_tasks
    )

