sumbil=0
sumbil_1=0
sumbil_2=0
colbil=int(input("Введите колличество билетов, которое хотите приобрести:"))
for age in range(colbil):
    age=int(input("Введите возраст:"))
    if age < 18:
        sumbil+=0
        print("Стоимость билета:",sumbil)
    elif age >= 18 and age <= 25:
        sumbil_1+=990
        print("Стоимость билета:",sumbil_1)
    elif age >25:
        sumbil_2+=1390
        print("Стоимость билета:",sumbil_2)
sumbil_3=int(sumbil+sumbil_1+sumbil_2)
print("Общая стоимость билетов:",sumbil_3)
if colbil > 3:
 sumbil_3 -= sumbil_3 / 100 * 10
 print("Полная стоимость заказа со скидкой:", sumbil_3)










