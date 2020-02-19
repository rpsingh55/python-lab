a = ()
print('enter element')
n = int(input())
for i in range(n) :
	d = input()
	if d.isalpha() :
		a += (d,)
	else :
		a += (eval(d),)
print(a)	

