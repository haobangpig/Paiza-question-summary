# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
#一定要！！转换成int型之后再运算，不然会出错！！！！

a=[]
for i in range (0,5):
	input_lines = raw_input()
	a.append(input_lines)
max=a[0]
min=a[0]
for i in range(0,5):
	if int(a[i])>int(max) :
		max=a[i]
	elif(int(a[i])<int(min)):
		min=a[i]
	print max,min
print max
print min
