def gcd(a,b): 
    if a>b: 
        return gcd(b,a) 
    elif a==0: 
        return b 
    else: 
        return gcd(b%a,a)
t=int(input())
while t:
    n,a,b,k=map(int,input().split()) 
    ano=n//a 
    bno=n//b 
    cno=n//((a*b)//gcd(a,b)) 
    if (ano+bno-(2*cno))>=k:
        print('Win') 
    else: 
        print('Lose')
        t-=1