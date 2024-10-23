rowlen, collen = map(int, input().split())
storenum = int(input())
store = []

for i in range(storenum+1) :
    direction, distance = map(int, input().split())
    if direction == 1 :
        store.append(distance)
    elif direction == 2 :
        store.append((rowlen-distance) + rowlen + collen)
    elif direction == 3 :
        store.append(rowlen*2 + collen + (collen-distance))
    elif direction == 4 :
        store.append(rowlen + distance)

Sum = 0
position = store[len(store)-1]
totalroad = rowlen*2 + collen*2

for i in range(len(store)-1) :
    if position < store[i] :
        dis = store[i] - position
        Sum += min(totalroad - dis, dis)
    elif position > store[i] :
        dis = position - store[i]
        Sum += min(totalroad - dis, dis)

print(Sum)