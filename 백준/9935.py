# mirkovC4nizCC44
# C4

origin = input()
bomb = input()
stack = []
m = len(bomb)


for o in origin:
    stack.append(o)
    if len(stack) >= m:
        if "".join(stack[-m:]) == bomb:
            for _ in range(m):
                stack.pop()

if not stack:
    print("FRULA")
else:
    print("".join(stack))
