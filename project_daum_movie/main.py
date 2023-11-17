# SELENIUM

# pip install selenium
# pip install webdriver_manager

# ** Selenium을 사용하는 이유?
# - Requests는 현재 URL의 정적 페이지 소스코드만 수집 가능
#   -> "더보기" 버튼 클릭과 같이 동적인 동작 불가!
# - Selenium은 전용 브라우저를 사용해서 동작
#   -> 따라서 chrome 드라이버와 같이 브라우저 설정 반드시 필요!
#   ※ Selenium은 처음에 웹 브라우저 테스트 용으로 개발

from datetime import datetime, timedelta
import math
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 1.Selenium 전용 웹 브라우저 구동
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 2.URL 접속
url = "https://movie.daum.net/moviedb/grade?movieId=169137"
driver.get(url)
time.sleep(2)

# 3.페이지 전체 코드 가져오기
doc_html = driver.page_source

# 4.Selenium -> BeautifulSoup
doc = BeautifulSoup(doc_html, "html.parser")

# 5. 영화 제목 수집
movie_title = doc.select("span.txt_tit")[0].get_text()
print("="* 100)
print(f"영화 제목: {movie_title}")
print("="* 100)

# 6.전체 리뷰 출력("평점 더보기" 클릭)
#   - 다음 영화 최초 페이지 -> 10개
#   - "평점 더보기" 클릭 -> 30개
# ? "평점 더보기" 몇 번 클릭? -> 전체 리뷰 출력

# ex) 전체 리뷰: 187개
# 수식: 올림((187 - 10) / 30)

# 6-1. 전체 리뷰 수집
total_review_cnt = doc. select("span.txt_netizen")[0].get_text()

# 6-2. 전체 리뷰에서 숫자만 추출
# - 문자열 슬라이싱
# 예) (187명)
# print(total_review_cnt[1:-2])
# - 정규식 -> 숫자만 추출
num_review = int(re.sub(r"[^~0-9]", "", total_review_cnt))

# 6-3. "평점 더보기" 클릭 횟수 계산(모든 리뷰 출력)
click_cnt = math.ceil((num_review - 10) / 30)

# 7.Selenium을 통해서 "평점 더보기" 클릭
for i in range(click_cnt):
    # "평점 더보기" 클릭
    driver.find_element(By.CLASS_NAME, "link_fold").click()
    time.sleep(1)

# 8.전체 소스코드 가져오기
doc_html = driver.page_source
doc = BeautifulSoup(doc_html, "html.parser")
review_list = doc.select("ul.list_comment > li")
print(f"= 전체 리뷰: {len(review_list)}건")

 # item: 리뷰 1건(평점, 리뷰, 작성자, 작성일자)
for item in review_list:
    print("=" * 100)
    review_score = item.select("div.ratings")[0].get_text()
    print(f"  - 평점: {review_score}")
    review_content = item.select("p.desc_txt")[0].get_text().strip()
    # \n : 한 줄 개행 -> \n을 제거
    re.sub("\n", "", review_content)
    print(f"  - 리뷰: {review_content}")

    review_writer = item.select("a.link_nick > span")[1].get_text() # [댓글 작성자, 작성자, 댓글 모아보기]
    print(f"  - 작성자: {review_writer}")

    review_date = item.select("span.txt_date")[0].get_text()
    # 24시간 이내에 작성 된 리뷰의 날짜 -> 24시간전, 3시간전 -> 다음영화날짜(2023. 11. 17. 2:12)
    # 1. 24시간전, 17시간전과 같은 날짜 찾기
    if len(review_date) < 7:
        # 2) "17시간" -> 숫자만 추출 17
        reg_hour =int(re.sub(r"[^~0-9]", "", review_date))
        # 3) 등록일자 = 현재시간 - 17
        # print(f"현재시간: {datetime.now()}") # 년월일시분초나노초
        review_date = datetime.now() - timedelta(hours=reg_hour)
        # print(f"등록시간: {review_date}")
        # 4) 계산된 등록일자 날짜 포맷 변경(다음 영화 리뷰 날짜 포맷)
        review_date = review_date.strftime("%Y. %m. %d. %H:%M")
    print(f"  - 날짜: {review_date}")
