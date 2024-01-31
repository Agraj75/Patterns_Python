for i in range(1,5):
    for j in range(1,5-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end="")
    for l in range(1,i):
        print(i-1,end="")
    print(" ")

for i in range(1,6,1):
    for j in range(1,i+1,1):
        print("* ",end='')
    print("")

for i in range(1,6,1):
    for k in range(1,(5-i)+1,1):
        print(" ",end=' ')
    for j in range(1,i+1,1):
        print("*",end=' ')
    print(" ")

for i in range(1,6,1):
    for k in range(1,(5-i)+1,1):
        print(" ",end='')
    for j in range(1,i+1,1):
        print("* ",end='')
    print(" ")

for i in range(1,7,1):
    for k in range(1,i+1,1):
        print(" ",end=' ')
    for j in range(1,(6-i)+1,1):
        print("*",end=' ')
    print(" ")

for i in range(1,7,1):
    for k in range(1,i+1,1):
        print("",end='')
    for j in range(1,(6-i)+1,1):
        print("* ",end='')
    print(" ")
