# 문제1) 사용자가 입력한 단수를 출력하는 코드
# dan = int(input("단수: "))
# for i in range(1, 10):
#     print(f"{dan}x{i}={dan*i}")

# 문제2) 2단부터 9단까지 출력(중첩 for문)
for i in range(2, 10): # 2~9단(i)
    for j in range(1,10): # 단수 내에 1~9까지
        print(f"{i}x{j}={i*j}")

# 문제3) list a 의 평균값을 계산하세요.
a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]
total = 0
for num in a:
    total += num # total = total + num
result = total / len(a)

# round(값, 자리수) : 자리수만큼 반올림
print(round(result, 2)) # 평균값

# 문제4) list b에서 최소값 찾기
b = [22, 1, 4, 7, 98]

print(num_min) # 1 출력
