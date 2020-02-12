a=int(input("Enter initial range value "))
b=int(input("Enter final range value "))
for i in range(a,b+1):
	p=i
	q=i
	c=0
	while (p>0):
		c=c+1
		p=p//10
	s=0
	while (q>0):
		r=q%10
		s=s+r**c
		q=q//10
	if(i==s):
		print(i," is an armstrong number")
	
