import random
"""
a = [1.3, 2.6, 3.5, 4.7, 5.2]
for i in range(len(a)):
    a[i] = int(a[i])
print(a)

a = [1.3, 2.6, 3.5, 4.7, 5.2]
a = list(map(int, a))
print(a)

a = list(map(str, range(10)))
print(a)

a = map(int, input("값을 입력하세요").split())
print(a)
a = list(a)
print(a)

list2d = [[10, 20], [30, 40], [50, 60]]
print(list2d)

list2d = [[10, 20], [30, 40], [50, 60]]
print(list2d[0][0])
print(list2d[1][1])
print(list2d[2][1])
list2d[1][0] = 88
print(list2d)

jaggedList = [[10, 20, 30], [40, 50],[60, 70, 80, 90]]
print(jaggedList)
jaggedList[0].append(1111)
print(jaggedList)
jaggedList[0].append(2222)
print(jaggedList)
jaggedList[2].extend([3333, 4444])
print(jaggedList)

jaggedList = [[10, 20, 30], [40, 50],[60, 70, 80, 90]]
for i in range(len(jaggedList)):
    for j in range(len(jaggedList[i])):
        print(jaggedList[i][j], end = " ")
    print()

#도전문제 5명의 이름, 전화번호, 나이를 입력받아서 2차원 리스트에 저장하는 프로그램을 작성하시오.
human = []
for i in range(5):
    human.append(list(map(str, input(str(i + 1) + "번째 사람의 이름, 전화번호, 나이를 입력해주세요 : ").split())))

print(human)

for i in range(len(human)):
    for j in range(len(human[i])):
        print(human[i][j], end = " ")
    print()
#도전문제 7 : 두 주사위 값이 같을 때까지 반복문의 실행 횟수를 출력하게 만드세요.
i, j = 1, 2
cnt = 0

while(i != j):
    i = random.randint(1, 6)
    j = random.randint(1, 6)
    print(i, j)
    cnt += 1
print("두 주사위의 값이 같습니다. 총", cnt, "번 반복했습니다.")

a = set([1, 2, 3, 4, 5])
a1 = [8, 9, 2, 7, 5, 3, 8, 2, 5, 3, 7, 3, 5, 5, 7]
a2 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
a3 = set([3, 6, 9, 12, 15])
b = set("love")
c = set()
d = set("I Love You")

print("\n-------------------+-------------------+-------------------+-------------------+")
print("a = ", a)
print("b = ", b)
print("c = ", c)
print("d = ", d)
print()

print("a1              =", a1)
print("중복 제거용 : set(a1) = ", set(a1))
print()
print("a2이 %s이고 a3이 %s일때," %(a2, a3))
print("a2와 a3의 합집합은 ", a2 | a3) # a2.intersection(a3)
print("a2와 a3의 교집합은 ", a2 & a3) # a2.union(a3)
print("a2와 a3의 차집합은 ", a2 - a3) # a2.difference(a3)
print("a3와 a2의 차집합은 ", a2 - a3) # a2.difference(a3)
print()

a2.add(10)
print("a2에 값 하나 추가하기 : a2.add(10)            ==>", a2)
a2.update([11, 12, 13])
print("a2에 값 여러개 추가하기 : a2.update([11, 12, 13])           ==>", a2)
a2.remove(13)
print("a2에 값 특정값 제거하기 : a2.remove(13)         ==>", a2)

print("-------------------+-------------------+-------------------+-------------------+\n")
"""
#도전문제8 로또번호 생성기 작성
#1 부터 45 사이의 숫자 6개를 출력 중복 X 
myList = []
while len(myList) < 6:
    lottery = random.randint(1, 45)
    if lottery not in myList:
        myList.append(lottery)
print(myList)

numbers = list(range(1, 46))
myList = []

while len(myList) < 6:
    lottery = random.choice(numbers)
    if lottery not in myList:
        myList.append(lottery)
print(myList)

numbers = list(range(1, 46))
myList = []
random.shuffle(numbers)

for i in range(6):
    if numbers[i] not in myList:
        myList.append(numbers[i])
    else:
        i -= 1
print(myList)
myList.sort()
print(myList)