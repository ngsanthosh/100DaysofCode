#Python SPECIFICS

a="TUE"
b=19
day=["MON","TUE","WED","THU","FRI","SAT","SUN"]
# find=b%8
# # print(day.index(a))
# print(day[((day.index(a)+1)+find)-1])
i=day.index(a)

check=b%7

final=i+check-1
# print(final)

print(day[final%7])