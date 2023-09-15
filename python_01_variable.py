# 주석(comment): 메모, 실행X

# 1. 출력 함수(print)
# - ()안의 값을 출력
# - 변수값 확인용도로 많이 사용
print("=" * 200)
print("Hello Python")

# 문자열 타입(String Type)
# - Python: '' or "" -> string
# - C, Java: ''(char), ""(string)

# 참고: Escape Code
# - 문법: \(역 슬러쉬) + @
# - 문자열(String) 내의 일부 문자의 의미를 달리하여 특정한 효과 주기
# - 예 \n: 한 줄 개행, \t: 탭(8칸 공백)
print("=" * 200)
print("Hello \nPython")
print("Hello \tPython")

# 2.자료형(Type)
# - Python의 모든 자료형은 객체(Object)
# - JAVA 정수형: byte, short, int, long
# - Pyton 정수형: int
# 1) 문자열(String): "Hello", 'Hi'
# 2) 정수형(int): 3 -1, 0
# 3) 실수형(float): 3.14, 0.0, -2.2
# 4) 논리형(boolean): True, False

# 설명: 동일한 Type에서 다양한 종류의 자료형을 사용하는 이유?
# - 메모리(저장공간)를 효율적으로 사용하기 위해서!
# - 대부분 만들어진지 오래 된 언어는 다양한 종류의 자료형 사용!
# - 자료형은 저장 할 수 있는 크기의 범위가 지정
# - 가정: int(-10000~ 10000)
# - 가정: short(-100 ~ 100)
# - 특정 값: 0~9 -> 어떤 Type을 사용하면 효율적일까요? short

# 3.동적 타이핑 언어(Dynamic Typing Language)
# _ JAVA: int num = 4;
# - Python: num = 4(Type 지정 X)
# - 코드가 실행될 때 자동으로 Type을 지정
# - type() 함수: ()안의 값의 type을 확인할 때 사용
print("=" * 200)
print(type("ABC"))
print(type(3.14))
print(type(5))

# 4.형 변환(Type Casting)
# - Type Casting을 사용하면 값을 원하는 자료형으로 변환 가능
# - 1) int(): 정수형으로 변환
# - 2) float(): 실수형으로 변환
# - 3) str(): 문자열형으로 변환
print("=" * 200)
# "Hi: -> float(), int() 불가!
# 문자열 실수형: "3.14"    가능!
# 문자열 정수형: "5"       가능!
int_a = 3
float_b = 3.14
str_int_c = "9"
str_float_d = "9.2"

# 큰자료형 -> 작은 자료형으로 변환할 때 주의!
# 정수형(3) -> 실수형(3.0)
print(float(int_a))
# 정수형(3) -> 문자열("3")
# 실수형(3.14) -> 정수형(3) # 주의!(파일 손실 생김)
# 실수형(3.14) -> 문자열("3.14")
# 문자열 정수형("3") -> 정수형(3)
# 문자열 정수형("3") -> 실수형(3.0)
# 문자열 실수형("3.14") -> 정수형(Error)
# print(int(str_float_d))
# 문자열 실수형("3.14") -> 실수형(3.14)

# 5.None
# - 아무런 값을 갖지 않을 때 사용
# - 일반적으로 변수가 초기값을 갖지 않게 하고 생성할 때 사용
# - 기타 언어의 Null과 같은 의미로 사용
print("="*200)

# C, JAVA: 변수 생성 -> int num;
# Python: 변수 호출 -> num
# Python: 변수 생성 -> num = None
student_name = None   # 절대 사용 금지!
student_name = ""     # 적극 권장!

# "Null Pointer Exception"

# 기본 자료형(Primitive Type): 변수에 값이 그대로 저장
# - int num = 4;
# 객체 자료형(Reference Type): 변수에 값이 위치한 "주소"가 저장
# - string name = "10";

# - JAVA와 C: 기본, 객체 둘 다 사용
# - Python: 객체만 사용

# 6.변수(Variable)
# - 변수: 하나의 값을 저장할 수 있는 메모리 공간
print("="*200)
num = 4
num = 10
print(num) # 출력: 10 (기존 값 4 삭제)

# - 변수 생성 및 초기화
#   문법: num = 5(5를 num에다가 넣는다)
#   * num: "num" 변수 생성
#   * 대입연산자(=): 우측의 값을 좌측에 저장
#   * 동등연산자(==): Equal
#   * 초기화: 초기 변수를 생성하면 쓰레기 파일들이 존재
#            변수에 값을 대입하면 공간이 초기화 되고 값만 저장!

# name(변수명), =(대입연산자)
name = "cheery"

# 7. 명명규칙(Naming Rule)
# * 변수, 함수, 클래스 등의 사용자 정의 이름에 사용
# * 명확하고 알아보기 쉽게!!!
#
# 1. 영문 대소문자, 숫자, 특수문자(_)만 사용
# 2. 숫자로 시작할 수 없음
#    abc1(0), 1abc(x)
# 3. 영어 대소문자 구별
#     abc ABC Abc ABc abc 모두 다른 변수로 인식
# 4. 예약어 사용 불가
#    예약어: Python에서 미리 선점하여 사용중인 키워드
#        ex) print, for, while, if, else, class, and, return, import, def, pass, ...

# 8. Naming Method
#  - 변수, 함수, 클래스 등의 사용자 정의 이름에
#     사용하는 기법
#  - 프로그래밍 언어별로 사용하는 Naming Method가 다름

# 1.snake_case: 소문자만 사용, 합성어는 _사용
#   ex) chosun_student_name
# 2.camelCase: 첫글자 소문자, 합성어 첫글자 대문자
#   ex) chosunStudentName
# 3.PascalCase: 첫글자 대문자, 합성어 첫글자 대문자
#    ex) ChosunStudentName


#             변수            함수           클래스
# Java, C  camelCase      camelCase()    PascalCase
# Python   snake_case     snake_case()   PascalCase

# 9.동적 출력
print("="*200)
student_num = 20233148
student_name = "th"
# 출력 예: "조선대학교 20233148, th 입니다."
print("조선대학교 20233148, th 입니다.") # 하드 코딩 지양
# 1. format() - Old
print("조선대학교 {}, {} 입니다.".format(student_num, student_name))
# 2. f-string - New
print(f"조선대학교 {student_num}, {student_name} 입니다.")

# 10.간단한 사칙연산
# + : 더하기
# - : 빼기
# ** or ^ : 제곱 ex) 3^2
# 5/2 : 나누기        2.5
# 5%2 : 나누기(나머지) 1
# 5//2 : 나누기(몫)     2

# Quiz
num = 9
num - 1
num + 2
print(num)