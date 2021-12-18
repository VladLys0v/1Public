#написать программу, которая будет подсчитывать общую стоимость билетов
#цена 1 билета зависит от возраста посетителя
#если зарегистрировано больше 3х человек - скидка к полной стоимости = 10%
try:
    amount = int(input('количество:'))
    age=None
    price=0
    i=0
    sum=0
    while i<amount:
        i+=1
        age = int(input(f'{i} билет: возраст:'))
        if 1<=age<18:
            price=0
            print('Бесплатно')
        elif 18<=age<=25:
            price=990
            print(f'{price} руб.')
        elif 100>age>25:
            price=1390
            print(f'{price} руб.')
        else:
            while True:
                print('Возраст указан неверно. Попробуйте снова.')
                break
            break
        sum=sum+price
except:
    print("Пожалуйста введите число билетов заново. Введенное значение не является числом")
if amount>=3:
    sum=sum-(sum*0.1)
if amount<=0:
    raise Exception('Извините, количество заказываемых билетов не может быть меньше 1')
print("ИТОГО:",int(sum),"руб")
