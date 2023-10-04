# 제어문
# 1.조건문(if)
# 2.반복문(for, while)

# 반복문(Loop)
# - 반복적인 작업을 가능하게 해주는 도구
# - list, str, tuple 등 컬렉션 타입의 아이템을 하나씩
#   순회하면서 사용 가능(for)
# - 특정 조건을 만족하는 경우(while)

# 반복횟수 0 => for
# 반복횟수 X => while

# for문 기본문법(list 활용)
# for num in [1, 2, 3];
#    print(num)

# for(int i=0; i<=9; i++) {
#   print(i)
# }

# range() 함수
# - range(시작, 끝, 증감)
# - default 시작(0), 증감(+1)
# - range(3):           0, 1, 2
# - range(1, 10):       1, 2, 3, 4, 5, 6, 7, 8, 9
# - range(2, 5, 2):     2, 4

# range() 함수를 활용해서 1~9까지 출력하는 for문
for i in range(1, 10):
    print(i)

# List를 활용한 for문
temp = ["A", "B", "C", "D", "E"]
for alpha in temp:
    print(alpha)

# enumerate() 함수
# - 반복횟수(index) 정보를 사용하고 싶을 때
# - 0번부터 시작
for i, alpha in enumerate(temp):
    print(i+1, alpha)

# dict를 활용한 for문
#   - dict를 출력 => key값만 출력
#   - dict.keys(), dict.values(), dict.items()
temp = {"A": 1,
        "B": 2,
        "C": 3,
        "D": 4}
print("="*100)
for element in temp.values():
    print(element)

for key, value in temp.items(): # tuple(key, value)
        print(key) # key
        print(value) # value

# break: 즉시 반복문을 빠져 나가세요!
# a를 출력하다가 3을 만나면 멈추세요!
a = [1, 2, 3, 4, 5]
for i in a:
    if i == 3:
        break
    print(i)

# continue: 즉시 다음 반복으로 넘어가세요!
# 1~10까지 중 홀수만 출력!
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

    # 구구단 2단 코드
    # 2x1=2
    # 2x2=4
    # ...
    # 2x9=18
for i in range(1, 10):
    print(f"2x{i}={2*i}")


