import joblib
import os


MODEL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../models"))
print(f"📁 Chemin des modèles : {MODEL_DIR}")

# Chargement des modèles de régression (entraînés sur Lille)
model_dt_apparts = joblib.load(os.path.join(MODEL_DIR, "decision_tree_apparts_Lille.pkl"))
model_dt_gs_apparts = joblib.load(os.path.join(MODEL_DIR, "decision_tree_gridsearchcv_apparts_Lille.pkl"))
model_dt_maisons = joblib.load(os.path.join(MODEL_DIR, "decision_tree_maisons_Lille.pkl"))
model_dt_gs_maisons = joblib.load(os.path.join(MODEL_DIR, "decision_tree_gridsearchcv_maisons_Lille.pkl"))
model_lr_apparts = joblib.load(os.path.join(MODEL_DIR,"linear_regression_apparts_Lille.pkl"))
model_lr_maisons = joblib.load(os.path.join(MODEL_DIR,"linear_regression_maisons_Lille.pkl"))
model_rf_apparts = joblib.load(os.path.join(MODEL_DIR,"random_forest_apparts_Lille.pkl"))
model_rf_gs_apparts = joblib.load(os.path.join(MODEL_DIR,"random_forest_gridsearchcv_apparts_Lille.pkl"))
model_rf_maisons = joblib.load(os.path.join(MODEL_DIR,"random_forest_maisons_Lille.pkl"))
model_rf_gs_maisons = joblib.load(os.path.join(MODEL_DIR,"random_forest_gridsearchcv_maisons_Lille.pkl"))
model_xgb_apparts = joblib.load(os.path.join(MODEL_DIR,"xgboost_apparts_Lille.pkl"))
model_xgb_maisons = joblib.load(os.path.join(MODEL_DIR,"xgboost_maisons_Lille.pkl"))

    
# (Optionnel) Fonction utilitaire pour exposer les modèles
def get_models():
    return {
        "appart": (model_dt_gs_apparts, model_dt_gs_apparts, 
                   model_lr_apparts,model_rf_apparts,model_rf_gs_apparts,
                   model_xgb_apparts
                   ),
        "maison": (model_dt_maisons, model_dt_gs_maisons, model_lr_maisons,
                   model_rf_maisons, model_rf_gs_maisons,
                   model_xgb_maisons)
    }

# ✅ Vérification manuelle du chargement 
print("📦 Modèles chargés avec succès !")
