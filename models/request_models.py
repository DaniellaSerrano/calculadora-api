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

class RestaRequest(BaseModel):
    """
    Modelo de datos para la operación de resta. 
    
    Attributes:
        a (float): Primer número.
        b (float): Segundo número.
    """
    a: float
    b: float
    
class MultiplicacionRequest(BaseModel):
    """
    Modelo de datos para la operación de multiplicación. 
    
    Attributes:
        a (float): Primer número.
        b (float): Segundo número.
    """
    a: float
    b: float
    
class DivisionRequest(BaseModel):
    """
    Modelo de datos para la operación de división. 
    
    Attributes:
        a (float): Primer número.
        b (float): Segundo número.
    """
    
    a: float
    b: float
    
class PotenciaRequest(BaseModel):
    """
    Modelo de datos para la operación de potencia. 
    
    Attributes:
        a (float): Primer número.
        b (float): Segundo número.
    """
    a: float
    b: float
    
class RaizRequest(BaseModel):    
    """
    Modelo de datos para la operación de potencia. 
    
    Attributes:
        a (float): El numero que queremos sacar raíz.    
    """
    
    a: float