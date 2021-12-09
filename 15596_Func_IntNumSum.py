"""def Sum_ListNum(list_Num):
    import sys
    list_Num = list(map(int,sys.stdin.readline().split()))
    sum = 0
    for i in list_Num:
        sum += i
    return sum
"""
def solve(a):
    #import sys
    #a = list(map(int,sys.stdin.readline().split()))
    ans = 0
    for i in a:
        ans += i
    return ans
b=[]
print(solve(b))