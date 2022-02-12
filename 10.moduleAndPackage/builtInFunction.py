# 내장 함수
# 따로 import 할 필요가 없다.
# 내장이 되어 있기 때문에 바로 사용 가능하다.

# input : 사용자 입력 받는 함수
# language = input("무슨 언어를 좋아하세요???")
# print("{0}은 아주 좋은 언어입니다!" .format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 알려줌
import pickle
import random  # 외장 함수
# print(dir())
# print(dir())

# print(dir())
# # pickle과 random을 쓸 수 있다고 알려준다. 리스트 반환

# print(dir(random))  # random 모듈 내에서 쓸 수있는 것들이 리스트로 반환되어 출력
# lst = [1, 2, 3]
# print(dir(lst))  # 리스트[]에서 쓸 수 있는 내용이 나오는거죠!!!

name = "Jim"
print(dir(name))  # str 에 대해서 쓸 수 있는 함수가 나오쥬
