pizzas_name=("4 fromages", "Calzone", "Hawai")
pizzas_price=(10.5,11,8)

name_and_price=list(zip(pizzas_name,pizzas_price))
print(name_and_price)

for (name,price) in name_and_price:
    print(f"{name} : {price} €"exit)