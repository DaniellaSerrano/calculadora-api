"""
Modelos de solicitud para la API de calculadora.
"""
from pydantic import BaseModel


class SumaRequest(BaseModel):
    """
    Modelo de datos para la operación de suma.

    Attributes:
        a (float): Primer número.
        b (float): Segundo número.
    """
    a: float
    b: float

class RestaResquest(BaseModel):
    """
    Modelo de datos para la operación de resta. 
    
    Attributes:
        a (float): Primer número.
        b (float): Segundo número.
    """
    a: float
    b: float
    
    