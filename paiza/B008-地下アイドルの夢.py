# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_lines = raw_input()
a=input_lines.split()
N=int(a[0])
M=int(a[1])
if (N!=0 and M!=0):
	result=[]
	array = [[0 for col in range(N)] for row in range(M)]
	for i in range(0,M):
		results=0
		put=raw_input()
		put=put.split()
		for j in range(0,N):
			array[i][j]=put[j]
			results=results+int(array[i][j])
		result.append(results)
	#print result
	num=0
	for i in range(0,M):
		t=int(result[i])
		if(t>0):
			num=num+t
	print num
else:
	print 0