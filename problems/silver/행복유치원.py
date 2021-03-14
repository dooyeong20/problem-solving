from sys import stdin

n, k = map(int, stdin.readline().split())
kids = list(map(int, stdin.readline().split()))

# kids의 차이 값
gaps = []

# kids들의 키 차이 값들을 구해서 저장함
for i in range(n-1):
    gaps.append(kids[i+1] - kids[i])

gaps.sort() # 키 차이 정렬

# 구한 차이 값들 중 큰 값부터 총 그룹수 - 1 만큼을 뺀 나머지 값들의 합이 정답이다.
# 왜냐하면 학생들의 키 차이의 값의 최솟값을 구하는 것이 목적이기 때문에, 큰 값(학생들 간의 차이가 큰 값)들을
# 최대한 제외해주어야 하고 그 값들은 키 총 그룹수 - 1 만큼이 되기 때문이다.
# 예를 들어서 키가 각각 1 3 4 10 11 인 아이들을 3그룹으로 나누고자 할 때,
# 키 차이의 값인 2 1 6 1 을 구해준 후, 이 값들 중에서 가장 큰 2(3 - 1)개의 수를 빼준 다음
# 나머지 값들의 합이 정답이다. (1 + 1 => 2) ----> (1) (3, 4) (10, 11)로 나누었을 때 
print(sum(gaps[:n - k]))