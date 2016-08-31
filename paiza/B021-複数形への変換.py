#coding:utf-8
input_lines=raw_input()
N=int(input_lines)
original=[]
plural=[]
for i in range(0,N):
	data=raw_input()
	#data=data.split()
	original.append(data)
	if(data[-1]=="s" or data[-2:]=="sh" or data[-2:]=="ch" or data[-1]=="o" or data[-1]=="x"):
		muti=data+"es"
	elif(data[-1]=="f"):
		muti=data[:-1]+"ves"
	elif(data[-2:]=="fe"):
		muti=data[:-2]+"ves"
	elif(data[-1]=="y" and (data[-2]!='a'and data[-2]!='i'and data[-2]!='u'and data[-2]!='e'and data[-2]!='o')):
		muti=data[:-1]+"ies"
	else:
		muti=data+"s"
	plural.append(muti)

for i in range(0,N):
	print plural[i]