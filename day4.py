import math

lines = []
with open('dataset.txt') as f:
    temp = f.readlines()
    for line in temp:
         lines.append(line[0:len(line)-1])

order = lines.pop(0).split(",")

cards = []
count = 0
for line in lines:
    if count % 6 == 0:
        count += 1
        cards.append([])
        continue
    cards[math.floor(count/6)].append(line)
    count += 1

def formatCards():
    cC = 0
    for card in cards:
        cR = 0
        for row in card:
            cards[cC][cR] = row.split()

            cR += 1
        cC += 1

def checkRows(array):
    for row in array:
        if all(val == " " for val in row):
            return True
    return False
        
def checkColumns(array):
    for index in range(5):
        if all(x[index] == " " for x in array ):
            return True   
    return False

def updateCard(array, target):
    cR = 0
    for row in array:
        cV = 0
        for val in row:
            if (val == target):
                array[cR][cV] = " "
            cV += 1
        cR += 1

def main():
    for n in order:
        count = 0
        while count < len(cards):
            card = cards[count]
            updateCard(card, n)
            if checkColumns(card) or checkRows(card):
                    if len(cards) == 1:
                        sum = 0
                        for row in card:
                            for val in row:
                                if val != " ":
                                    sum += int(val)
                        print(card)
                        print(sum * int(n))
                        return
                    cards.pop(count)
                    count -= 1
            count += 1

formatCards()
main()