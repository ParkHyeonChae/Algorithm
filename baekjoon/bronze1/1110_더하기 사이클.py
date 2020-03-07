n = int(input())

check = n
left_num = 0
right_num = 0
new_num = 0
count = 0

if n >= 0 and n <= 99:
    while True:
        left_num = n // 10
        right_num = n % 10
        new_num = right_num*10 + (left_num+right_num)%10
        count+=1
        n = new_num

        if check == new_num:
            break
        
    print(count)