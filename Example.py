#생년월일 받고 년, 월, 일로 나누고 2000년 이전 생이면 20세기 2000년 이후 생이면 21세기
birth = input("생년월일을 8자로 적어주시길 바랍니다 : ")
print(birth[0 : 4] + "년")
print(birth[4 : 6] + "월")
print(birth[6 : 8] + "일")

if int(birth[0 : 4]) <= 2000:
    print("20세기 사람입니다^^")
else:
    print("21세기 사람입니다^^")