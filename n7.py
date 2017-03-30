Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s=input('Введите строку:   ')
Введите строку:   сегодня февраль, среда
>>> lst=list(s)
>>> lst
['с', 'е', 'г', 'о', 'д', 'н', 'я', ' ', 'ф', 'е', 'в', 'р', 'а', 'л', 'ь', ',', ' ', 'с', 'р', 'е', 'д', 'а']
>>> for i in range(len(lst):
	       
SyntaxError: invalid syntax
>>> for i in range(len(lst)):
	kol=lst.count(lst[i])
	if kol==1:
		print(lst[i])

		
г
о
н
я
ф
в
л
ь
,
>>> 
