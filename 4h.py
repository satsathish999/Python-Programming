b=int(input())
ac=input()
ac=ac.split(" ")
c=0
ac=[int(x) for x in ac]
for i in ac:
        if ac.count(i)!=2:
            print(i)
