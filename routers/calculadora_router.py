"""
Este es un comentario de varias líneas,
usuado comunmente para describir las funciones. 
"""

"""
Router de operaciones matemáticas para la API de calculadora.
"""
# Esto es un comentario. 

from fastapi import APIRouter
from models.request_models import SumaRequest, RestaRequest, MultiplicacionRequest, DivisionRequest, PotenciaRequest, RaizRequest
from services.operaciones_service import sumar, restar, multiplicar, dividir, potencia, raiz, factorial

router = APIRouter()

@router.post("/suma")
def ruta_suma(datos: SumaRequest):
    """
    Calcula la suma de dos números.

    Args:
        datos (SumaRequest): Cuerpo de la petición con dos números.

    Returns:
        dict: Resultado de la suma.
    """

    resultado = sumar(datos.a, datos.b)
    return {"resultado": resultado} #Es un diccionario de Python, que FastAPI convierte automaticamnt a JSON.
    # En este caso el diccionario {} con la palabra clave "resultado"

@router.post("/resta")
def ruta_resta(datos: RestaRequest):
    
    """
    Calcula la resta de dos números.

    Args:
        datos (RestaRequest): Cuerpo de la petición con dos números.

    Returns:
        dict: Resultado de la resta.
    """
      
    resultado = restar(datos.a,datos.b)
    return {"resultado": resultado}

@router.post("/multiplicacion")
def ruta_multiplicacion(datos: MultiplicacionRequest):
    
    """
    Calcula la multiplicación de dos números.

    Args:
        datos (MultiplicaciónRequest): Cuerpo de la petición con dos números.

    Returns:
        dict: Resultado de la multiplicación.
    """
    resultado = multiplicar(datos.a,datos.b)
    return {"resultado": resultado}

@router.post("/division")
def ruta_division(datos: DivisionRequest):
    
    """
    Calcula la división de dos números.

    Args:
        datos (DivisiónRequest): Cuerpo de la petición con dos números.

    Returns:
        dict: Resultado de la división.
        
    Raises: 
        HTTPExpetion: Si el divisor es cero. 
    
    """
    
    try:
        resultado = dividir(datos.a,datos.b)
        return {"resultado": resultado}
    
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))     
  
@router.post("/potencia")
def ruta_potencia(datos:PotenciaRequest):
    """
    Potencia de a ^ b.

    Args:
        datos (PotenciaRequest):Base y exponente.

    Returns:
        float: Resultado de la potencia.
    """ 
    resultado = potencia(datos.a,datos.b)
    return{"resultado": resultado}

@router.post("/raiz")
def ruta_raiz(datos: RaizRequest):
    """
    Calcula la raíz cuadrada de un número. 

    Args:
        datos (RaizRequest): Cuerpo con el número.

    Returns:
        dict: Resultado de la raíz.
        
    Raises: 
        HTTPExpetion: Si el número es negativo. 
    
    """   
    try:
        resultado = raiz(datos.a)
        return{"resultado": resultado}
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

@router.get("/factorial/{n}")
def ruta_factorial(n: int):
    """
    Calcula el factorial de un número entero no negativo.

    Args:
        n (int): Número entero no negativo.

    Returns:
        dict: Resultado del factorial.

    Raises:
        HTTPException: Si el número es negativo.
    """
    resultado = factorial(n)
    return {"resultado": resultado} 
