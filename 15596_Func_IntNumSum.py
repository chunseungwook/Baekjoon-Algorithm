def Sum_ListNum(list_Num):
    import sys
    list_Num = list(map(int,sys.stdin.readline().split()))
    sum = 0
    for i in list_Num:
        sum += i
    return sum
a=[]
print(Sum_ListNum(a))
# a list n 은 a의 종속 그리고 합