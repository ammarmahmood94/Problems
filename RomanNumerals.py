var = str(input("Enter a roman numeral: "))

Roman_Numericals = {"I":1,
"V":5,
"X":10,
"L":50,
} 

def ConvertNumericalToInteger(n):
    i = Roman_Numericals[n]
    return i
    
def CalculateValue(l):
    if l.count(1) == 1:
        m = sum(l) - 2
        print(m)
    else:
        m = sum(l)
        print(m)

m = map(ConvertNumericalToInteger, var)
p = list(m)
CalculateValue(p)







