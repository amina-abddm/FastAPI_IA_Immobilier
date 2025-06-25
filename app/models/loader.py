import joblib
import os

# Dossier où les modèles sont sauvegardés. Ici nous choisirons le modéle DecisionRegressor avec GridSearchCV
# Modéle qui présente le moin s d'écart entre Lille et Bordeaux. 

MODEL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../models"))
print(f"📁 Chemin des modèles : {MODEL_DIR}")

# Chargement des modèles de régression (entraînés sur Lille)
model_dt_gs_apparts = joblib.load(os.path.join(MODEL_DIR, "decision_tree_gridsearchcv_apparts_Lille.pkl"))
model_dt_gs_maisons = joblib.load(os.path.join(MODEL_DIR, "decision_tree_gridsearchcv_maisons_Lille.pkl"))
    
# (Optionnel) Fonction utilitaire pour exposer les modèles
def get_models():
    return {
        "appart": model_dt_gs_apparts,
        "maison": model_dt_gs_maisons,
    }
