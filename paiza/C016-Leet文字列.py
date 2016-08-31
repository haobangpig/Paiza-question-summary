# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
input_lines = raw_input()
a=input_lines.split()
str1=list(a[0])
i=0
for i in range(0,len(str1)):
	if(str1[i]=='A'):
		str1[i]='4'
	elif(str1[i]=='E'):
		str1[i]='3'
	elif(str1[i]=='G'):
		str1[i]='6'
	elif(str1[i]=='I'):
		str1[i]='1'
	elif(str1[i]=='O'):
		str1[i]='0'
	elif(str1[i]=='S'):
		str1[i]='5'
	elif(str1[i]=='Z'):
		str1[i]='2'

b=''.join(str1)
print b
