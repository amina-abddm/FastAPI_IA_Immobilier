# Pour exécuter le main : ouvrir terminal puis python -m app.main  
# Pour lancer l'application : ouvrir terminal puis uvicorn app.main:app --reload

from fastapi.responses import HTMLResponse
from .models.loader import load_model

models = load_model()
appart_model = models["appart"]
maison_model = models["maison"]

# ✅ Vérification manuelle
print("📦 Modèles chargés avec succès !")


from fastapi import FastAPI
from .routes import predict

app = FastAPI(title="API de Prédiction Immobilière 🏡🏘️",
    description="Estimez le prix au m² pour Lille et Bordeaux avec des modèles pré-entraînés.",
    version="1.0")

# 🌐 Inclusion des routes
app.include_router(predict.router)

# 🏠 Page d'accueil
@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <h1> 🏡 Bienvenue sur l'API de prédiction immobilière </h1>
    <p>Utilisez <a href='/docs'>/docs</a> pour explorer l'API.</p>
    <ul>
            
    """