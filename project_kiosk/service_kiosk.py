# 키오스크 기능은...

# 사용자 메뉴 선택
# - max_cnt: 메뉴별 갯수
# - menu_type: main or sub

def user_choice(max_cnt, menu_type=""):
    while True:
        choice = int(input(">> 번호: "))
        if choice == 99 and menu_type == "main":
            return choice
        if max_cnt >= choice >= 1:
            return choice
        else:
            print("MSG: 올바른 번호를 입력하세요.")