import random

def demander_nombre(nb_min,nb_max):
    reponse_int=0
    while reponse_int ==0:
        reponse= input(f"Quel est le nombre magique? (entre {nb_min} et {nb_max})")
        try:
            reponse_int = int(reponse)
        except:
            print("Vous devez entrer un nombre, rééssayez!")
        else :
            if reponse_int <1 or reponse_int >10:
                print(f"Vous devez choisir un nombre entre {nb_min} et {nb_max}. Réésayez avec un nombre conforme.")
                reponse_int=0
    return reponse_int

nombre_min=1
nombre_max=10
nombre_magique=random.randint(nombre_min,nombre_max)
nombre_vies=4


reponse=0
vies=nombre_vies
while not reponse==nombre_magique and vies>0:
    if vies > 1:
        print(f"Il vous reste actuellement {vies} vies.")
    elif vies == 1:
        print(f"Il vous reste actuellement {vies} vie.")
    reponse=demander_nombre(nombre_min,nombre_max)
    if reponse < nombre_magique:
        print("Le nombre magique est plus grand.")
        vies -=1
    if reponse > nombre_magique:
        print("Le nombre magique est plus petit.")
        vies -=1
if reponse == nombre_magique:
    print("Bravo vous avez gagné!")
if not reponse ==nombre_magique:
    print(f"Vous n'avez plus de vie. Vous avez perdu. Le nombre magique était {nombre_magique}.")


