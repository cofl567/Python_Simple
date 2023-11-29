# 스케줄러
# - 정해진 시간에 동작하도록 프로그램을 스케줄링
# 예) 5초마다 한번씩 동작
#       특정일(크리스마스)에만 동작
#       하루에 한 번 동작

# apscheduler
# 1.blocking
# 2.background

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
def print_now():
    print(datetime.now())
# 1.스케줄러 생성
scheduler = BlockingScheduler()
# 2.스케줄러 등록(일, 주기, 5초)
scheduler.add_job(print_now, "interval", seconds=5)
# 3.스케줄러 실행
scheduler.start()
