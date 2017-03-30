import random
import sys

class OutOfMoney(Exception):
    pass

def bankomat(banks,money):
    _money=money
    _banks=banks.copy()
    pos_banks=[1000,100,50,10]
    kol=[]
    for i in pos_banks:
        kol=money//i
        if kol>=1:
            for k in range(kol,0,-1):
                if banks[i]-k>=0 and money-k*i>=0:
                    money-=k*i
                    banks[i]-=k
                    print(k,'*',i)
    if money!=0:
        print('-'*20)
        print('Банкомат временно не работает')
        raise OutOfMoney
    print("Купюры",_banks)
    print("Нужно снять",_money)
    print("Осталось купюр",banks)
    print("-"*20)
    return banks

#словарь, ассоциативный массив - друг другу соответствую
bnk={j:random.randint(1,10) for j in [1000,100,50,10]}
print("Купюры в банкомате",bnk)
for i in sys.stdin:
    #ввод суммы
    try:
        sum=int(input("Введите нужную сумму для выдачи наличными "))
        if sum<10 or sum>10000:
            raise ValueError
    except ValueError:
        print("Введите сумму больше 0 и меньше 10000")
        print("-"*20)
    #выдача денег
    try:
        bnk=bankomat(bnk,sum)
    except OutOfMoney:
        break
        
