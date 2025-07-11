"""
Servicios que implementan la lógica de negocio para operaciones matemáticas.
"""
import math #estandar 
from fastapi import HTTPException #terceros

def sumar(a: float, b: float) -> float:
    """
    Suma dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la suma.
    """
    return a + b

def restar(a:float, b:float) -> float:
    """
    Resta dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la resta.
    """
    return a - b

def multiplicar(a:float, b:float) -> float:
    """
    Multiplicación dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la multiplicación.
    """ 
    return a * b

def dividir(a:float, b:float) -> float:
    """
    División dos números.

    Args:
        a (float): Diviendo.
        b (float): Divisor.

    Returns:
        float: Resultado de la división.
        
    Raises:
        ValueError: Si b es cero. 
    """ 
    if b==0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b 

def potencia(a:float, b:float) -> float:
    """
    Potencia de a ^ b.

    Args:
        a (float): Base.
        b (float): Exponente.

    Returns:
        float: Resultado de a elevado a la b.
    """ 
    return a ** b

def factorial(n: int) -> int:
    """
    Calcula el factorial de un número entero no negativo.

    Args:
        n (int): Número entero.

    Returns:
        int: Factorial del número.

    Raises:
        HTTPException: Si el número es negativo.
    """
    if n < 0:
        raise HTTPException(status_code=400, detail="El número debe ser no negativo")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def raiz(a:float) -> float:
    """
    Calcula la raíz cuadrada de un numero a.

    Args:
        a (float): Número (no negativo).
        
    Raises:
        ValueError: Si el numero es negativo.
    """
    if a < 0 :
        raise ValueError ("No se puede calcular la raíz cuadrada de un número negativo.")
    return math.sqrt(a)