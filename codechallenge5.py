#cc5
#loop

for x in range(1, 7):
    for y in range(7, x, -1):
        print("*", end= " ")
    print()

print("======================")

for x in range(1, 7, 1):
    for y in range(0,x):
        print(x,end=" ")
    print()
