ac=input()
ac=ac.split(" ")
b=[]
for i in ac:
    b.append(i[::-1])
print(*b,sep=" ")
