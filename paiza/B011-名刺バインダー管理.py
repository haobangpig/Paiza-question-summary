#coding: utf-8
input_lines=raw_input()
input_array=input_lines.split()
n=int(input_array[0])
m=int(input_array[1])
if(m>2*n):
	dishu=int(m/(2*n))
	c=m%(2*n)
else:
	c=m
	dishu=0
#print dishu
if(c>n):
	diverse=c-n
	print dishu*(2*n)+(n-diverse)+1
else:
	print dishu*(2*n)+(n-c)+n+1

