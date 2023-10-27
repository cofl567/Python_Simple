# 주차타워
# 조건
# 1.1층~5층
# 2.층별로 1대만 주차
# 3.차량번호: 숫자4자리
# 기능
# 1.차량입고
# 2.차량출고
# 3.차량조회
# 4.프로그램 종료

# 설정
max_car = 5 # 최대 주차 5대
car_cnt = 0 # 현재 주차 대수(Count)

# 주차 타워 생성(List)
# ["", "", "", "", ""]
# tower = []
# for i in range(max_car):
#     tower.append("")

# * List Comprehension
tower = ["" for i in range(max_car)]

while True:
    print("="*50)
    print("== 주차 타워 시스템ver1.1 ==")
    print("="*50)
    print("1. 입고")
    print("2. 출고")
    print("3. 조회")
    print("4. 종료")
    print("="*50)

    while True:
        select_num = int(input(">>번호: "))
        if 4 > select_num >= 1:
            break
        else:
            print("MSG: 올바른 번호를 입력하세요.")

    if select_num == 1:
        pass
        # 주차타워 여유공간 Check
        if car_cnt < max_car:
            car_num = input(">>입고: ")
            for i, car in enumerate(tower):
                if car == "":
                    tower[i] = car_num
                    car_cnt += 1
                    break
        else:
            print("MSG: 만차입니다. 다음에 이용해주세요.")
        # 입고할 차량 번호 입력
        # 입고

    elif select_num == 2:
        # 1.출고 차량번호 입력
        car_num = input(">>출고: ")
        if car_num in tower:
            for i, car in enumerate(tower):
                if car == car_num:
                    tower[i] = "" # 차량 제거
                    car_cnt -= 1  # 현재 주차대수 동기화
                    break
        else:
            print("MSG: 해당 번호로 입고 된 차량이 없습니다.")
        # 2.tower == 출고 차량번호 match
        # 3-1 yes: 출고(tower 제거(""), car_cnt-1)
        # 3-2 no: MSG(입고 된 차량X)
    elif select_num == 3:
        print("== 주차 타워 현황 ==")
        for i in range(len(tower)-1, -1, -1):
            print(f" > {i+1}층 {tower[i]}")
    elif select_num == 4:
        print("MSG: 프로그램을 종료합니다.")
        exit()