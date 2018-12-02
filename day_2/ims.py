f = open("input.txt")
text = f.read().split()
f.close()

alpha = "abcdefghijklmnopqrstuvwxyz"

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
        
print(check(text))