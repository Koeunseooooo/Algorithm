def solution(rows, columns, max_virus, queries):

    grid = [[0]*columns for _ in range(rows)]

    def action(i, j):
        stack = [(i, j)]
        visited = set([(i, j)])
        while stack:
            i, j = stack.pop()
            if grid[i][j] < max_virus:
                grid[i][j] += 1
            else:
                for _i, _j in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                    if 0 <= _i < rows and 0 <= _j < columns and (_i, _j) not in visited:
                        visited.add((_i, _j))
                        stack.append((_i, _j))

    for i, j in queries:
        action(i-1, j-1)

    return grid
