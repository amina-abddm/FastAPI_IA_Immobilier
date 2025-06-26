# Pour executer les codes passer par le terminal avec la commande : python -m app.models.loader

import joblib
import os
from ..schemas.inputs import InputData


MODEL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../models"))
print(f"📁 Chemin des modèles : {MODEL_DIR}")

# Chargement des modèles de régression (entraînés sur Lille)

model_dt_gs_apparts = joblib.load(os.path.join(MODEL_DIR, "decision_tree_gridsearchcv_apparts_Lille.pkl"))
model_dt_gs_maisons = joblib.load(os.path.join(MODEL_DIR, "decision_tree_gridsearchcv_maisons_Lille.pkl"))

# ✅ Vérification manuelle du chargement 
print("📦 Modèles chargés avec succès !")
   
# ✅ Fonction utilitaire pour exposer les modèles
def get_which_models():
    return {
        "appart": (model_dt_gs_apparts ),
        "maison": (model_dt_gs_maisons)
    }

print(f"Modèles utilisés : 🏢 {model_dt_gs_apparts.__class__.__name__} | 🏡 {model_dt_gs_maisons.__class__.__name__}")
