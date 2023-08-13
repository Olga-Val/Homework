zarplata={"БТК":250, "ММФ":230, "ЖЭУ":150 }
chasi=int((input("Введите колличество рабочих часов:")))
itogo=[]
itogo.append(int(zarplata["БТК"]*chasi))
itogo.append(int(zarplata["ММФ"]*chasi))
itogo.append(int(zarplata["ЖЭУ"]*chasi))
print("Итоговая зарплата без вычета налога:",itogo )
itogo=float(input("Введите оклад без вычета налога:"))
procent=float(input("Введите ставку подаходного налога:"))
nalog=itogo*procent/100
summa=itogo-nalog
print("Итоговая зарплата после вычета налога:",summa)

