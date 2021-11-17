"""
연습문제

1. 현재년도 계산
from datatime import datetime as dt
 dt.today().year
2. 태어난 년도를 입력하라고 메시지 보내고 사용자 입력 기다림
3. 나이 = 현재년도 - 태어난 년도 + 1
4.
"""

"""
나이 = 현재년도 - 태어난녀도 + 1
태어난년도는 입력을 받습니다.
"""

from datetime import datetime as dt
from datetime import date

print(dt.today())
print(dt.today().year)
print(dt.today().month)

current_year = dt.today().year
print("태어난 년도를 입력하세요")
birth_year = int(input())
print(current_year, birth_year)
age = current_year - birth_year + 1

if 17 <= age < 20 :
    print('고등학생 입니다.')
elif 20 <= age <= 27:
    print('대학생 입니다.')
else:
    print('학생이 아닙니다.')






