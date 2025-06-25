# Pour exécuter le main : ouvrir terminal puis python -m app.main  

from .models.loader import get_models

models = get_models()
appart_model = models["appart"]
maison_model = models["maison"]

# ✅ Vérification manuelle
print("📦 Modèles chargés avec succès !")
print(f"🧠 Appart Model: {type(appart_model)}")
print(f"🧠 Maison Model: {type(maison_model)}")


from fastapi import FastAPI
from app.routes import predict

app = FastAPI()

app.include_router(predict.router)
