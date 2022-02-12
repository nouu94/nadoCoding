class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")


# 모듈 직접 실행
# if __name__ 정보를 활용하여 여러분들이 직접 모듈 내에서 실행하는건지,
# 혹은 외부에서 모듈을 가져다 쓰는건지 구분해서 필요한 코드를 작성할 수 있습니다.
if __name__ == "__main__":  # name이 main이라면...
    print("Thailand 모듈을 직접 실행한다.")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요.")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")

    # practice.py 파일에서 ThailandPackage를 갖다 쓸 때는 else 구문이 실행
    # thailand.py에서 직접 이 내용을 실행할 때는 if 구문을 사용 될 거에요.
