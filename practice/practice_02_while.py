# 문제1) 로그인(pw) -> 3번 이상 암호를 틀리면 프로그램 종료!
# pw = 1234
#
# count = 0 # 틀린 횟수
# while True:
#     if count >= 3:
#         print("종료: 암호를 3회이상 틀리셨습니다.")
#         break
#     input_pw = int(input("암호: "))
#
#     if pw == input_pw:
#         print("반갑습니다.")
#         break
#     else:
#         print("경고: 올바른 암호를 입력해주세요.")
#         count += 1

# 문제2) 1~100까지 더해서 총합을 계산하세요.
# - for문
total = 0
for x in range(1, 101):
     total += x
print(f"총합(for): {total}")

# - while문
total = 0
x = 0
while True:
    x += 1
    if x >= 101:
        break
    total += x
print(f"총합(while): {total}")
