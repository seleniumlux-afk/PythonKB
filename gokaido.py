questions = []
print("Saisir les points de grammaire (saisir 'fin' pour terminer)")
while True:
    q = input(">> ")
    if q.lower() == "fin":
        break
    questions.append(q)

for q in questions:
    print(f"{q} : aizome n'a jamais entendu, et n'utilise pas ça au quotidien")

