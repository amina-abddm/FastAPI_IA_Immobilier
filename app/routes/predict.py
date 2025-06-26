# Pour executer les codes passer par le terminal avec la commande : python -m app.routes.predict

from fastapi import APIRouter, HTTPException
from ..models.loader import get_which_models
from ..schemas.inputs import InputData
import pandas as pd

router = APIRouter()
models = get_which_models()  # charge les modèles au lancement

# ✅ Fonction qui convertir la classe InputData en df pour son utilisation dans le modéle de prédiction
def prepare_data(data: InputData):
    return pd.DataFrame([data.dict()])

# ✅ Fonction qui permet d'identifier le nom du modele utiliser dans la réponse API
def get_model_name(model):
    return type(model).__name__


@router.post("/predict/lille")
def predict(data: InputData):
    
    model = models["appart"] if data.type_local == "Appartement" else models["maison"]
    df = prepare_data(data)
    
    try:
         # Effectuer la prédiction à partir du DataFrame préparé
        prediction = model.predict(df)[0]
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f" Erreur lors de la prédiction : {e}")

    return {
        "prix_m2_estime": round(prediction, 2),
        "model": get_model_name(model)
    }



@router.post("/predict/bordeaux")
def predict(data: InputData):
    
    model = models["appart"] if data.type_local == "Appartement" else models["maison"]
    df = prepare_data(data)
    
    try:
         # Effectuer la prédiction à partir du DataFrame préparé
        prediction = model.predict(df)[0]
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f" Erreur lors de la prédiction : {e}")

    return {
        "prix_m2_estime": round(prediction, 2),
        "model": get_model_name(model)
    }
