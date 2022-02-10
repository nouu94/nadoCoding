class Unit : 
    def __init__(self, name, hp, damage) -> None:
        # 멤버 변수 클래스 내 선언 된 변수. 그 변수를 가지고 초기화를 할수 있습니다.
        self.name = name 
        self.hp = hp 
        self.damage = damage 

        print("{0} 유닛이 생성 되었습니다." .format(self.name))
        print("체력 {0}, 공격력 {1}." .format(self.hp, self.damage))


# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않습니다.)
wraith1 = Unit("레이스", 80, 5)
# 객체.멤버변수, 객체. 을 한다면 멤버변수가 보인다. 
print("유닛 이름 : {0}, 공격력 : {1}" .format(wraith1.name, wraith1.damage))

# 상대방이 프로토스 다크아칸이 마인드 컨트롤 : 상대방 유닛을 내 것으로 만든느 것
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True : 
    print("{0} 는 현재 클로킹 상태입니다." .format(wraith2.name))
