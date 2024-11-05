def prime(n):
    k=n
    c=0
    for i in range(1,n+1):
        if k%i==0:
            c+=1
    if(c==2):
        return k
    else:
        return com(pre(n),next(n),n)
def pre(n):
    while True:
        c=0
        n=n-1
        for j in range(1,n+1):
            if n%j==0:
                c+=1
        if(c==2):
            return n
def next(n):
    while True:
        c=0
        n=n+1
        for j in range(1,n+1):
            if n%j==0:
                c+=1
        if(c==2):
            return n
def com(pre,next,n):
    if n-pre<=next-n:
        return pre
    else:
        return next
n=int(input())
l=[]
r=0
for i in range(n):
    k=int(input())
    r=prime(k)
    l.append(r)
for j in range(n):
    print(l[j])
