a=input()
a=list(a)
b=len(a)
if b%2!=0:
    c=b/2
    d=round(c)
    a[d]='*'
else:
    c=b/2
    d=round(c)
    a[d]='*'
    a[d-1]='*'
print(*a,sep="")
