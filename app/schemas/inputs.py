from pydantic import BaseModel
from typing import Literal

class InputData (BaseModel):
    surface_bati : float
    nombre_pieces : int
    type_local: str 
    surface_terrain: float
    nombre_lots: int
    
class Features (BaseModel):
    surface_bati: float
    nombre_pieces: int
    type_local: Literal["Appartement", "Maison"]
    surface_terrain: float
    nombre_lots: int
   
class PredictRequest(BaseModel):
    ville: Literal["lille", "bordeaux"]
    features: Features