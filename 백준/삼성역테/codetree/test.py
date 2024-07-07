closestX = 10
closestY = 10
rudolf = (5, 5)

currentBest = (
    (closestX - rudolf[0]) ** 2 + (closestY - rudolf[1]) ** 2,
    (-closestX, -closestY),
)

print(currentBest)

currentValue = (40, (-10, -10))

print(currentBest < currentValue)
