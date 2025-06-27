# Pour exécuter les codes : python -m app.routes.predict

from fastapi import APIRouter, HTTPException
from ..models.loader import load_model
from ..schemas.inputs import PredictionInput

router = APIRouter()

# ✅ Charge les modèles au lancement
models = load_model()

# ✅ Fonction pour obtenir le nom du modèle utilisé
def model_name(model):
    return type(model).__name__

@router.post("/")
def predict(data: PredictionInput):
    
    # ✅ Encodage du type_local et sélection du modèle
    if data.type_local == "Appartement":
        model = models["appart"]
        type_local_enc = 0
    elif data.type_local == "Maison":
        model = models["maison"]
        type_local_enc = 1
    else:
        raise HTTPException(
            status_code=400,
            detail="Type de bien non reconnu. Utilisez 'Appartement' ou 'Maison'."
        )

    # ✅ Construction du vecteur de caractéristiques
    features = [[
        data.surface_bati,
        data.nombre_pieces,
        type_local_enc,
        data.surface_terrain,
        data.nombre_lots,
    ]]

    # ✅ Prédiction de prix 
    try:
        prediction = model.predict(features)
        return {
            "prix_m2 estimé": prediction[0],
            "modèle utilisé": model_name(model)
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erreur lors de la prédiction : {e}"
        )
