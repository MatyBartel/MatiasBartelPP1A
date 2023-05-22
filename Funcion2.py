#2. Crear una función que se llame reemplazarCaracteres que reciba una cadena de caracteres como primer parámetro, 
# un carácter como segundo y otro carácter  como tercero,  la misma deberá reemplazar cada ocurrencia del segundo parámetro 
# por el tercero y devolver la cantidad de veces que se reemplazo ese carácter  en la cadena.

def reemplazarCaractres(cadena:str,caracter:str,caracter_reemplazo:str):
    """
    Function: Recibe por parametro una cadena, un caracter y un segundo caracter. Reemplazara en la cadena ingresada, el primer caracter por el segundo.

    Args:
        cadena (str): Cadena que vamos a querer usar.
        caracter (str): Caracter que queremos reemplazar.
        caracter_reemplazo (str): Caracter que reemplazaremos por el 1ro.
    
    Returns:
        nueva_cadena (str): Sera la nueva cadena con sus caracteres remplazados.
    """

    nueva_cadena = cadena.replace(caracter, caracter_reemplazo)  
    reemplazos = nueva_cadena.count(caracter_reemplazo)
    print("La cadena con los caracteres reemplazdos es: -",nueva_cadena," - se reemplazo ",caracter," por ",caracter_reemplazo," una cantidad de veces de: ",reemplazos)
    return nueva_cadena