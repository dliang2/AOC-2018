l = [[0 for r in range(1000)] for c in range(1000)]

#for id in text:

src = open("input.txt")
data = src.read().strip().split("\n")
newdata = [s.replace("#", " ").replace("@", " ").replace(",", " ").replace(":", " ").replace("x", " ") for s in data]
newdata = [ [int(x) for x in s.split()] for s in newdata]

#print(newdata)

for item in newdata:
    row = item[1]
    endrow = row + item[3]
    col = item[2]
    endcol = col + item[4]
    for r in range(row,endrow):
        for c in range(col,endcol):
            l[r][c] += 1


count = 0
for r in range(1000):
    for c in range(1000):
        if l[r][c] > 1:
            count += 1
        
#print(count)

for item in newdata:
    row = item[1]
    endrow = row + item[3]
    col = item[2]
    endcol = col + item[4]
    b = True
    for r in range(row,endrow):
        for c in range(col,endcol):
            if l[r][c] != 1:
                b = False
    if b:
        print(item[0])
                
