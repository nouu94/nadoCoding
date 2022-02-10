'''
연산자 오버라이딩
부모 클래스에서 정의한 메소드 말고 자식 클래스에서 정의한 메소드를 쓰고 싶어요.
메소드를 새롭게 정의하는데 이를 오버라이딩 이라고 합니다.
'''
# 일반 유닛 
class Unit : 
    def __init__(self, name, hp, speed) : 
        self.name = name 
        self.hp = hp 
        self.speed = speed

    def move(self, location) : 
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
            .format(self.name, location, self.speed))

# 공격 유닛 
class AttackUnit(Unit) : 
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location) : 
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))

    def damaged(self, damage) : 
        print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다." .format(self.name, self.hp))

        if self.hp <= 0 : 
            print("{0} : 파괴되었습니다." .format(self.name))

# 드랍쉽 : 공중 유닛, 수송기. 마린/ 파이어뱃/ 탱크 등을 수송하여 다른 곳에 떨어뜨림 공격 기능x 
# 날 수 있는 기능을 가진 클래스
class Flyable : 
    def __init__(self, flying_speed) : 
        self.flying_speed = flying_speed

    def fly(self, name, location) : 
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" \
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable) : 
    def __init__(self, name, damage, hp, flying_speed) : # q) 왜 여기에 0은 안넣지?
        AttackUnit.__init__(self, name, hp, damage, 0) # 지상 speed 0 
        Flyable.__init__(self, flying_speed)

    def move(self, location) : # UnitClass.move() 메소드 오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location) 


# 벌처 : 지상 유닛, 기동성 좋음 
vulture = AttackUnit("벌처", 80, 20, 10)

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋고, 공격력도 좋다. 
battlecruiser = FlyableAttackUnit("배틀크루저", 25, 500, 3)

# vulture.move("11시")
# battlecruiser.fly("1시")
battlecruiser.move("11시")

'''
그런데 지금 문제가 뭐냐면 지상 유닛은 move 함수를 써야되고, 공중 유닛은 fly로 써야됨
그래서 지상 유닛인지 공중 유닛인지 확인해가면서 함수를 써야돼요. 조온나 귀찮죠? 
'''

# 건물 
class BuildingUnit(Unit) :
     def __init__(self, name, hp, location) : 
        #  Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location


# 서플라이 디팟 : 건물, 1개 건물 = 8 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
    

    



