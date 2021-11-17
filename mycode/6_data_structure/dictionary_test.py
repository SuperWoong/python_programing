"""
dictionary는 key : value 쌍으로 이루어진 데이터 저장하는 자료구조
"""
# class dict 선언 및 초기화
# 초기화 두가지 방법, 콜론으로 키와 값
my_dict = dict()
my_dict = {'name': '홍길동', 'age': 20}

#
print(type(my_dict))
#key로 value 조회
print(my_dict['name'])
#dict에 새로운 key와 value 추가
my_dict['addr']= '충주'

print(my_dict)

#print(my_dict['name1'])
result = my_dict.get('name1')
if result:
    print(result)
else:
    print('key does not exist')

result = my_dict.get('name')
if result:
    print(result)
else:
    print('key does not exist')

if "name1" in my_dict:
    print('name1 key가 있습니다.')
else:
    print('name1 key가 없습니다.')

if "name" in my_dict:
    print('name key가 있습니다.')
else:
    print('name key가 없습니다.')


for key, value in my_dict.items():
    print(key,value)





