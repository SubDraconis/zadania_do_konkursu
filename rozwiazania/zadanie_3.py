x, y = 0, 0

for i in input():
    if i == "G":
        y+=1
    elif i == "D":
        y-=1
    elif i == "P":
        x+=1
    elif i == "L":
        x-=1
print(x,y)