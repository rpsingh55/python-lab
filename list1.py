
k = list(map(int,input().split()))
l = []
for i in k:
 if i not in l:
  l.append(i)

for i in range(len(l)):
     if i!=len(l)-1:
         print(l[i],end="*")
     else:
         print(l[i])
 


