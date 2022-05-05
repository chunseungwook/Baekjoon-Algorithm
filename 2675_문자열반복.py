#2675_문자열 반복하기
#input : 문자열 
#output : 반복된 문자열

import sys
from timeit import repeat

Num = int(sys.stdin.readline())
list_value = list(str(sys.stdin.readline().strip()) for i in range(Num))

list_repeatNum = []
list_repeatStr = []

for value in list_value:
    list_repeatNum.append(value[:1])
    list_repeatStr.append(value[2:])

list_int_repeatNum = list(map(int, list_repeatNum))
#1 대 1 대응이 될수 있어야함.
#list_Repeatstr을 낱개 분리 필요
for repeatStr in list_repeatStr:
    repeatStr[0]*list_int_repeatNum[0] + repeatStr[1]*list_int_repeatNum[0] .....
list_repeatStr[0]*list_int_repeatNum[0] 의 반복

# repeatNum = []
# repeatStr = []

# for num in list_Num:
#     repeatStr.append(num[2:])
#     repeatNum.append(num[:1])

# repeatNum = list(map(int,repeatNum))
# result = []
# print(repeatNum)

# # 너무 어렵다 ㅠㅠ 꺄올
# for j in repeatStr:
#     for m in range(0, len(j)):
#         print(j[m]*repeatNum[m], end ="")
        
#     print(end = "\n")

# print(result)

#print(repeatNum)
#print(repeatStr)
#print(type(repeatNum[0]))"""
#print(type(list_N))
# list 로 구하기 너무 어렵습니다 ㅠㅠㅠㅠ


