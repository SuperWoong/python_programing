
"""
리스트 튜플
"""
# packing
my_list1 = [20, 30, 40, 50]
print(my_list1)
my_list1.remove(30)
print(my_list1)
#my_list1 = del my_list1[2]

# unpacking
n1, n2, n3 = my_list1

print(n1, n2, n3)

my_list2 = list()

my_list1.append(10)
print(my_list1)

my_list1.extend([50,60])
print(my_list1)

my_list1.insert(0,10)
print(my_list1)

my_list1[2] = 100
print(my_list1)
print(my_list1[0:3])



"""
set  중복허용 안함, 순서가 유지안됨
"""
my_set = set(my_list1)
print(type(my_set))
print(my_set)

"""
tuple 한번 값 넣으면 수정 불가 (read only), 속도는 빠름
"""
my_tuple =(10, 20, 30)
my_tuple2 = tuple()
print(type(my_tuple))
print(my_tuple)
#TypeError: 'tuple' object does not support item assignment
#my_tuple[0] = 50

num1 = (3)
num2 = (3,)
print(type(num1), type(num2))

#tuple usage 리드온리 함수리턴 타입으로 사용됨
def swap(a,b):
    return (b,a)

n1, n2 = swap(10, 20)
print(n1, n2)

cat_list = list('cat')
print(cat_list)

birth_day =  "1982/07/07"
birth_list = birth_day.split("/")
print(birth_list)

print('1982' in birth_list)
print('1982' not in birth_list)

if '1982' not in birth_list:
     print('not found')



"""
연습문제

1. 현재년도 계산
from datatime import datetime as dt 
 dt.today().year
2. 태어난 년도를 입력하라고 메시지 보내고 사용자 입력 기다림
3. 나이 = 현재년도 - 태어난 년도 + 1
4. 
"""




