# 라이브러리(Library), 패키지(Package), 모듈(Module)
# - 라이브러리 >= 패키지 >= 모듈

# 1.라이브러리: 여러 패키지와 모듈의 묶음(Python_simple-main)
# 2.패키지: 특정 기능과 관련된 여러 모듈의 묶음(ex:lecture)
# 3.모듈: 이미 작성된 프로그램(일반적으로 한 파일(.py)을 의미)

# ** 모듈의 종류
# 1.내부 모듈: Python 내에서 제공하는 모듈
# 2.외부 모듈: 다른 개발자가 개발해 놓은 모듈
# 3.사용자 정의 모듈: 직접 개발해서 사용하는 모듈

# ** 모듈 사용 방법
#   - 라이브러리 또는 모듈을 사용하기 위해서는 "import" 필요!

# 가정: "requests" 라이브러리 안에는 1000개 모듈

# 1.import
#   ex) import requests
#   → "requests" 라이브러리 전체 호출(1000개)
#   → requests.get()

# 2.from ~ import
#   ex) from requests import get
#   → "requests" 라이브러리 내에서 "get" 모듈만 호출(1000개 중 1개)
#   → get()

# 3.as(Alias: 별명)
#   ex) import requests as req
#   → "requests" 라이브러리 전체 호출, 그리고 "req"라는 별명 붙이기
#   → requests.get() :1
#   → req.get() : 3