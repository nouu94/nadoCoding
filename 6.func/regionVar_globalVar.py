gun = 10 

def checkpoint(soldiers) : # 경계근무 군인 수  
    global gun # 전역 공간에 있는 gun을 사용할래요~
    gun =  gun - soldiers
    print(f"[함수 내 ] 남은 총 : {gun}")

def checkpoint_ret(gun, soldiers) : 
    gun = gun - soldiers
    print(f"[함수 내 ] 남은 총 : {gun}")

    return gun

print("전체 총 : {0}" .format(gun))
# checkpoint(5) # 2명이 경계 근무를 나간다. 
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}" .format(gun))

# 전역 변수와 지역 변수의 개념을 잘 기억 합시다!