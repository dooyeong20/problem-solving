from sys import stdin


def preorder(tree):
    s = ''

    def recursive(node):
        nonlocal s

        if node == '.':
            return

        s += node
        recursive(tree[node][0])
        recursive(tree[node][1])

    recursive('A')

    return s


def inorder(tree):
    s = ''

    def recursive(node):
        nonlocal s

        if node == '.':
            return

        recursive(tree[node][0])
        s += node
        recursive(tree[node][1])

    recursive('A')
    return s


def postorder(tree):
    s = ''

    def recursive(node):
        nonlocal s

        if node == '.':
            return

        recursive(tree[node][0])
        recursive(tree[node][1])
        s += node

    recursive('A')
    return s


def solution(n, treeDict):
    for _ in range(n):
        root, left, right = stdin.readline().split()
        treeDict[root] = [left, right]

    print(preorder(treeDict))
    print(inorder(treeDict))
    print(postorder(treeDict))


n = int(input())
treeDict = dict()
solution(n, treeDict)
