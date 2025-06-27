# Pour exécuter les codes passer par le terminal avec la commande : python -m app.routes.predict

from fastapi import APIRouter, HTTPException
from ..models.loader import load_model
from ..schemas.inputs import PredictionInput
from sklearn.preprocessing import LabelEncoder
import logging

router = APIRouter()
models = load_model()  # Charge les modèles au lancement
logger = logging.getLogger(__name__)


# ✅ Fonction pour obtenir le nom du modèle utilisé
def model_name(model):
    return type(model).__name__


# ✅ Encodage du type de bien
def encode_type_local(type_local: str) -> int:
    encoder = LabelEncoder()
    encoder.classes_ = ['Appartement', 'Maison']
    return encoder.transform([type_local])[0]


# ✅ Mapping dynamique des modèles
model_mapping = {
    "Appartement": "appart",
    "Maison": "maison"
}


@router.post("/")
def predict(data: PredictionInput):
    # 📌 Log des données d'entrée
    logger.info(f"Requête de prédiction reçue: {data.dict()}")

    # 📌 Récupération dynamique du modèle
    model_key = model_mapping.get(data.type_local)
    if not model_key:
        raise HTTPException(status_code=400, detail="Type de bien non reconnu. Utilisez 'Appartement' ou 'Maison'.")

    model = models[model_key]

    # 📌 Encodage
    type_local_enc = encode_type_local(data.type_local)

    # 📌 Construction du vecteur de caractéristiques
    features = [[
        data.surface_bati,
        data.nombre_pieces,
        data.surface_terrain,
        data.nombre_lots,
        type_local_enc
    ]]

    try:
        prediction = model.predict(features)
        return {
            "prix_m2 estimé": prediction[0],
            "modèle utilisé pour la prédiction": model_name(model)
        }

    except Exception as e:
        logger.error(f"Erreur lors de la prédiction : {e}")
        raise HTTPException(status_code=500, detail=f"Erreur lors de la prédiction : {e}")
