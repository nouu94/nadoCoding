""" Quiz ) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다. 
참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다. 
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다. 
추첨 프로그램을 작성하세요. 

조건1 : 편의상 댓글은 20명이 작성했고 아이디는 1 ~ 20 이라고 가정한다. 
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복은 불가하다. 
조건3 : random 모듈의 shuffle 과 sample을 활용한다. """

# (출력 예제)
#  -- 당첨자 발표 --
# 치킨 당첨자 : 1 
# 커피 당첨자 : [2, 3, 4]
#  -- 축하합니다. -- 

# (활용 예제)
# from random import * 
# lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

from random import * 
lst = []
lst = [i for i in range(21)]
# print(lst)
shuffle(lst)
# print(lst)
comment_winning_chicken = int(sample(lst, 1)[0])
comment_winning_coffee = sample(lst, 3)

print(f'-- 당첨자 발표 --\n치킨 당첨자 : {comment_winning_chicken}\n커피 당첨자 : {comment_winning_coffee} \
    \n-- 축하합니다 --')

