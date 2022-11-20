'''
Este módulo contiene funcionalidades para sumar, restar o multiplicar números. 
Para ello se apoya en la propia funcionalidad del lenguaje a la hora de realizar 
estas operaciones
'''

def sumar(sumando1: int|float, sumando2: int|float)->int|float:
    '''
    Suma dos números
    
    Parámetros
    ----------

    :param sumando1: uno de los valores a sumar
    :param sumando2: el otro valor a sumar

    Ejemplo
    -------

    >>> from mipaquete.math import sumar
    >>> sumar(1, 1)
    2
    '''
    return sumando1 + sumando2

def restar(minuendo: int|float, sustraendo: int|float)->int|float:
    '''
    Resta dos números

    Parámetros
    ----------

    :param minuendo: valor inicial
    :param sustraendo: valor a restar al valor inicial

    Ejemplo
    -------
    >>> from mipaquete.math import restar
    >>> restar(1, 1)
    0
    '''
    return minuendo - sustraendo

def multiplicar(multiplicando1: int|float, multiplicando2: int|float)->int|float:
    '''
    Multiplica dos números

    Parámetros
    ----------
    
    :param multiplicando1: uno de los valores a multiplicar
    :param multiplicando2: el otro valor que participa en la multiplicación

    Ejemplo
    -------

    >>> from mipaquete.math import multiplicar
    >>> multiplicar(2, 2)
    4

    '''
    return multiplicando1 * multiplicando2
