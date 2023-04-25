print("Bienvenido a la isla del tesoro")
decision1 = input("¿Qué camino deseas tomar: izquierda o derecha? ")

if decision1 == "derecha":
    print("Caíste en un foso y moriste")
elif decision1 == "izquierda":
    print("Sigues caminando y te toca elegir entre 3 diferentes caminos con diferentes colores")
    decision2 = input("¿Qué camino deseas tomar: rojo, azul o amarillo? ")
    if decision2 == "rojo":
        print("Caíste en un foso  de fuego y moriste")
    elif decision2 == "azul":
        print("Hora tienes que decicidir entre nadar o volar ")
        decicion3 = input("¿Qué camino deseas tomar: nadar o volar? ")
        while decicion3 == "nadar":
            print("vulve al inicio")
        if decicion3 == "volar":
            print("Caiste en un atajo")   
