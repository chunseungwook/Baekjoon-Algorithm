import sys
N = int(sys.stdin.readline())
list_score = list(map(int,sys.stdin.readline().split()))
M = max(list_score)
list_calscore = []
calscore = 0
AvgScore = 0
3
for i in list_score:
    calscore=(i/M)*100
    list_calscore.append(calscore)
AvgScore = sum(list_calscore) / len(list_calscore)
print(AvgScore)
