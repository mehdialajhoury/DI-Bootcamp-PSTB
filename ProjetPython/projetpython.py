import random
#Embrace the challenge and have fun while coding! 🎯 The Number Guessing Game will sharpen your logic and Python fundamentals 🐍, while the Password Cracking Challenge will push your problem-solving skills to the next level 🔓💡.

#Keep experimenting, stay curious, and remember—every challenge is a step toward mastery! 🚀🔥 will push your problem-solving skills to the next level 🔓💡.

nombremagique = random.randrange(1,100)

for i in range(0,7):
    entree_utilisateur=input("Choisissez un nombre parmi 1 et 100")
    if entree_utilisateur != nombremagique:
        print("Ce n'est pas la bonne réponse, réessayez !")
    elif entree_utilisateur <=0:
        print("Le chiffre est inférieur à 1 ! Réessayez !")
    elif entree_utilisateur >100:
        print("Le chiffre est supérieur à 100 ! Réessayez !")
    else:
        print("BRAVO !! Vous avez deviné !")
        break

print("Le nombre magique était :"+str(nombremagique))