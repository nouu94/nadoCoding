'''
Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다. 
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하세요.

조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다. 
조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다. 

(출력문 예제)
[0] 1번째 손님 (소요시간 : 15분)
[] 2번째 손님 (소요시간 : 50분)
[0] 3번째 손님 (소요시간 : 5분)
...
[] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2 분
'''

from random import * # randint 사용.

customers = list(range(1, 51)) # 매일 50명의 승객과 매칭
# print(customer)
total_riding_customers = 0 # 총 탑승 승객

for customer in customers : 
    spending_time = randint(5, 50)
    if spending_time > 15 : 
        print(f"[] {customer}번째 손님 (소요시간 : {spending_time}분)")
    else : 
        print(f"[O] {customer}번째 손님 (소요시간 : {spending_time}분)")
        total_riding_customers += 1

print(f"\n총 탑승 승객 : {total_riding_customers} 분")
