import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().strip().split())) for _ in range(n)]


dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
