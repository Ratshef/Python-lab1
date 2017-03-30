import random
n=random.randint(1,100)
lst=[]
for i in range(n):
	lst.append(random.randint(1,100))
print('Количество элементов n =',n)
print(lst)
i=0
p=1
while (n>p):
	p=p*2
	i=i+1
k=p-n
print('Степень двойки p=',p)
print('Количество добавленных нелей k =',k)
for i in range(k):
	lst.append(0)
print(lst)
