from matplotlib import pyplot as plt
"""
plt.plot([1, 2, 3], [110, 130, 120])
plt.show()
plt.savefig("pythontest.png")
"""
"""
plt.plot(["Seoul", "Paris", "seattle"], [30, 25, 55])
plt.xlabel("City")
plt.ylabel("Response")
plt.title("Experiment Result")
plt.show()
"""
"""
plt.plot([1, 2, 3], [1, 4, 9])
plt.plot([2, 3, 4], [5, 6, 7])
plt.xlabel("Sequence")
plt.ylabel("Time(secs)")
plt.title("Experiment Result")
plt.legend(["Mouse", "cat"])
plt.show()
"""
"""
y = [5, 3, 7, 10, 9, 5, 3.5, 8]
x = range(len(y))
plt.bar(x, y, width = 0.7, color = "black")
plt.show()
"""
"""
scores = [45, 37, 18]
team = ["A", "B", "C"]
colors = ["yellowgreen", "skyblue", "lightgray"]
plt.pie(scores, labels = team, colors = colors, autopct = "%1.2f%%", startangle = 270)
plt.title("pie chart")
#plt.show()
plt.savefig("C:\\Users\\User\\Desktop\\python\\pieChart1.png")
"""

jobRate = [43955, 42337, 39803, 29824, 26636, 25588, 23973, 20112, 19555, 19336, 18842, 16264, 16176, 14791, 13872, 12242, 12062, 11409, 6561, 6277]
job = ["리퍼", "건슬링어", "바드", "인파이터", "워로드", "서머너", "스트라이커", "홀리나이트", "버서커", "블레이드", "스카우터", "디스트로이어", "창술사", "배틀마스터", "아르카나", "데모닉", "블래스터", "기공사", "호크아이", "데빌헌터"]
colors = ["black", "skyblue", "lightgreen", "green", "aliceblue", "chartreuse", "greenyellow", "gold", "goldenrod", "indianred", "lightcoral", "hotpink", "lightpink", "magenta", "mediumorchid", "mediumpurple", "mediumslateblue", "royalblue", "powderblue", "turquoise"]
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["font.size"] = 12
plt.rcParams["figure.figsize"] = (12, 8)
job.reverse()
jobRate.reverse()

plt.barh(job, jobRate, label = "로스트아크 직업 분포도")
plt.legend()
plt.xlim(1000, 50000)
plt.title("로스트아크 직업 분포도")
plt.yticks(job)

for i, v in enumerate(job):
    str_val = "%d명" % jobRate[i]
    plt.text(jobRate[i], v, str_val, fontsize = 9, color = colors[i], horizontalalignment = "left", verticalalignment = "center")
plt.show()
#plt.savefig("lostark.png")