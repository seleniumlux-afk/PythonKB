import time


#oeufs à la coque = 3 min
#oeufs mollets =6 mins
#oeufs dur = 9 mins
def temps_minutes(t):
    min=t//60
    return min
def temps_secondes(t):
    min=t//60
    sec=t-min*60
    return sec


while True:
    entree_recette = input("""Bienvenue dans le programme de cuisson des oeufs!
1 - Oeufs à la coque
2 - Oeufs mollets
3 - Oeufs durs
Veuillez indiquer la recette souhaitée en entrant 1,2 ou 3 :
    """)
    if entree_recette in ["1","2","3"]:
        recette=str(entree_recette)
        break
    else:
        print("Erreur, veuillez entrer une réponse valide :")

duree_cuisson_s=0
if recette == "1":
    duree_cuisson_s=180
elif recette =="2":
    duree_cuisson_s= 360
elif recette =="3":
    duree_cuisson_s=540

min=duree_cuisson_s//60
sec=duree_cuisson_s-min*60
temps_restant_cuisson=duree_cuisson_s

print(f"La cuisson démarre, le temps de cuisson total est de {min} minutes.")

while temps_restant_cuisson >0:
    i=0
    print(f"Temps restant : {temps_minutes(temps_restant_cuisson):02} min {temps_secondes(temps_restant_cuisson):02} s ",end="",flush=True)
    for i in range (0,10):
        print(".",end="",flush=True)
        time.sleep(1)
        i += 1
    temps_restant_cuisson-=10
    print()


print("Cuisson terminée, bon appétit!")
