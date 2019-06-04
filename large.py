a=input()
a=a.split(" ")
if int(a[0])>int(a[1]) and int(a[0])>int(a[2]):
    print(int(a[0]))
elif int(a[1])>int(a[0]) and int(a[1])>int(a[2]):
    print(int(a[1]))
else:
    print(int(a[2]))
