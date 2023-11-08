# 다음 실시간 뉴스 목록(15개) 기사 [제목, 본문, 날짜] 수집기

import requests
from bs4 import BeautifulSoup
from service.service_news import get_news

count = 0 # 수집 된 전체기사 수
page = 1 # 시작 페이지 1로 고정
while True:
    url = f"https://news.daum.net/breakingnews/digital?page={page}"
    result = requests.get(url)

    if result.status_code == 200:
        print("URl 접속 성공 -> 데이터를 수집합니다.")
        doc = BeautifulSoup(result.text, "html.parser")
        url_list = doc.select("ul.list_news2 a.link_txt")


        if len(url_list) == 0:
            break

        for url in url_list:
             count += 1
             print(f"{count}", "="*150)
             get_news(url["href"])
    else:
        print("잘못된 URL 경로입니다. 다시 한 번 확인해주세요.")
    page += 1