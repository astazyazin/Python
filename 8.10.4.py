i_year=int(input("Введите один из годов для проверки (1800,1900,1903,2000,2002): "))
if (i_year%4 == 0):
    if(i_year%100 == 0):
       if (i_year % 400 == 0):
           print(" Год " + str(i_year) + " является високосным ")
       else:
           print(" Год " + str(i_year) + " не является високосным ")
    else:
        print(" Год " + str(i_year) + " является високосным ")
else:
    print(" Год "+ str(i_year)+ " не является високосным " )