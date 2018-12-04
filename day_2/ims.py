f = open("input.txt")
text = f.read().split()
f.close()

alpha = "abcdefghijklmnopqrstuvwxyz"

text1 = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
# part 1
def check(input):
    d = {"twice": 0, "thrice": 0}
    for id in input:
        for letter in alpha:
            if id.count(letter) == 2:
                d["twice"] += 1
                break
        for letter in alpha: 
            if id.count(letter) == 3:
                d["thrice"] += 1
                break
    return d

# part 2
def common(input):
    for i in input:
        for j in input:
            forgive = 0
            index = 0
            while index < len(i):
                if i[index] != j[index]:
                    forgive += 1
                index += 1
            if forgive == 1:
                return (i, j)
            
        
        
    
    
print(common(text))
        
