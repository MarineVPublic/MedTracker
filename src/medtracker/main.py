from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Tout va bien, No Panic !!! MedTracker API"}

@app.get("/health")
def health():
    return {"status": "ok"}