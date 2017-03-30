class Kart16Eror(Exception):
    pass
try:
    deb_kart=int(input('Введите цифры для карты '))
    
except ValueError:
    print("Ошибка! Вы ввели букву! Введите число!")
else:
    try:
       str_kard=str(deb_kart)
       if len(str_kard)!=16:
           raise Kart16Eror
        
    except Kart16Eror:
           print(len(str(str_kard)))
           print("Карта должна содержать 16 цифр!")
    else:
        #str=deb_kart[0:4]+'*'*8+deb_kart[12:16]
        print(str_kard[0:4],'*'*8,str_kard[12:16])
