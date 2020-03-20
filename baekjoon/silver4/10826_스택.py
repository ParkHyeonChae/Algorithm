# n = int(input())
# stack = list()

# for i in range(n):
#     f = input()
#     if f.split()[0] == 'push':
#         stack.append(int(f.split()[1]))
#     elif f == 'pop':
#         if not stack:
#             print('-1')
#         else:
#             print(stack[-1])
#             stack.pop(-1)
#     elif f == 'empty':
#         if not stack:
#             print('1')
#         else:
#             print('0')
#     elif f == 'top':
#         if not stack:
#             print('-1')
#         else:
#             print(stack[-1])

import sys
input = sys.stdin.readline
count = int(input())
stack = []


def f(command_input):
    command = command_input.split()[0]
    if len(command_input.split()) > 1:
        number = command_input.split()[1]

    if command == 'push':
        stack.append(number)
    elif command == 'pop':
        if len(stack):
            print(stack[-1])
            stack.pop()
        else:
            print('-1')
    elif command == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print('-1')
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(0 if len(stack) else 1)


for i in range(count):
    f(input())