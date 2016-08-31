input_lines = raw_input()
str=input_lines.split()
if str[0]<str[1]:
	print str[1]
elif str[0]>str[1]:
	print str[0]
elif str[0]==str[1]:
	print "eq"


