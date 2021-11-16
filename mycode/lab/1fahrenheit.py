




"""
섭씨온도를 입력 받아서 화씨로 변환하기
"""

#섭씨를 화씨로 변환하는 함수
def fah_convert(celsius):
   return ( (9/5) * float(celsius) ) + 32

print("변환하고 싶은 섭씨 온도를 입력하세요~!")
user_intput = input()
print(type(user_intput), user_intput )

fah = fah_convert(user_intput)

print('섭씨온도: ',float(user_intput))
print(f'섭씨온도: {user_intput}' )
print('화씨온도: ' + str(fah))
print('화씨온도: {0:.2f}'.format(fah))
print(f'화씨온도: {round(fah,2)}')







