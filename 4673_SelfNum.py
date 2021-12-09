numbers = set(range(1,10001))
remove_set = set()

for num in numbers:
    for i in str(num):
        num += int(i)
    remove_set.add(num)

selfNum = numbers - remove_set
for j in sorted(selfNum):
    print(j)

