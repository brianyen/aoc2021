pos = []
possible = []

with open("dataset.txt") as f:

  for val in f.readline().split(","):
    pos.append(int(val))
mi = pos[0]
ma = pos[0]

for val in pos:
  mi = min(mi, val)
  ma = max(ma, val)

for val in range(mi, ma):
  sum = 0
  for p in pos:
    n = abs(val-p)
    sum += n * (n+1)/2
  possible.append(sum)

def run():
  minFuel = possible[0]
  for val in possible:
    minFuel = min(minFuel, val)
  print(minFuel)