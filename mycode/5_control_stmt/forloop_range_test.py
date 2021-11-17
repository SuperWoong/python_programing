"""
for loop lange
"""

my_list = [10,20,30,50]

for val in my_list:
    print(val)

for idx, val in enumerate(my_list,1):
    print(idx, val)

#값확인이 안되서 리스트로 싸줌
print (range(10))

print(list(range(10)))
for val in range(1, 10, 2):
    print(val)


import numpy as np

print(np.arange(10))

for val in np.arange(1, 10, 2):
    print(val)
