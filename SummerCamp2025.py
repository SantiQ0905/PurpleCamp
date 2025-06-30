"""
📣✨ ¡BIENVENID@ A HORA DE PROGRAMAR! ✨📣

Hoy crearás tu primer **chatbot** con Python. Pero... ¡el código está incompleto! 😱
Tu misión es **rellenar los espacios con ¿?** usando las palabras mágicas de la programación. ¡Tú tienes el poder! 💻🧙‍♂️

🧩 ¿Qué significan los ¿?? 
Donde veas un ¿?, tú tienes que escribir una **palabra clave** o una **función de Python**. Usa esta tabla para saber qué va en cada tipo de espacio:

👾 TABLA DE PALABRAS MÁGICAS:
---------------------------------------
`print`  👉 (para mostrar cosas en pantalla)
`input`  👉 (para pedirle algo al usuario)
`if`     👉 (para tomar decisiones)
`elif`   👉 (más decisiones si la primera no se cumple)

🎯 TU OBJETIVO:
---------------------------------------
✅ Preguntar el nombre y edad del usuario.
✅ Preguntar si quieren platicar o hacer matemáticas.
✅ Si escogen platicar: hacerle 3 preguntas divertidas.
✅ Si escogen matemáticas: permitir Sumar, Restar, Dividir o Multiplicar.
✅ ¡Usa muchas palabras emocionantes como WOW, FANTÁSTICO, INCREÍBLE!
✅ ¡Dibuja algo divertido con texto al inicio (ASCII art)!

🎉 BONUS:
---------------------------------------
¡Si terminas antes, puedes decorar tu chatbot con emojis, más preguntas o colores usando código ANSI!

📌 Recuerda:
- No borres los textos entre comillas ("") — ¡solo cambia los ¿? por la palabra correcta!
- Cuida la indentación. Si algo va dentro de un `if`, ¡va con espacio al inicio!
- Puedes pedir ayuda si te atoras. ¡Estamos para ayudarte!

💡 ¡Diviértete programando, crea tu mundo y haz que tu chatbot cobre vida!
"""


# Dibujo de introducción         

¿?("¡Hola! Soy Castaway, tu compa de matemáticas!!\n")

nombre = ¿?("¿Cómo te llamas? ")
¿?("Hola", nombre, "¡qué bonito nombre!")

edad = ¿?("¿Cuántos años tienes? ")
¿?("WOW! Ya tienes", edad, "años. ¡INCREÍBLE!\n")

¿?("¿Qué te gustaría hacer?")
queHacer = ¿?("A. Platicar  B. Matemáticas")

if queHacer == "A":
    cosa1 = ¿?("¿Cuál es tu color favorito? ")
    ¿?("¡WOW!", cosa1, "es un color genial!")

    cosa2 = ¿?("¿Qué animal te gusta más? ")
    ¿?("¡FANTÁSTICO!", cosa2, "es muy interesante!")

    cosa3 = ¿?("¿Qué materia te gusta más en la escuela? ")
    ¿?(cosa3, "es una gran materia. ¡ÉPICO!\n")

elif queHacer == "B":
    ¿?("¡Hora de MATEMÁTICAS! 🎉")

    operacion = ¿?("Elige: A. Sumar  B. Restar  C. Dividir  D. Multiplicar")

    if operacion == "A":
        num1 = int(¿?("Escribe el primer número: "))
        num2 = int(¿?("Escribe el segundo número: "))
        resultado = num1 + num2
        ¿?("La suma es:", resultado)

    elif operacion == "B":
        num1 = int(¿?("Primer número para restar: "))
        num2 = int(¿?("Segundo número para restar: "))
        resultado = num1 - num2
        ¿?("La resta es:", resultado)

    elif operacion == "C":
        num1 = int(¿?("Primer número para dividir: "))
        num2 = int(¿?("Segundo número para dividir: "))
        resultado = num1 / num2
        ¿?("El resultado de la división es:", resultado)

    elif operacion == "D":
        num1 = int(¿?("Primer número para multiplicar: "))
        num2 = int(¿?("Segundo número para multiplicar: "))
        resultado = num1 * num2
        ¿?("El resultado de la multiplicación es:", resultado)

¿?("\n¡Gracias por jugar con tu chatbot! ¡Eres increíble! ⭐")
