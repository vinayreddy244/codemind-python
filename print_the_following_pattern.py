n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(0 if j==i else "x",end="")
    print()