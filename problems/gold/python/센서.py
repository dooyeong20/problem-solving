from sys import stdin

n = int(stdin.readline())
k = int(stdin.readline())
sensors = sorted(list(map(int, stdin.readline().split())))


# 센서 사이의 거리를 구해서 gaps 리스트에 저장해준 후, 정렬해준다.
gaps = []
for i in range(n-1):
    gaps.append(sensors[i+1] - sensors[i])

gaps.sort()

# 센서 사이의 거리가 클 경우 집중국을 나누는 것이 효율적이기 때문에(그리디)
# 집중국의 개수 만큼 구간을 나누어 줄 수 있기 때문에 집중국의 개수 - 1 만큼
# 큰 거리를 0으로 만들어 구간의 합을 최소화 해준다.
for _ in range(k-1):
    if not gaps:
        break
    gaps.pop()

print(sum(gaps))


'''
[풀이]

먼저, 각 센서를 정렬한 후에 센서간의 거리의 차를 gaps 라는 리스트에 저장해준다.
그리고, 그 센서 사이의 차가 클 때 비용이 커지기 때문에 gaps의 가장 큰 값부터
집중국의 개수 - 1 (집중국의 개수만큼 구간을 나눌 수 있기 때문에) 만큼 gaps 리스트에서
pop()을 통해 큰 값을 제거해준다.

그리고 이후에 gaps 리스트에 남은 값들을 모두 더해주면 집중국 배치 후 센서사이 
거리 값의 최소값을 구할 수 있다. 
'''