from os import system, name

class Pizza:
    def __init__(self, dough, size, toppings, drink):
        self.dough = dough
        self.size = size
        self.toppings = toppings
        self.drink = drink
def clear():  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux
    else: 
        _ = system('clear')
clear()

mePizza = Pizza("asdasd", "dsadsa", "ssss", "dddd")
meList = []
meToppings = []
# print(mePizza.dough)
a = 5
while (a>0):
    mePizza.dough = "NobirAbi"
    mePizza.size = "SPY"
    mePizza.toppings = ["TOps", "TOpsİKİ"]
    mePizza.drink = "Drink"
    meList.append([mePizza.dough, mePizza.size, mePizza.toppings, mePizza.drink])
    # print(meList)
    a-=1
print(meList[3])
outList = meList[3]

print(outList[2])