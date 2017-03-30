import sys

class OutData(Exception):
    pass

def prowerka(data):
    count_digit=0
    count_lower=0
    count_upper=0    
    
    for i in data:
            if i.isdigit():
                count_digit+=1  # Считаем сколько цифр в пароле
            if i.islower():
                count_lower+=1  # Считаем сколько символов нижнего регистра
            if i.isupper():
                count_upper+=1  # Считаем сколько в верхнем регистре
    # Если длина пароля >6, есть цифра и есть одна заглавная и одна маленькая буква, то True  
    if len(data)>8 and count_digit>0 and count_lower>0 and count_upper>0:
        return "Пароль надежный"
    else:
        raise OutData
        
for i in sys.stdin:
    try:
        digit=input("Введите пароль ")
        if len(digit)<8:
            raise ValueError
    except ValueError:
        print("Введите пароль, состоящий минимум из 8 символов")
    try:
        #digit="1q2wg%3eSD"
        print(prowerka(digit))
    except OutData:
        print("Парoль не надежный")
        break
