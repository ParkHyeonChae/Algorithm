t = int(input())
result = []
new_string = ''

for i in range(t):
    r, s = input().split()
    s_len = len(s)

    for i in range(int(s_len)):
        new_string += s[i] * int(r)
    result.append(new_string)
    new_string = ''

for i in range(t):
    print(result[i])

