s=input("Введите предложение ")
print(s)
lst=list(s)
print(lst)
for i in range(len(lst)):
    kol=lst.count(lst[i])
    if kol==1:
        print(lst[i])
