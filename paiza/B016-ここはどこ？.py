#coding:utf-8
data=raw_input()
data=data.split()
w=int(data[0])
h=int(data[1])
steps=int(data[2])

init=raw_input()
init=init.split()
x_init=int(init[0])
y_init=int(init[1])

direction=[]
num=[]
x=x_init
y=y_init
for i in range(0,steps):
	inputway=raw_input()
	inputway=inputway.split()
	direction.append(inputway[0])
	num.append(inputway[1])  
	if(inputway[0]=='U'):
		x=x	
		y=(y+(int(num[i])))%(h)
	elif(inputway[0]=='D'):
		x=x
		y=(y-int(num[i]))%(h)
	elif(inputway[0]=='L'):	
		y=y
		x=(x-int(num[i]))%(w)
	elif(inputway[0]=='R'):
		y=y
		x=(x+(int(num[i])))%(w)
print ("%d %d")%(x,y)