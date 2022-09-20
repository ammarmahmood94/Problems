from itertools import count


var = str(input("Enter a word with repeating characters: "))

def split_characters(m):
    for i in m:
        return i
    
def lengthofsubstring(p):
    
    m = []
    countkeep = []
    count = 0
    
    for i in p:
        count+=1
        if i not in m:
            m.append(i)
            countkeep.append(count-1)
    return m, countkeep
        
def new_func(m, countkeep):
    
    new = []
    new.append(0)
    k=[]

    for i in range(len(countkeep)):
        if i < (len(countkeep) - 1):
            k.append(countkeep[i+1] - countkeep[i])
        

    # t = ""
    
    # for i in new:
    #     t+=p[i]
    
    # print(f"The longest substring is: {t} and its length is: {len(new)}")

m = map(split_characters, var)
p = list(m)
list, counter = lengthofsubstring(p)
new_func(list, counter)

