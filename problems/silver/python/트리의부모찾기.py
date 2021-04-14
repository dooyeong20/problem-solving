from sys import stdin, setrecursionlimit

setrecursionlimit(1000000)


def solution(n, treeInfo):
    def find_parent(node):
        linked = node_dict[node]

        for l in linked:
            if l in used:
                continue

            used.add(l)
            parent[l] = node
            find_parent(l)

    node_dict = {key: [] for key in range(1, n+1)}
    parent = {1: 1}
    used = {1}
    ans = []

    for (n1, n2) in treeInfo:
        node_dict[n1].append(n2)
        node_dict[n2].append(n1)

    find_parent(1)
    for i in range(2, n+1):
        ans.append(str(parent[i]))

    return ans


n = int(input())
treeInfo = [list(map(int, stdin.readline().split())) for _ in range(n-1)]
print('\n'.join(solution(n, treeInfo)))
