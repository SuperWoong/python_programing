
"""
BMI
"""
print("이름을 입력하세요")
name = input()

print("키(cm)를 입력해세요")
height_cm = int(input())


print("몸무게를 입력하세요")
weight = int(input())



bmi = weight / (height_m ** 2)

print(f'{name}님의 BMI 수치는 {bmi:.1f} 입니다.')



#print(name, height_cm, height_m)