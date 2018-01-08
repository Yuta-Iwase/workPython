import random

y=0
x=0
d=0.2

r = random.random()
if 0 <= r < 0.25:
# move north
    y=y+d
elif 0.25 <= r < 0.5:
# move east
    x=x+d
elif 0.5 <= r < 0.75:
# move south
    y=y-d
else:
# move west
    x=x-d

    xyz = 8


print ("x",x)
print ("y",y)