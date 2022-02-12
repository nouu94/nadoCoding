'''
이런 식으로 필요한 것들 끼리 부품처럼 만드는 것을 module화 라고 하고
파이썬은 함수 정의나 클래스를 담고 있는 파일을 module이라고 해요. 확장자 .py
'''

# 예를 들어 극장이 있다. 극장에서는 희안하게 현금만 받아요.
# 잔돈을 안바꿔준다고 합니다. 영화 티켓이 35,000; 40,000이면 거스름돈 안줌 ㅋ

# 일반 가격


def price(people):
    print("{0}명 가격은 {1}원 입니다." .format(people, people * 10000))

# 조조 가격


def earlyPrice(people):
    print("조조할인 {0}명 가격은 {1}원 입니다." .format(people, people * 6000))

# 군인 할인


def soldierPrice(soldier):
    print("군인 할인 {0}명 가격은 {1}원 입니다." .format(soldier, soldier * 4000))

# theater_module.py 라는 파일이 만들어지고, 이게 하나의 모듈이 되는 거에요.
