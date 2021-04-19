"""
for i in range(10, 22, 2):
    print(i)
print()
for i in range(5, 0):
    print(i)
print()
for i in range(5):
    print(i)
print()
for i in range(5, 11):
    print(i)
print()
for i in range(1,  5):
    print(i)
    
a = int(input("숫자를 입력해주세요 : "))

if a % 2 == 0:
    print(str(a) + "는(은) 짝수입니다.")
else:
    print(str(a) + "는(은) 홀수입니다.")
   
i = 0

while True:
    print(i)
    i += 1
    if i == 100:
        break
        
listA = [10, 20, 30, 40]
sum = 0
for i in listA:
    sum += i
print(sum)

print(not 0)
print(not 3 > 5)
print(not 1 is 1.0)
print(7 == 7 and 10 != 7)
print(4 % 2 == 2)

sum, k = 0, 0
for k in range(1, 5):
    if k % 2 == 0:
        continue
    sum += k
print("합계 %d" % sum)
"""
code = ["C", "G", "B", "E", "D", "F", "A", "H", "I"]
code.sort()
print(code)

del code[4] #E지워짐
print(code)

code.append("J")
print(code)

code.insert(4, "E")
print(code)

code.pop()
print(code)
