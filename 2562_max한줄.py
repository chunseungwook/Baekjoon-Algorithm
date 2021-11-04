import sys
list1 = list(int(sys.stdin.readline().strip()) for i in range(9))
max = max(list1)
print(max)
idx = list1.index(max(list1))
print(idx+1)
