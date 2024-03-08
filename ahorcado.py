import os
ps="gatito"
letras=[]
intentosm=7
intentos=0
print("bienvenido al juego de la m-word  x.x ")
print("debes adivinar la palabra para ganar, tienes solo 7 intentos! >:D ")

while intentos<intentosm:
    palabra = ""
    for letra_secreta in ps:
        if letra_secreta in letras:
            palabra += letra_secreta
        else:
            palabra += "_ "
    print(palabra)
    letra=input("Ingresa una letra > ").lower()
    if letra in letras:
        print("De verdad la misma letra ??? o.O ")
        continue
    letras.append(letra)
    if letra not in ps:
        intentos+=1
        print(f"SE EQUIVOCOOO!!! te quedan  {intentosm - intentos} intentos.")
    else:
        print("wow adivinaste eso vamo >")
    if palabra== ps:
        print("Ganaste esta vez! >:D")
        break
    if intentos == intentosm:
        print(f"Perdiste. La palabra secreta era: {ps}")
