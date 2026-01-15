def element_dans_liste(e,l):
    l_lower=[el.lower() for el in l]
    return e.lower() in l_lower

noms= ["Jean","Sophie","Martin","Christophe","Zoé","Martin"]

if element_dans_liste("JeaN",noms):
    print("Jean est là")
else:
    print ("Jean n'est pas là")


