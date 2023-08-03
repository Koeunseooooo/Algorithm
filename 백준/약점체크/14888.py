import sys
from itertools import permutations

input = sys.stdin.readline
N= int(input())
nums=list(map(int,input().split()))
operators_input=list(map(int,input().split()))
op_list=['+','-','*','/']
op=[]

for i in range(4):
    for _ in range(operators_input[i]):
        op.append(op_list[i])

max_num = -1e9
min_num = 1e9

def calculator(nums, operators):
    res = nums[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            res += nums[i + 1]
        elif operators[i] == "-":
            res -= nums[i + 1]
        elif operators[i] == "*":
            res *= nums[i + 1]
        else:
            if res >= 0:
                res //= nums[i + 1]
            else:
                res = -res // nums[i + 1]
                res = -res
    return res


for combi in permutations(op):
    new_num = calculator(nums, combi)
    max_num = max([new_num, max_num])
    min_num = min([new_num, min_num])
print(max_num)
print(min_num)
        
        
    

'''백트래킹(dfs) - Python3 통과, PyPy3도 통과
import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)
'''