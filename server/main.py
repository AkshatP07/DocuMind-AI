from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import files, tts, model_relevant, model_a  

app = FastAPI(title="Unified Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(files.router)
app.include_router(tts.router)
app.include_router(model_relevant.router) 
app.include_router(model_a.router) 
