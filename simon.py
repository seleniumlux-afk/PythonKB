import time
import os
import random

def clear_screen():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Linux / Mac
    else:
        os.system('clear')
print("Bienvenue dans le jeu du Simon des chiffres!")
score = 0
time.sleep(2)

sequence=""
for i in range (0,3):
    sequence+=str(random.randint(0, 9))


while True :
    sequence+=str(random.randint(0,9))
    print("Retenez cette séquence :")
    print(sequence)
    time.sleep(3)
    clear_screen()
    while True :
        print("Taper votre séquence complète :")
        reponse = input("")
        try:
            test_reponse=int(reponse)
            if reponse==sequence:
                score+=1
                print(f"Bonne réponse! Votre score actuel est de {score}")
                time.sleep(2)
                clear_screen()
                break
            else:
                break
        except ValueError:
            clear_screen()
            print("Erreur, la séquence ne comporte que des chiffres! Veuillez entrer une séquence de chiffres!")
    if reponse != sequence:
        break
print(f"Mauvaise réponse, la bonne réponse était {sequence}")
print(f"Votre score final est de {score}")