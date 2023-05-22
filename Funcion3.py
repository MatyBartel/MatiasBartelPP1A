#3. Crear una función que se llame ordenarCaracteres que reciba una cadena de caracteres como parámetro 
# y su responsabilidad es ordenar los caracteres de manera ascendente dentro de la cadena. 
# Ejemplo si le pasamos "algoritmo" la deja como "agilmoort"

def ordenarCaracteres(cadena:str):
    """
    Function: Recibe una cadena por parametro y utiliza la funcion burbuja que va intercambiando segun cual es mayor, ordena de forma ascendente segun el abecedario.

    Args:
        Cadena (str): Es la cadena que reemplazaremos

    Returns:
        cadena_ordenada: Nos retorna la cadena ordenada
    """
    largo= len(cadena)
    lista_cadena = list(cadena)
    
    for i in range(largo - 1):
        for j in range(0, largo - i - 1):
            if lista_cadena[j] > lista_cadena[j + 1]:
                lista_cadena[j], lista_cadena[j + 1] = lista_cadena[j + 1], lista_cadena[j]

    cadena_ordenada = ''.join(lista_cadena)
    print(cadena_ordenada)
    return cadena_ordenada