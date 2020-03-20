import string

s = input()

for a in string.ascii_lowercase:
    print(s.find(a), end=" ")