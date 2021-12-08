import copy
def findVal(ind):
    lines = []

    with open('dataset.txt') as f:
        temp = f.readlines()
        for line in temp:
            lines.append(line[0:12])

    result = copy.deepcopy(lines)

    def findCommon(list, index):
        count0 = 0
        count1 = 0
        for val in list:
            if val[index] == "0":
                count0 += 1
            else:
                count1 += 1
        
        if (count1 >= count0):
            return ["1", "0"]
        return ["0", "1"]
        # common first

    for i in range(0, 12):
        arr = findCommon(result, i)
        for el in lines:
            if (el[i] == arr[ind]):
                try: 
                    index = result.index(el)
                except ValueError:
                    continue
                if (len(result) > 1):
                   result.pop(index)

    print(result, result[0])
    return result[0]

oxy = findVal(1)
co2 = findVal(0)
sumO = 0
sumC = 0
for i in range(0, 12):
    if (oxy[11-i] == "1"):
        sumO += 2 ** i
    if (co2[11-i] == "1"):
        sumC += 2 ** i

print(sumO * sumC)