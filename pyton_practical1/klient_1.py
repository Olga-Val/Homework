class Klient :
    def __init__(self,name,soneim,city,balance):
        self.name = name
        self.soneim = soneim
        self.city = city
        self.balance = balance
    def get_guest(self):
        return f' {self.name}  {self.soneim} , г. {self.city}.'

klient_1 = Klient('Иван',"Петров","Москва",50)
klient_2 = Klient("Владимир","Зайцев","Кострома",50)
klient_3 = Klient("Олеся","Янина","Новосибирск",50)

guest_list = [klient_1,klient_2,klient_3]
for klient in guest_list:

  print(klient.get_guest())