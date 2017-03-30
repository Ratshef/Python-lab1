lst=['pythonworld.ru','ps.readthedocs.io/','www.youtube.com']
print(lst)

lst2=[]
s='http:/'
for i in range(len(lst)):
	if lst[i].startswith('www'):
		lst2.append(s+lst[i])
	else:
		lst2.append(lst[i])
print(lst2)

lst3=[]
for i in range(len(lst2)):
	if not lst2[i].endswith('.com'):
		lst3.append(lst2[i]+'.com')
	else:
		lst3.append(lst2[i])
print(lst3)
