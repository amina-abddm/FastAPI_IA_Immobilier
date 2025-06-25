from pydantic import BaseModel

class InputData (BaseModel):
    surface_bati : float
    nombre_pieces : int
    type_local: str  # "Appartement" ou "Maison"
    surface_terrain: float
    nombre_lots: int
   
