noms= ["Jean","Sophie","Martin","Christophe","Zoé","Martin"]

'''nb_char =0
for nom in noms:
    nb_char+=len(nom)
print(nb_char)'''

'''list_length=[len(nom) for nom in noms]
nb_char=sum(list_length)
print(nb_char)'''

print("Total character count :",len("".join(noms)))
