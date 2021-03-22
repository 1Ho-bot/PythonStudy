listA = [0, 0, 0, 0, 0]
for i in range(5):
    listA[i] = input(str(i + 1) + "번째에 넣은 숫자를 적어주세요 : ")
print("listA에서 가장 큰 수는? " + max(listA))

listB = map(int, input("숫자를 적어주세요! : ").split())
print("listB에서 가장 큰 수는? ", max(listB))