
#from bmi_clac import print_bmi

import mycode.lab.bmi_clac as bmi_clac

def main():
    print("이름을 입력하세요")
    name = input()

    print("키(cm)를 입력해세요")
    height_cm = int(input())

    print("몸무게를 입력하세요")
    weight = int(input())

    bmi_clac.print_bmi(name, height_cm, weight)

print(__name__)
if __name__ == "__main__":
    main()
#print_bmi(name, height_cm, weight)