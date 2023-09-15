# 문자열의 이해(String)
#  활용 예: 데이터 분석, 자연어 처리 응용,
#           사용자로부터 값 입력받을 때 처리용도
#

# 1.문자열 인덱스(index)
# -  문자열은 각 문자마다 순서(인덱스)가 있음
# -  첫번째 문자부터 마지막 문자까지 순차적으로 인덱스
# -  인덱스 시작은 0
# -  인덱스는 공백 포함
print("="*100)
print("python")

# 2.문자 추출
# - 인덱스를 통해서 문자 추출
# - 인덱스 범위 벗어난 경우 오류
#   (Error: index out of range)
lang = "Python"
print(lang[0])
print(lang[2])
# print(lang[9] # Error

# -1 인덱스(Reverse Index)
# - 우측에서 좌측으로 인덱스
# - 시작값 -1

# 3.문자열 슬라이싱
#  - lang[3]: 문자 1개만 추출
#  - 부분 문자열 추출하고 싶은 경우
#  - 시작인덱스, 끝인덱스 필요
msg = "Python is all you need"
print(msg[0:6])  # 끝인덱스 +1
print(msg[:6])   # 시작 인덱스 생략 -> 자동 0입력
print(msg[3:])   # 끝 인덱스 생략 -> 자동 -1 입력
print(msg[:])    # 처음부터 끝까지

print(msg[18:])
print(msg[-4:])


# Quiz
# msg에서 "need"만 추출
# 정방향
# 역방향