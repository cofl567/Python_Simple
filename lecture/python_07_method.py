# 함수(method, function)
#   - 어떤 일을 수행하는 코드 묶음
#   - 반복적으로 동작해야하는 일들!

# ex) 회사원 -> 매일 아침마다 보고서 작성(15줄 코드 작성)
#     15줄 코드 -> 함수로 정의(1회) -> 매일 함수호출

# ** 함수 개발 가이드라인 **
# 1.함수 이름 및 내용
#   + 함수 이름에 함수의 역할과 의도 명확히 드러낼것!
#   + 함수 내용은 가능하면 짧게 작성(Code Line 줄이기)
#   ex) def print_hello():
#           print("Hello")

# 2.함수의 역할
#   + 하나의 함수에 유사한 역할을 하는 코드만 포함
#   + 하나의 함수는 한가지 기능만 명확히 정의
#   ex) def add_value(x, y):
#           return x+y

#   3.함수를 만들어야 하는 경우
#   + 공통적으로 사용되는 코드는 함수로 생성
#   + 복잡한 로직이 사용되는 경우 식별 가능한 이름의 함수 생성

# ** 함수의 종류 **
# 1.내장함수(Built-in function)
#   + python에서 내부적으로 기본적으로 제공하는 함수
#   ex) print(), len() type(), format(), list(0, tuple)
# print("Hello")
# 2.외장함수(Library or Module)
#   + Library: 다른 사람이 개발한 코드 묶음
#   + import문을 통해서 라이브러리 모듈 제공
#   ex) import pandas as pd
#       df_data = pd.read_excel("path")
#
# 3.사용자 정의 함수
#   + 개발자가 직접 만들어서 사용하는 함수

# ** 함수 이름 규칙 **
# - snake_case 사용

# ** 함수 정의 **
# 1.기본 함수 문법
# def 함수명(parameter1, parameter2, ...):
#     실행문
#     return 반환값
# 2.함수 정의시 "def" 키워드 사용(define)
# 3.인자(argument of parameter) 정의: 함수 입력값
# 4.return: 함수 종료 의미
# 5.return 반환값: 함수종료+호출문으로 반환값 전달(tuple)
# 6.함수 종료: 1.return, 2.들여쓰기 끝
# 7.parameter와 return은 생략가능
#   (입력과 반환이 없는 함수도 존재)


# ** 함수 실습 **
#  1.함수 정의
def sum_two_value(x, y):
    n = x + y
    print(n)
    return n


# 2.함수 호출
result = sum_two_value(5, 10)
print(result)

# 3.인자(Parameter or argument)
#   - 함수에 전달되는 입력값(input)
#   - 함수 정의문과 호출문의 parameter 갯수가 동일해야함
#   - parameter로 int, str, float, bool, list 등 사용 가능
#   - 심지어 사용자 정의 함수를 parameter로 전달 가능
#   - parameter값 2개 이상 사용시 정의 된 순서대로 전달해야함


def sub_two_value(x: int, y: int):
    n = x-y
    return n
a, b = 15, 20
num = sub_two_value(a, b)
print(num)

# 4.Default Parameter
# - 함수 호출시 parameter를 전달 받지 못한 경우 기본값 사용
# def test(a, b, c=3):      # (0)
# def test(a, b=2, c=3):    # (0)
# def test(a=1, b=2, c=3):  # (0)
# def test(a=1, b, c):      # (x)
# def test(a, b=2, c):      # (x)
# def test(a=1, b=2, c):    # (x)

# 5.return
# - 기본적으로 함수 종료 의미
# - return 반환값: 함수호출문으로 값 전달(tuple type)
# - return만 사용하면 함수호출문을 None값 전달
# - return이 없는 경우 들여쓰기 종료 함수 종료로 간주
# - return문 다음에 오는 코드는 실행 안됨(Error X)
def soju_yn(age):
    if age >= 20:
        return 1 # 구매 가능
    else:
        return 0 # 구매 불가

age = int(input("나이: "))
result = soju_yn(age)
if result == 1:
    print("주류 구매 가능")
elif result == 0:
    print("주류 구매 불가")

# 6.변수의 범위
#   - 변수가 참조 가능한 코드상의 범위를 명시
#   - 함수내의 변수는 자신이 속한 코드 블록이 종료되면 소멸
#   - 이렇게 특정 코드블록에서 선언된 변수를 지역변수
#   - 반대로 가장 상단에 정의되어 프로그램 종료 전까지
#     유지되는 변수를 전역변수
#   - 같은 이름의 지역변수와 전연변수 존재하는 경우
#     가까운(지역변수) 우선순위가 높음
num1 = 10 # 전역
num2 = 20 # 전역

def test(num1, num2):
    print(num1, num2)
    return
test(30, 40)
print(num1, num2)

# *함수 내에서 함수밖의 전역변수를 변경하고 싶은 경우
# 1.return 반환값
a = 1
print(a)
def vartest(a):
    a = a+1
    return a
a = vartest(3)
print(a)

# 2. global 키워드(절대 사용 금지)
a = 1
print(a)

def vartest():
    global a
    a = a+1
vartest()
print(a)

# 7.Variable length parameter(가변길이인자)
#   - 전달되는 parameter의 개수가 고정적이지 않은 경우
#   - print(), format()
#   ex) print("Hi"), print("Hi", "Hello")

#   1) *args: tuple type
def test(*args):
    for item in args:
        print(item)
test(10, 20, 30)

#   2) **kwargs: dict type
def test2(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
test2(a=1, b=2, c=3