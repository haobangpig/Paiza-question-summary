#coding:utf-8
input_lines=raw_input()
input_array=input_lines.split()
a=int(input_array[0])
b=int(input_array[1])
c=int(input_array[2])

n=int(raw_input())
timehour=[]
timemin=[]
#array = [[0 for col in range(N)] for row in range(n)]
for i in range(0,n):
	timeinput=raw_input()
	timeinput=timeinput.split()
	hour=int(timeinput[0])
	mins=int(timeinput[1])
	timehour.append(hour)
	timemin.append(mins)

StationTime=9*60-b-c
tempHour=int(StationTime/60)
tempMin=int(StationTime%60)
righttrain=[]
for i in range(0,n):
	count=(timehour[i]*60)+timemin[i]
	if(StationTime>count):
		righttrain.append(int(i))
trainNum=int(righttrain[-1])
#print trainNum
getTraintime=timehour[trainNum]*60+timemin[trainNum]
startTime=getTraintime-a
h=startTime/60
m=startTime%60
print "%02d:%02d"%(h,m)

