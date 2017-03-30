class VozrastEror(Exception):
    pass
try:
    g=[2,4,7,9,6]
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

