from pydantic import BaseModel
from typing import Literal

class InputData (BaseModel):
    surface_bati : float
    nombre_pieces : int
    type_local: str 
    surface_terrain: float
    nombre_lots: int
    

 