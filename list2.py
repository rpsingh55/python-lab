k = list(map(int,input().split()))
l = []
for i in k:
 if i not in l:
  l.append(i)
print(*l)
