# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_lines = raw_input()
N=int(input_lines)
sum=0
for i in range(0,N):
	input_strings=raw_input()
	a=input_strings.split()
	m=int(a[1])
	if(int(a[0])==0):
		s=int(m/100)*5
	elif(int(a[0])==1):
		s=int(m/100)*3
	elif(int(a[0])==2):
		s=int(m/100)*2
	elif(int(a[0])==3):
		s=int(m/100)*1
	else:
		print "1"
	sum=sum+s
print sum