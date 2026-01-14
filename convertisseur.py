def conv_inch_cm(a):
    a_cm=a*2.54
    return a_cm
def conv_cm_inch(a):
    a_inch=a*0.394
    return a_inch
while True:
    print("""Vous souhaitez effectuer :
    a : Une conversion de inch vers cm
    b : Une conversion de cm vers inch""")
    type_conv = input("Votre choix : ")
    if type_conv=="a" or type_conv=="b":
        break
    else:
        print("Erreur, veuillez indiquer a ou b selon votre choix.")
print()
print("Combien de conversion(s) successive(s) voulez-vous faire au total?")
while True:
    nb_conversion = (input())
    try:
        nb_conversion_int = int(nb_conversion)
        break
    except:
        print("Erreur, veuillez indiquer un nombre entier")
print()
if type_conv=='a':
    for i in range(0,nb_conversion_int):
        while True:
            valeur_donnee = input("Valeur à convertir depuis inch : ")
            try:
                valeur_donnee_float = float(valeur_donnee)
                break
            except:
                print("Erreur, veuillez entrer un nombre valide.")
        valeur_convertie=str(conv_inch_cm(valeur_donnee_float))
        print(f"{valeur_donnee_float} inch vaut {valeur_convertie} cm")
else:
    for i in range(0,nb_conversion_int):
        while True:
            valeur_donnee = input("Valeur à convertir depuis cm : ")
            try:
                valeur_donnee_float = float(valeur_donnee)
                break
            except:
                print("Erreur, veuillez entrer un nombre valide.")
        valeur_convertie=str(conv_cm_inch(valeur_donnee_float))
        print(f"{valeur_donnee_float} cm vaut {valeur_convertie} inch")




