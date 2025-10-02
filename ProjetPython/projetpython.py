import random
#Embrace the challenge and have fun while coding! 🎯 The Number Guessing Game will sharpen your logic and Python fundamentals 🐍, while the Password Cracking Challenge will push your problem-solving skills to the next level 🔓💡.

#Keep experimenting, stay curious, and remember—every challenge is a step toward mastery! 🚀🔥 will push your problem-solving skills to the next level 🔓💡.

nombremagique = random.randrange(1,100)

for i in range(0,7):
    entree_utilisateur=input("Choisissez un nombre parmi 1 et 100. Vous avez 7 tentatives !")
    if int(entree_utilisateur) >=1 and int(entree_utilisateur) <=100:
        if entree_utilisateur != nombremagique:
            if int(entree_utilisateur) > nombremagique:
                print("C'est moins !")
            else:
                print("C'est plus !")
        else:
            print("BRAVO !! Vous avez deviné !")
            break
    else:
        print("Vous devez choisir un nombre entre 1 et 100 !!!")
print("Le nombre magique était :"+str(nombremagique))