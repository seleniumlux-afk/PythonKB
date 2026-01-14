import turtle

def escalier(taille,nb):
    for i in range(0,nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
        taille -=5
    t.forward(taille)
    #nb marches de taille pixels

def carres(cote_depart,nb):
    for i in range (1,nb):
        carre(cote_depart*i)


def carre(cote):
    for i in range(0,4):
        t.forward(cote)
        t.left(90)

t = turtle.Turtle()

carres(50,10)

#escalier(50,8)



turtle.done()

