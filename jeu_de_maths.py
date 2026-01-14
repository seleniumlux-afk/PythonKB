import random

nombre_min=1
nombre_max=10
nombre_questions=4
moyenne=int(nombre_questions/2)

def poser_question():
    a= random.randint(nombre_min,nombre_max)
    b= random.randint(nombre_min,nombre_max)
    o=random.randint(0,1)
    juste=False
    operateur_str="+"
    if o==1:
        operateur_str="*"
    reponse=input(f"Calculez {a} {operateur_str} {b} = ")
    reponse_int=int(reponse)
    if o==1:
        calcul=a*b
    else:
        calcul=a+b
    if reponse_int == calcul:
        print("Réponse correcte")
        juste = True
    else:
        print("Réponse incorrecte")
    return juste

nombre_points=0

for i in range (0,nombre_questions):
    print(f"Question {i+1}/{nombre_questions} : ")
    juste=poser_question()
    if juste==True:
        nombre_points+=1
    if not i==nombre_questions-1:
        print(f"Score actuel : {nombre_points} / {i + 1}")
    print()
print(f"Votre score total est de {nombre_points} / {nombre_questions}")
if nombre_points==0:
    print("Vous êtes une fraude. Révisez vos maths!")
elif nombre_points == nombre_questions:
    print("Excellent, vous avez tous les points (encore heureux)!")
elif nombre_points <= moyenne:
    print("Peux mieux faire, vous êtes dans le bas du panier")
elif nombre_points > moyenne:
    print("Pas si mal, vous êtes au dessus de la moyenne!")







