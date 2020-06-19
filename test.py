import math
import operator

scores=[5,8,6,3,100]
w=['abc','def','ghi','jkl','mno']
p = sorted(enumerate(scores), key=operator.itemgetter(1), reverse=True)
print(p)
z = [(str(w[i]), y, p[0][1] - y) for i, y in p]
print(z)
result = [(w[index], value) for (index, value) in enumerate(scores)]
print(result)
p = max(result,  key=operator.itemgetter(1))
print(p[0])