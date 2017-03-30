s=input('Введите слова ')
lst=s.split()
lst2=[]
for i in range(len(lst)):
	if lst[i].istitle():
		lst2.append(lst[i].upper())
	else:
		lst2.append(lst[i])
print(lst2)
svihod=''
for i in range(len(lst2)):
	svihod=svihod+str(lst2[i])+' '	
print(svihod)
