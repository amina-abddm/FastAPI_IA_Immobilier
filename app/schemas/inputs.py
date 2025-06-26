# Pour executer les codes passer par le terminal avec la commande : python -m app.schemas.inputs
from pydantic import BaseModel
from typing import Literal

class InputData (BaseModel):
    surface_bati : float
    nombre_pieces : int
    surface_terrain: float
    nombre_lots: int
    

 