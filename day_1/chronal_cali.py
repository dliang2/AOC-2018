f = open("input.txt")
text = f.read().split()
f.close()

def listSums(text):
    result = 0
    l = [0]
    for num in text:
        result = result + int(num)
        l.append(result)
    return l

def find(text):
    result = 0
    l = [0]
    while True:
        for num in text:
            result += int(num)
            if result in l:
                return result
            else:
                l.append(result)
            
print(find(text))