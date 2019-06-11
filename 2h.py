b=int(input())
ac=input()
ac=ac.split(" ")
c=0
ac=[int(x) for x in ac]
ac.sort(reverse=True)
for i in ac:
    if i==0:
        c=c+1
if c==b:
    print(0)
else:
    print(*ac, sep="")
