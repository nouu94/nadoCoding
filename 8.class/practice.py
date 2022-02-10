from random import *
# 일반 유닛 
class Unit : 
    def __init__(self, name, hp, speed) : 
        self.name = name 
        self.hp = hp 
        self.speed = speed
        print("{0} 유닛이 생성되었습니다." .format(name))

    def move(self, location) : 
        # print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
            .format(self.name, location, self.speed))

    def damaged(self, damage) : 
        print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다." .format(self.name, self.hp))

        if self.hp <= 0 : 
            print("{0} : 파괴되었습니다." .format(self.name))

# 공격 유닛 
class AttackUnit(Unit) : 
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location) : 
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))

# 마린 
class Marine(AttackUnit) : 
    def __init__(self):
        super().__init__("마린", 40, 5, 1)

    # 스팀팩 : 일정 시간 동안 공격 속도를 증가, 자기 체력 10 감소
    def stimpack(self) : 
        if self.hp > 10 : 
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)" .format(self.name))
        else : 
            print("{0} : 체력이 부족해서 스팀팩을 사용하지 않습니다." .format(self.name))

# 탱크 클래스 
class Tank(AttackUnit) : 
    def __init__(self):
        super().__init__("Tank", 150, 35, 4)

    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격이 가능합니다. 이동은 불가.
    seize_developed = False # 시즈모드 개발 여부 

    def __init__(self) : 
        AttackUnit.__init__(self, "탱크", 150, 35, 1)
        self.seize_mode = False

    def set_seize_mode(self) : 
        if Tank.seize_developed == False : 
            return 

        # 현재 시즈모드가 아닐 때 -> 시즈모드
        if self.seize_mode == False : 
            print("{0} : 시즈모드로 전환합니다." .format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드일 때 -> 시즈모드 해제
        else : 
            print("{0} : 시즈모드를 해제합니다." .format(self.name))
            self.damage /= 2
            self.seize_mode = False





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
        # print("[공중 유닛 이동]")
        self.fly(self.name, location) 


# 레이스 
class Wraith(FlyableAttackUnit) :
    def __init__(self):
        super().__init__("레이스", 8, 120, 6)
        self.clocked = False # 클로킹 모드 (해제 상태)

    def clocking(self) : 
        if self.clocked == True : # 클로킹 모드 -> 모드 해제
            print("{0} : 클로킹 모드를 해제합니다." .format(self.name))
            self.clocked = False 
        else : # 클로킹 모드를 해제 -> 모드 설정 
            print("{0} : 클로킹 모드 설정합니다." .format(self.name))
            self.clocked = True


def game_start() : 
    print("새로운 게임이 시작되었습니다.")

def game_over() : 
    print("Player : gg") # good game 
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

# 실제 게임을 진행한다. 
game_start()

# 마린 3마리 생성 
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성 
w1 = Wraith()

# 유닛 일괄 관리 (생성된 모든 유닛을 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# print(f"attack_units 리스트는 다음과 같은 원소들이 있습니다 : {attack_units}")
# 전군 이동 
for unit in attack_units : 
    unit.move("1시")

# 탱크 시즈모드 개발 
Tank.seize_developed = True 
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드를 준비한다. (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units : 
    if isinstance(unit, Marine) : # isinstance(unit, Marine) unit 이라는 변수가 마린 객체라면..
        unit.stimpack()
    elif isinstance(unit, Tank) : 
        unit.set_seize_mode()
    elif isinstance(unit, Wraith) : 
        unit.clocking()

# 전군 공격을 시킨다. 
for unit in attack_units : 
    unit.attack("1시")


# 전군 피해 
for unit in attack_units :
    unit.damaged(randint(5, 20)) # 공격은 랜덤으로 받음 5 ~ 20 사이

    
# 게임 종료 
game_over()


