import random

command = int(input("난수를 몇 번 생성할 것인가요> "))
for i in range(command):
    print(random.randrange(1, 101))
