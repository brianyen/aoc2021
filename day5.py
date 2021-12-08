lines = []
with open("dataset.txt") as f:
  lines = f.readlines() 

for line in lines:
  lines[lines.index(line)] = line[0:len(line)].split(" -> ")
for line in lines:
  for cord in line:
      lines[lines.index(line)][line.index(cord)] = cord.split(",")

map = []
for val in range(0, 1000):
    map.append([])
    for index in range(0, 1000):
        map[val].append(0)

def update(x, endX, y, endY):
    print(x, endX, ",", y, endY)
    while x <= endX:
        map[y][x] += 1
        x += 1
        if (y < endY):
             y += 1
        else:
            y -=1

for line in lines:
    fX = int(line[0][0])
    sX = int(line[1][0])
    fY = int(line[0][1])
    sY = int(line[1][1])
    if fX == sX:
        pos = fX
        rangeF = range(min(fY, sY), max(fY, sY)+1)
        for val in rangeF:
            map[val][pos] += 1
    elif fY == sY:
        pos = fY
        rangeF = range(min(fX, sX), max(fX, sX)+1)
        for val in rangeF:
            map[pos][val] += 1
    else:
        if (fX < sX):
            update(fX, sX, fY, sY)
        else:
            update(sX, fX, sY, fY)
    
sum = 0
for line in map:
    for val in line:
        if val >= 2:
            sum += 1
for line in map:
    print(line)
print("sum", sum)