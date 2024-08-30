import sys
sys.setrecursionlimit(10**5)

nodenum = int(input())
arr = [0]*(nodenum+1)

for _ in range(nodenum) :
    lst = list(map(str, input().split()))
    arr[ord(lst[0])-64] = [ord(lst[1])-64, ord(lst[2])-64]

def preorder(now) :
    if now == -18: return
    print(chr(now+64), end='')
    preorder(arr[now][0])
    preorder(arr[now][1])

def inorder(now) :
    if now == -18: return
    inorder(arr[now][0])
    print(chr(now+64), end='')
    inorder(arr[now][1])

def postorder(now) :
    if now == -18: return
    postorder(arr[now][0])
    postorder(arr[now][1])
    print(chr(now+64), end='')

preorder(1)
print()
inorder(1)
print()
postorder(1)