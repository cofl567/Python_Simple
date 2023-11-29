from collect.collect_daum_movie_review import review_collector
def main():
    print("="*100)
    print("== 영화 리뷰 수집기 ==")
    print("="*100)
    movie_code = input("영화 코드>> ") # 169328
    print("MSG: 매일 12시간에 수집")
    review_collector(movie_code)

if __name__ == "__main__":
    main()
