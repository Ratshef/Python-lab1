s=input('введите слова ')
k=s.split()
str1=[]
str2=[]
str3=[]
for i in range(len(k)):
	if len(k[i])>7:
		str1.append(k[i])
	elif 4<=len(k[i])<=7:
		str2.append(k[i])
	else:
		str3.append(k[i]) 

lst=[]
lst.extend(str1)
lst.extend(str2)
lst.extend(str3)
print(lst)
