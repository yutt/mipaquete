'''
Este módulo contiene funciones de transformación de strings para 
generar textos en mayúsculas o minúsculas, utilizando las operaciones 
de las que el propio lenguaje dispone
'''


def minusculas (text:str)->str:
    '''
    Devuelve una versión en minúsculas del texto almacenado en text
    
    Parametros
    ----------

    :param text: el texto a mostrar en minúsculas

    Ejemplo
    -------

    >>> from mipaquete.string import minusculas
    >>> minusculas("HOLA")
    'hola'
    '''
    return text.lower()

def mayusculas (text:str)->str:
    '''
    Devuelve una versión en mayúsculas del texto almacenado en text

    Parametros
    ----------

    :param text: el texto a mostrar en mayúsculas

    Ejemplo
    -------

    >>> from mipaquete.string import mayusculas
    >>> mayusculas("hola")
    'HOLA'
    '''
    return text.upper()
