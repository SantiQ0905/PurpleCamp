"""
--- oOo INSTRUCCIÓNES oOo ---

En la actividad de PYTHON de hoy su objetivo será hacer un "CHATBOT". Que cumpla con las siguientes caracteristicas:
DE CONTENIDO:
 - Tiene que tener una introducción donde se pregunte:
    + Nombre
    + Edad
 - Tiene que preguntar al usuario que preferirian hacer.
 - Tiene que preguntar al menos 3 cosas de conversación al usuario.
 - Tiene que tener un apartado de calculadora donde al menos podamos sumar y restar numeros enteros. 

DE CREATIVIDAD:
 - Tiene que tener un dibujo de introducción.
 - Tiene que contar con palabras de emoción (EJ. "WOW", "EPICO", "FANTASTICO", etc.).
 - Puede contar con comentarios.

DE CODIGO:
 - Su chatbot tiene que usar PRINTS, INPUTS, IFs y ELIFs. 
 - Tienen que cuidar la indentación, las variables y los inputs y outputs. 
 
"""
#AQUÍ EMPIEZEN SU CODIGO.

print("  _____   ___   _____ _____ ___  _    _  _____   __  ")
print(" /  __ \ / _ \ /  ___|_   _/ _ \| |  | |/ _ \ \ / /  ")
print(" | /  \// /_\ \ `--.  | |/ /_\ \ |  | / /_\ \ V /     ")
print(" | |    |  _  | `--. \ | ||  _  | |/\| |  _  |\ /     ")
print(" | \__/\| | | |/\__/ / | || | | \  /\  / | | || |     ")
print("  \____/\_| |_/\____/  \_/\_| |_/\/  \/\_| |_/\_/     \n")              

print("Hola soy Castaway y soy tu compa el de matematicas!!\n")

#Nombre
nombre = input("Buenas, ¿Cual es tu nombre?")
print(f"Hola, ", nombre, " que bonito nombre.")

#Edad
edad = input(f"¿Cuántos años tienes?")
print(f"Wow a tu edad, ", edad, " ya aprendiendo Python?!! GENIAL!!")


#Preguntar que hacer
print(f"¿Qué te gustaría hacer?")
queHacer = input(f"Podemos hacer una de estas dos cosas: A. Hablar o B. Matemática")

if queHacer == "A":
    #Cosa1
    cosa1 = input("¿Quien es tu actor/actriz favorito?")
    print("WOW, ", cosa1, "TAMBIEN ME ENCANTA!!")

    #Cosa2
    cosa2 = input("¿Cúal es tu color favorito??")
    print("EXCELENTE, el color ", cosa2, "tambien me encanta!!")

    #Cosa3
    cosa3 = input("¿Cuál es tu materia favorita?")
    print("INCREIBLE, la materia ", cosa3, "es muy interesante!!")

elif queHacer == "B":
    print("VAMOS A HACER MATEMÁTICAS LETSGOOOOOOOOOOOOOOOOOOO!!")

    sumaResta = input("¿Que te gustaria hacer? A. SUMA o B. RESTA")

    if sumaResta == "A":
        print("Vamos a Sumar!!")
        numSuma1 = int(input("Escribe el primer número: "))
        print("Primer número es: ", numSuma1)

        numSuma2 = int(input("Escribe el segundo número: "))
        print("Segundo número es: ", numSuma2)

        sumaTotal = int

        sumaTotal = numSuma1 + numSuma2
        print("La suma total es: ", sumaTotal)
    elif sumaResta == "B":
        print("Vamos a Restar!!")
        numResta1 = int(input("Escribe el primer número: "))
        print("Primer número es: ", numResta1)

        numResta2 = int(input("Escribe el segundo número: "))
        print("Segundo número es: ", numResta2)

        restaTotal = int

        restaTotal = numResta1 - numResta2
        print("La suma total es: ", restaTotal)



