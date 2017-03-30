import random 
import datetime
from datetime import timedelta

TeamList = ['Group 1','Group 2','Group 3','Group 4','Group 5','Group 6','Group 7',
    'Group 8','Group 9','Group 10','Group 11','Group 12','Group 13','Group 14',
    'Group 15','Group 16']
random.shuffle(TeamList)
print (TeamList)
TeamList = [TeamList[d:d+4] for d in range(0, len(TeamList), 4)]
print ('\nГруппы:')
print ('Group A: ',TeamList[0])
print ('Group B: ',TeamList[1])
print ('Group C: ',TeamList[2])
print ('Group D: ',TeamList[3])
print ('\nДаты:')

#текущая дата в нужном формате
##now_date = datetime.date.today()
##print(now_date)
##print(now_date.strftime('%d/%m/%Y, %I:%M'))

datestart=datetime.date(2016,9,14)
print(datestart.strftime('%d/%m/%Y, %I:%M'))
delta = timedelta(days=14)
print(delta)
while(datestart<datetime.date(2017,9,14)):
    datestart=datestart+delta
    print(datestart.strftime('%d/%m/%Y, %I:%M'))
