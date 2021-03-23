"""
a = [1, 2, 3, 4, 5]
a.pop()
print(a)
a.pop()
print(a)

b = [1, 2, 3, 4, 5]
b.pop(2)
print(b)
del b[1]
print(b)

c = [1, 3, 5, 7, 9]
c.remove(5)
print(c)

c = [1, 3, 5, 7 ,9]
c.remove(6)
print(c)

d = [1, 3, 5, 7, 9, 11]
for i in range(2):
    data = int(input("리스트에서 삭제할 값을 입력하세요 : "))
    if data in d:
        d.remove(data)
        print(d)
    else:
        print("리스트에 존재하지 않는 값입니다.")
        print(d)

a = [10, 20, 30, 40, 50]
print(a.index(40))
print(a.index(25))

listA = [1, 2, 3, 4, 5, 6, 7, 8]
command = int(input("주소를 찾고 싶은 숫자를 적어주세요 : "))
if command in listA:
    print(listA.index(command))
else:
    print("리스트에 존재하지 않는 값입니다.")


a = [10, 20, 30, 40, 50, 60, 40]
print(a.index(40))

a = [10, 20, 30, 40, 50, 60, 40]
print(a.count(40))

b = [30, 10, 40, 20, 60, 50]
print(b)
b.reverse()
print(b)

#도전문제 5
girlfriend = ["소원", "예린", "은하", "유주", "신비", "엄지"]
command = input("이름을 입력하세요 : ")
if command in girlfriend:
    print(girlfriend.index(command),"번째 있습니다.")
else:
    print("리스트에 없는 이름입니다.")

#for, len사용
girlfriend = ["소원", "예린", "은하", "유주", "신비", "엄지"]
command = input("이름을 입력하세요 : ")
if command in girlfriend:
    for i in range(len(girlfriend)):
        if command == girlfriend[i]:
            print(i + 1, "번째에 있습니다.")
else:
    print("리스트에 존재하지 않는 이름입니다.")

b = [30, 10, 40, 20, 60, 50]
b.sort()
print(b)
b.sort(reverse = True)
print(b)

test = [3, 6, 2, 1, 7, 8, 9, 3, 2, 6, 7, 5, 2]
command = int(input("숫자를 입력해주세요 : "))
if test.count(command) > 1:
    print(str(test.count(command)) + "개")
elif command in test:
    print(test.index(command))
elif command not in test:
    print("값이 존재하지 않습니다.")

a = [1, 2, 3, 4, 5]
b = a
print(id(a))
print(id(b))
print(a)
print(b)
b[3] = 400
print(a)
print(b)

a = [1, 2, 3, 4, 5]
b = a.copy()
print(id(a))
print(id(b))
print(a)
print(b)
b[3] = 400
print(a)
print(b)

c = [1, 2, 3, 4, 5]
d = [6, 7, 8, 9, 10]
c.clear()
del d[:]
print(c)
print(d)

a = ["서울", "인천", "대전", "춘천", "전주", "광주", "울산", "부산"]
#for i in a:
#    print(i, end = "-")


for index, city in enumerate(a):
    print(city,"(",index,")")

a = [i for i in range(10)]
print(a)

b = [i + 1 for i in range(10)]
print(b)

listA = [i + 5 for i in range(10) if i % 2 == 1]
print(listA)

a = [1.3, 2.6, 3.5, 4.7, 5.2]
for i in range(len(a)):
    a[i] = int(a[i])
print(a)

a = [1.3, 2.6, 3.5, 4.7, 5.2]
a = list(map(int, a))
print(a)

a = list(map(str, range(10)))
print(a)

a = map(int, input("값을 입력해주세요").split())
print(a)
a = list(a)
print(a)

a = [10, 4, 67, 53, 6, 3, 9]
print("리스트의 최소값은", min(a))
print("리스트의 최대값은", max(a))
print("리스트의 값들의 합은", sum(a))
#도전문제
listQ = map(int, input("정수를 여러개 입력해 주세요.").split())
listQ = list(listQ)
print("합", sum(listQ), "최대값", max(listQ), end = "\n")
"""

#4의 배수와 6의 배수 출력 최소공배수 제외
for i in range(1, 101):
    if i % 4 == 0:
        if i % 6 != 0:
            print("4의 배수", i)
    if i % 6 == 0:
        if i % 4 != 0:
            print("6의 배수", i)