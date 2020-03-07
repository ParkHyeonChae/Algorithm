num = int(input())

if num >= 1 and num <= 4000:
    if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
        print ('1')
    else:
        print('0')