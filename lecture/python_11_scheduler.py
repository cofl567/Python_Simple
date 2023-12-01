# 스케줄러
# - 정해진 시간에 동작하도록 프로그램을 스케줄링
# 예) 5초마다 한번씩 동작
#       특정일(크리스마스)에만 동작
#       하루에 한 번 동작
import time

# apscheduler
# 1.blocking
# 2.background

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time
def print_now():
    print(datetime.now())

def print_love():
    print("I LOVE YOU")


# 1.스케줄러 생성
# scheduler = BlockingScheduler()
scheduler = BackgroundScheduler()
# 2.스케줄러 등록(일, 주기, 5초)
# - date: 특정일, 특정날짜에만 동작
# - interval: 주기별로(5초, 10분, 1시간)
# - CRON(*): 만능(매일 특정 시간에~)
scheduler.add_job(print_now, "interval", seconds=5)
scheduler.add_job(print_love, "cron", hour=13, minute=16)
# 3.스케줄러 실행
scheduler.start()

# 임의로 work
while True:
    time.sleep(1)
