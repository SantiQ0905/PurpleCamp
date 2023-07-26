# Introduction Drawing
print(f"  BBBBBB     OOOOO    BBBBBB")
print(f"  BB   BB  OO    OO  BB   BB")
print(f"  BBBBBB   OO    OO  BBBBBB")
print(f"  BB   BB  OO    OO  BB   BB")
print(f"  BBBBBB     OOOO    BBBBBB \n")

print(f"BOB YOUR MATH BUDDY \n")


#Introduction
print(f"Let's get to know each other!")
print(f"Hello I'm BOB, I am a chatbot that helps you to do math homework and I'm here to give you company my friend! \n")
print(f"Let's introduce each other! \n")

#Ask for your name
name = input("What is your name? \n")
print("Nice to meet you ", name, "\n")

#Ask for your age
age = input("How old are you? \n")
print("WOW are you already learning Python at your age?, you are ", age, "\n")
print("THAT IS AWESOME!! \n")

#Ask for what to do
print("What should we do? \n")

whatToDo = input("A. Chill B. Math\n")

if whatToDo == "A":
    #Ask for three favourite things from the user
    print("Alright you've selected to Chill\n")
    
    #Thing 1
    colour = input("What is your favourite colour\n")
    print(f"Really?!", colour, "is my favourite colour too!!\n")

    #Thing 2
    musicArtist = input("So... Who is yor favourite music artist?\n")
    print(f"OMG I LOVE", musicArtist, " TOO AAAAAAAAA\n")

    #Thing 3
    purpleCamp = input("So are you liking PurpleCamp by Overture7421\n")
    if purpleCamp == "Yes":
        print("Awesome. I'm so happy you are enjoying PurpleCamp.\n")
    elif purpleCamp == "No":
        print("I'm sorry, hopefully you will enjoy it at the end.\n")

elif whatToDo == "B":
    #Calculator
    print("Alright you've selected to do some Math!!\n")
    operation = input("What do you wish to do? A. Addition B. Substraction\n")

    if operation == "A":
        print("Allright let's add some numbers.")
        add1 = int(input("Enter the first number: \n"))
        print("Number selected", add1)
        add2 = int(input("Enter the second number: \n"))
        print("Number selected", add2)
        print("Alright let's add ", add1, "and ", add2, ".\n")
        addition = int

        addition = add1 + add2
        print(addition)

    elif operation == "B":
        print("Allright let's substract some numbers.")
        sub1 = int(input("Enter the first number: \n"))
        print("Number selected", sub1)
        sub2 = int(input("Enter the second number: \n"))
        print("Number selected", sub2)
        print("Alright let's substract ", sub1, "and ", sub2, ".\n")
        substraction = int

        substraction = sub1 - sub2
        print(substraction)

#Farewell
print(f"All right time to go. It was wonderfull to talk with you! Have a nice day.\n")
print(f"BOB SHUTTING DOWN...")