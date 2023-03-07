from os import system, name

# Sınıfları tanımla 
# Toppings liste olarak değiştirilecek
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
# Girdileri hazırla, 
# kaç tane pizza alınacağı seçilecek her pizza için pizzanın türü ve malzeme ekleme çalışacak
# malzemeler eklenecek malzemeleri liste olarak tutup gönderebiliriz belki 
# birden fazla malzeme eklenebileceği için while döngüsü içinde yaz 
# aynı döngüyü pizza ve içeceğe de ekle 
# switch case içinde çalışması için işlev yaz 
# switch case yapısı içinde satır atlat veya işlev çağır 
# switch case'ler işlev içine yazılıp çağırılabilir, böylece menü içinde durma veya diğer menülere geçme seçenek olarak eklenebilir
pizzaClass = Pizza("","","","")
pizzaNum = int(input("Kaç tane pizza alınacak?\nYanıt: "))

while(pizzaNum > 0):
    selectedDough = input("Pizza hamuru seçin: \n1 - Margaritalı\n2 - Peperoni\n3 - Balıklı\n4 - Kaburgalı\n5 - Tavuklu")
    # Değerlerin nere gittiği belli değilt düzelt, string olarak gidecek
    match selectedDough:
        case "1":
            pizzaClass.dough = "Margarita"
        case "2":
            pizzaClass.dough = "Peperoni"
        case "3":
            pizzaClass.dough = "Balıklı"
        case "4":
            pizzaClass.dough = "Kaburgalı"
        case "5":
            pizzaClass.dough = "Tavuklu"
        case _:
            print("Hatalı giriş.")

    selectedSize = input("Pizza boyutu seçin: \n1 - Küçük boy\n2 - Orta boy\n3 - Büyük boy\n Seçiminiz: ")

    match selectedSize:
        case "1":
            pizzaClass.size = "Küçük boy"
        case "2":
            pizzaClass.size = "Orta boy"
        case "3":
            pizzaClass.size = "Büyük boy"
        case _:
            print("Hatalı giriş.")

    clear()

    toppingSelection = input("Pizzanın üstüne ek malzeme istiyor musunuz?\n(e/h): ")
    if(toppingSelection == "e"):
        check = 1
        '''
        while(check == 1): Burda kullanıcı sonlandırana kadar malzeme eklenecek
            input("1 - Zeytin\n2 - Mantar\n3 - Kaşar\n4 - Soğan\n5 - Keçi peyniri\n6 - Mısır")
            match toppingSelection:
                case "1":

        '''

    answer = input("İçecek alır mısınız?\ne/h: ")
    if(answer == "e"):
        selectedDrink = input("1 - Ayran\n2 - Kola\n3 - Fanta\n4 - Gazoz\n5 - Soda\nHangisini alırsınız: ")
        match selectedDrink:
            case "1":
                drink = 1
            case "2":
                drink = 2
            case "3":
                drink = 3
            case "4":
                drink = 4
            case "5":
                drink = 5
            case _:
                print("Hatalı girdi.")

    clear()

    # Girdileri işle


    # orderedPizza = Pizza(size, toppings, drink)

    pizzaNum-=1
    # Tamamlama ve kayıt için ilet