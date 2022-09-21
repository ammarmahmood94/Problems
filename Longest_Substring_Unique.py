from itertools import count


var = str(input("Enter a word with repeating characters: "))

def split_characters(m):
    return m
    
def lengthofsubstring(p):
    
    m = []
    countkeep = []
    count = 0
    
    for i in p:
        count+=1
        if i not in m:
            m.append(i)
            countkeep.append(count-1)
    return countkeep
        
def new_func(countkeep):

    for i in range(len(countkeep)):
        if i < (len(countkeep) - 1):
            pass

m = map(split_characters, var)
p = list(m)
counter = lengthofsubstring(p)
print(counter)
new_func(counter)

