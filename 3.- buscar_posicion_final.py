#FUNCION 3

def buscar_posicion_final(texto_ingresado, texto_buscado):
    
    encontrado = False
    
    for i in range(len(texto_ingresado)-1, len(texto_buscado)-1, -1):
        if texto_ingresado[i-len(texto_buscado)+1:i+1] == texto_buscado:
            encontrado = True
            return i-len(texto_buscado)+1
    if not encontrado:
        return -1

texto_ingresado = input("Ingrese un texto: ")
texto_buscado = input("Ingrese el texto a buscar: ")
resul = buscar_posicion_final(texto_ingresado, texto_buscado)
print("La cadena fue encontrada en la posicion: ",resul)