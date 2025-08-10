xdot = int(input())
ydot = int(input())

if xdot < 0 and ydot < 0 :
    print(3)
elif xdot < 0 and ydot > 0 :
    print(2)
elif xdot > 0 and ydot < 0 :
    print(4)
else :
    print(1)