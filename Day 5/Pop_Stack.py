def push(x):
    global l, top, size
    if top == size - 1:
         print('overflow!')
         return
    top = top + 1
    l.insert(top, x)

def pop(x):
    global l, top, size
    top = top - 1


def display():
    if top == -1:
        print('underflow!')
        return
    for i in range(top, -1, -1):
        print(l[i])

l = list()
size = 5
top = -1
push(10)
push(20)
push(30)
pop(30)
display()
