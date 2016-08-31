# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_lines = raw_input()
a=input_lines.split()
x1=int(a[0])
y1=int(a[1])
r1=int(a[2])
x=[]
y=[]
r=[]
N=int(raw_input())
for i in range(0,N):
	b=raw_input()
	b=b.split()
	x.append(b[0])
	y.append(b[1])
r=r1*r1
for i in range(0,N):
	c=(int(x[i])-x1)*(int(x[i])-x1)+(int(y[i])-y1)*(int(y[i])-y1)
	if(c>=r):
		print "silent"
	else:
		print "noisy"