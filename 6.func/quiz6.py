'''
Quiz ) 표준 체중을 구하는 프로그램을 작성하세요 

* 표준 체중 : 각 개인의 키에 적당한 체중 

(성별에 따른 표준 체중 공식)
남자 : 키(m) * 키(m) * 22 
여자 : 키(m) * 키(m) * 21 

조건1 : 표준 체중은 별도의 함수 내에서 계산한다. 
    * 함수명 : std_weight 
    * 전달값 : 키(height), 성별(gender) # parameter (height, gender)

조건2 : 표준 체중은 소수점 둘째자리까지 표시한다. % .2f % 표준 체중 변수

 (출력 예제)
 키 175cm 남자의 표준 체중은 67.38kg 입니다. 
'''
# 조건 1
def std_weight(height, gender) : # height는 m로 표시
    if gender == '남자' : 
        stand_weight = '%.2f' % (height ** 2 * 22) # 조건 2
    elif gender == '여자' :
         stand_weight = '%.2f' % (height ** 2 * 21)

    return stand_weight

chulsu_std_weight = std_weight(1.75, '남자')
print(f'철수의 표준 체중은 {chulsu_std_weight}kg 이어야 합니다.')

yurim_std_weight = std_weight(1.55, '여자')
print(f'유림의 표준 체중은 {yurim_std_weight}kg 이어야 합니다.')

# 조건 1은 함수(func)를 생성(def), 조건 2는 표준 체중은 소수점 둘째자리까지 표시한다.

# round(실수, 2) 임의의 실수를 2째 자리까지 표시해줘!


         
