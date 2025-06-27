# Pour executer les codes passer par le terminal avec la commande : python -m app.schemas.inputs
from pydantic import BaseModel

class PredictionInput (BaseModel):
    surface_bati : float
    nombre_pieces : int
    type_local : str # sert a définir le modele qui sera utilisé
    surface_terrain: float
    nombre_lots: int