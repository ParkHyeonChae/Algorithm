n = int(input())

count = 0
movie = 666

while True:
    if '666' in str(movie):
        count += 1
    if count == n:
        print(movie)
        break
    movie += 1