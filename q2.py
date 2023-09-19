h = int(input("Enter side length: "))
l = [[""]*h for _ in range(h)]
x = 0
y = 0
n = 1
dir = [[0,1], [1,0], [0,-1],[-1,0]]
dnum = 0
while n <= (h*h):
    l[x][y] = n
    n += 1
    try:
        if ((x + dir[dnum][0]) > h or (y + dir[dnum][1]) > h or l[x + dir[dnum][0]][y + dir[dnum][1]] != "" ):
            dnum += 1
            dnum = dnum % 4
    except IndexError:
        dnum += 1
        dnum = dnum % 4

    x = x + dir[dnum][0]
    y = y + dir[dnum][1]

for z in range(h):
    for c in range(h):
        print(l[z][c], end = " ")
    print("")

