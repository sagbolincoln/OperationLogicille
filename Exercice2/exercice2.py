from fastapi import FastAPI

# Initialisation de l'application
app = FastAPI()

# Route de test
@app.get("/")
def read_root():
    return {"message": "Hello FastAPI 🚀"}

# Route avec paramètre
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
