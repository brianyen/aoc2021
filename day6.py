lines = []
fish = [0,0,0,0,0,0,0,0,0]


with open("dataset.txt") as f:
  lines = f.readline().split(",") 

index = 0
for val in lines:
  fish[int(val)] += 1

for val in range(0, 256):
    temp = fish.pop(0)
    fish.append(temp)
    fish[6] += temp
    
print(sum(fish))