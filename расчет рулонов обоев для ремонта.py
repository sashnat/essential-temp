# coded by Nataliya Sashnikova
# Расчет рулонов обоев
def s():
    a = float(input('высота участка: '))
    b = float(input('ширина участка: '))
    print ("целых кусков (полос) 1 рулона: ", math.floor(x/a))
    print ("всего нужно полос: ", math.ceil(b/y),b/y)
    z = math.ceil(math.ceil(b/y)/math.floor(x/a))
    print ("количество рулонов: ", z , "= количество полос: ", z*(x//a))
    p = z*math.floor(x/a)-math.ceil(b/y)
    print ("в резерве полос: ", p)
    q.append(z)
    spare.append(p)
    return z


import math
from functools import reduce
q = []
spare = []
x = float(input('высота (длина) рулона: '))
y = float(input('ширина рулона: '))
print(s(), "рулонов 1я площадь")
print(s(), "рулонов 2я площадь")
print(s(), "рулонов 3я площадь")
print(s(), "рулонов 4я площадь")
print(s(), "рулонов 5я площадь")

print(q)
print(spare)
print(reduce((lambda x, y: x + y), q))
