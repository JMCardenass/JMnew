print("Ingrese una lista de palabras separadas por coma")
palabras = input()
palabras_lista = palabras.split(",")  
for palabra in palabras_lista:
        print(palabra)