# Pour executer les codes passer par le terminal avec la commande : python -m app.routes.predict

from fastapi import APIRouter, HTTPException
from ..schemas.inputs import InputData, PredictRequest
from ..models.loader import get_models
import pandas as pd

router = APIRouter()
models = get_models()  # charge les modèles au lancement


def prepare_data(data):
    return pd.DataFrame([data.dict()])

def get_model_name(model):
    return type(model).__name__

@router.post("/predict/lille")
def predict_lille(data: InputData):
    model = models["appart"] if data.type_local == "Appartement" else models["maison"]
    df = prepare_data(data)
    prediction = model.predict(df)[0]
    return {
        "prix_m2_estime": round(prediction, 2),
        "ville_modele": "Lille",
        "model": get_model_name(model)
    }

@router.post("/predict/bordeaux")
def predict_bordeaux(data: InputData):
    model = models["appart"] if data.type_local == "Appartement" else models["maison"]
    df = prepare_data(data)
    prediction = model.predict(df)[0]
    return {
        "prix_m2_estime": round(prediction, 2),
        "ville_modele": "Lille",  # ✅ on précise que le modèle vient de Lille
        "model": get_model_name(model)
    }
    
    
@router.post("/predict")
def predict_dynamic(request: PredictRequest):
    ville = request.ville.lower()
    data = request.features

    if ville not in ["lille", "bordeaux"]:
        raise HTTPException(status_code=400, detail="Ville inconnue. Choisissez 'lille' ou 'bordeaux'.")

    model = models["appart"] if data.type_local == "Appartement" else models["maison"]
    df = prepare_data(data)

    try:
        prediction = model.predict(df)[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la prédiction : {e}")

    return {
        "prix_m2_estime": round(prediction, 2),
        "ville_modele": "Lille",  # le modèle reste entraîné sur Lille
        "model": get_model_name(model)
    }