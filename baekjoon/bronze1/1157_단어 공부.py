# 1157_단어 공부.py

import sys
input = sys.stdin.readline

arr = [0]*26
max_alp = 0
# alp_index = None
# overlab_cnt = 0

s = list(input().upper())

# if len(s) == 2:
#     print(s[0])
# else:
for i in range(len(s)):
    for j in range(26):
        if ord(s[i]) == j+65:
            arr[j] += 1

if arr.count(max(arr)) >= 2:
    print("?")
else:
    print(chr(arr.index(max(arr))+65))
    # for i in range(26):
    #     if max_alp <= arr[i]:
    #         if max_alp != arr[i]:
    #             max_alp = arr[i]
    #             alp_index = i
    #         else:
    #             overlab_cnt += 1

    # if overlab_cnt > 1:
    #     print("?")
    # else:

    # print(chr(alp_index + 65))