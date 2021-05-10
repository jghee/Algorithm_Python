import sys


def push(self, item):
    return self.append(item)


def pop(self):
    return self.pop() if self else -1


def size(self):
    return len(self)


def empty(self):
    return 0 if self else 1


def top(self):
    return self[-1] if self else -1


N = int(sys.stdin.readline())
stack = []

while N > 0:
    N -= 1
    command = sys.stdin.readline().rstrip().split(' ')

    if command[0] == "push":
        push(stack, command[1])
    elif command[0] == "pop":
        print(pop(stack))
    elif command[0] == "size":
        print(size(stack))
    elif command[0] == "empty":
        print(empty(stack))
    elif command[0] == "top":
        print(top(stack))
