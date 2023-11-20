# 4                          // N = 4, 테스트 케이스 #1
# 5 3 4 3
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)
    visited = [0] * (n)
    price = 0

    def dfs(visited):
        global n, arr, price
        if visited.count(1) == n:
            return price
        purchase = 0
        for i in range(n):
            if visited[i] == 0 and not purchase:
                price += arr[i]  # 방문 안했다면 일단 삼
                purchase = arr[i]
                visited[i] = 1
            elif visited[i] == 0:
                if arr[i] < purchase:
                    visited[i] = 1
                    break
        dfs(visited)

    dfs(visited)
    print("#{} {}".format(test_case, price))
