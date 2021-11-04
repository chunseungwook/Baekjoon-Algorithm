import sys
list1 = list(int(sys.stdin.readline().strip()) for i in range(9))
print(max(list1))
print(list1.index(max(list1))+1)
