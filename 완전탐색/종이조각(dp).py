N,M=map(int,input().split())
L=[]
for i in range(N):
    L+=list(input())
DP=[-1]*(1<<(N*M))
def f(x):
    print(bin(x)[2:])
    if x==0: return 0
    if DP[x]!=-1: return DP[x]
    ans=0
    for i in range(N*M-1,-1,-1):
        if x&(1<<i):
            y=x
            d=[]
            for j in range(i,i-(i%M)-1,-1):
                if (x&(1<<j))==0: break
                y^=(1<<j)
                d.append(L[N*M-1-j])
                r=f(y)+int(''.join(d))
                if r>ans: ans=r
            y=x
            d=[]
            for j in range(i,-1,-M):
                if x&(1<<j)==0: break
                y^=(1<<j)
                d.append(L[N*M-1-j])
                r=f(y)+int(''.join(d))
                if r>ans: ans=r

            break
    DP[x]=ans
    return ans
print(f((1<<(N*M))-1))
print(DP)