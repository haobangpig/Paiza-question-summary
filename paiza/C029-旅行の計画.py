# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_lines = raw_input()
a=input_lines.split()
M=int(a[0])
N=int(a[1])
ar=[]
pr=[]
for i in range(0,M):
	put=raw_input()
	b=put.split()
	ar.append(int(b[0]))
	pr.append(int(b[1]))
average=0
sum=0
value=[]
for i in range (0,(M-N)+1):
	sum=0
	for j in range(i,i+N):
		sum=pr[j]+sum
	value.append(int(sum))
correct=min(value)
t=int(value.index(correct))
x=t+int(ar[0])
y=x+N-1
print x,y