k = list(map(int,input().split()))
p = list(map(int,input().split()))

L = []

[L.append(i) for i in k if i in p]
[L.append(i) for i in p if i in k]
print(L)
