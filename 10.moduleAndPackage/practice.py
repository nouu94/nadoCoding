""" import theater_module

theater_module.price(3)  # 3명이서 영화 보러 갔을 때
theater_module.earlyPrice(4)  # 4명이서 조조 할인 영화 보러 갔을 때
theater_module.soldierPrice(2)  # 2명이서 조조 할인 영화 보러 갔을 떄
 """

# import theater_module as mv

# mv.price(3)
# mv.earlyPrice(4)
# mv.soldierPrice(5)

# from theater_module import *
# # from random import *
# price(3)
# earlyPrice(2)
# soldierPrice(4)

# from theater_module import price, earlyPrice

# price(5)
# earlyPrice(3)

# from theater_module import soldierPrice as price

# price(5)

# import travel.thailand.ThailandPackage  # import는 모듈이나 패키지 ModuleNotFoundError
# import travel.thailand

# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# 다만 from import 구문에서는 클래스나 함수까지 적을 수 있어요.

# from travel.thailand import ThailandPackage

# trip_to = ThailandPackage()
# trip_to.detail()


# from travel import *  # travel 패키지의 모든 것을 가져오겠다. 공개 범위 설정
# from travel import vietnam  # travel 패키지의 vietnam 모듈


# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

import random
import inspect
from travel import *

trip2_to = thailand.ThailandPackage()
trip2_to.detail()

# 패키지 모듈의 위치??!

# inspect 모듈의 getfile(위치를 알고 싶은 모듈명) 함수를 쓰면 모듈의 경로를 알 수 있다.
print(inspect.getfile(random))
# C:\Users\ck12q\AppData\Local\Programs\Python\Python310\lib\random.py

print(inspect.getfile(thailand))
# c:\python_basic\10.moduleAndPackage\travel\thailand.py

# 이렇게 여러분들이 만든 패키지를 lib 경로에 가져다두면은 다른 프로젝트를 할 때
# 사용 가능합니다. 우리는 연습으로 만든 것이기 떄문에 ...
