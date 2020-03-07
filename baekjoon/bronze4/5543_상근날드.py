min_burger = 2000
min_water = 2000

for i in range(3):
    burger = int(input())
    if  burger >= 100 and burger <= 2000:
        min_burger = min(burger, min_burger)

for i in range(2):
    water = int(input())
    if  water >= 100 and water <= 2000:
        min_water = min(water, min_water)

print(min_burger + min_water - 50)