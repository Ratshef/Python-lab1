class VozrastEror(Exception):
    pass
try:
    g=[]
    i=0
    while i<6:
        x=int(input("Введите число "))
        g.append(x)
        i=i+1


    
    k=sorted(g)
    print(g)
    print(k)
except ValueError:
    print("Ошибка! Вы ввели букву! Введите число!")
else:
    try:
        if k!=g:
            raise VozrastEror
    except VozrastEror:
        print("False")
    else:
        print("True")

