# Pour executer les codes passer par le terminal avec la commande : python -m app.routes.predict

from fastapi import APIRouter, HTTPException
from ..schemas.inputs import InputData
from ..models.loader import get_models
import pandas as pd

router = APIRouter()
models = get_models()  # charge les modèles au lancement

def preprocess_input(data: InputData) -> pd.DataFrame:
    # Convertir l'objet Pydantic en DataFrame pour le modèle
    df = pd.DataFrame([data.dict()])
    # Optionnel : encode type_local
    df['type_local'] = df['type_local'].map({'Appartement': 0, 'Maison': 1})
    return df

@router.post("/predict/lille")
def predict_lille(data: InputData):
    model = models.get("appart") if data.type_local == "Appartement" else models.get("maison")
    if not model:
        raise HTTPException(status_code=400, detail="Type de bien non reconnu.")
    
    X = preprocess_input(data)
    prediction = model.predict(X)[0]
    return {"ville": "Lille", "prediction_prix_m2": round(prediction, 2)}


@router.post("/predict/bordeaux")
def predict_bordeaux(data: InputData):
    model = models.get("appart") if data.type_local == "Appartement" else models.get("maison")
    if not model:
        raise HTTPException(status_code=400, detail="Type de bien non reconnu.")
    
    X = preprocess_input(data)
    prediction = model.predict(X)[0]
    return {"ville": "Bordeaux", "prediction_prix_m2": round(prediction, 2)}
