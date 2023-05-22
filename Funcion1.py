# 1. Crear una función llamada aplicarAumento que reciba como parámetro el precio de un producto y devuelva 
# el valor del producto con un aumento del 5%. Realizar la llamada desde el main.

def aplicarAumento(precio:float)->float:
    """
    Function: Recibe por parametro un precio y le aumenta un 5% de ese precio.

    Args:
        Precio (float): Precio que queremos aumentar.

    Returns:
        Precio_Aumentado: Nos retorna el precio con un 5% de aumento.
    """

    aumento=5
    precio_aumentado=precio+(precio*aumento/100)
    print("El precio aumentado es:",precio_aumentado)
    return precio_aumentado