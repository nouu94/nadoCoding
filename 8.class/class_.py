# class의 개념은 좀 어렵지만 파이썬에서 중요한 부분이라 꼭 해야됩니다. 
# 스타크래프트의 예로 들게요. 

# 마린 : 공격 유닛, 군인. 총을 쏩니다. 
name = "마린" # 유닛의 이름 
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력

print("{} 유닛이 생성되었습니다." .format(name))
print("체력 : {}, 공격력 : {}\n" .format(hp, damage))

# 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드가 있고 시즈 모드가 있다. 
tank_name = "탱크"
tank_hp = 150 
tank_damage = 35

print("{0} 유닛이 생성되었습니다." .format(tank_name))
print("체력 {0}, 공격력 {1}\n" .format(tank_hp, tank_damage))

tank_name2 = "탱크"
tank_hp2 = 150 
tank_damage2 = 35

print("{0} 유닛이 생성되었습니다." .format(tank_name2))
print("체력 {0}, 공격력 {1}\n" .format(tank_hp2, tank_damage2))



def attack(name, location, damage) : 
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" .format(\
        name, location, damage))

# 만들 수 있지만 너무 비효율 적이야. 같은 패턴의 코드를 한번 더 쓰잖아?! 
attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage2)
attack(tank_name2, "1시", tank_damage2)

# class는 붕어빵 틀 instance(객체)는 붕어빵!, 틀은 하나인데 붕어빵은 무한정으로 만들 수 있어요.
class Unit : 
    def __init__(self, name, hp, damage) : # self는 인스턴스 그 자기 자신을 가리킴
        self.name = name 
        self.hp = hp 
        self.damage = damage 
        print("{0} 유닛이 생성되었습니다." .format(self.name))
        print("체력 {0}, 공격력 {1}" .format(self.hp, self.damage))

# class의 생성자 파라미터는 name, hp, damage
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35) 

# 똑같은 하나의 클래스를 가지고 마린과 탱크를 만들었습니다.





