class OtrizatEror(Exception):
    pass
try:
    cost=float(input('Введите стоимость '))
except ValueError:
    print("Ошибка! Вы ввели букву! Введите число!")
else:
    try:
       if cost<=0:
           raise OtrizatEror
    except OtrizatEror:        
           print("Число меньше нуля! Введите больше нуля!")
    else:
           print(int(cost), 'руб.',round((cost - int(cost)) * 100),'коп.')

	
