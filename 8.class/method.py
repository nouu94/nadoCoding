class Unit : 
    def __init__(self, name, hp, damage) -> None:
        # 멤버 변수 클래스 내 선언 된 변수. 그 변수를 가지고 초기화를 할수 있습니다.
        self.name = name 
        self.hp = hp 
        self.damage = damage 
        print("{0} 유닛이 생성 되었습니다." .format(self.name))
        print("체력 {0}, 공격력 {1}." .format(self.hp, self.damage))

# 메소드 생성 
# 공격 유닛
class AttackUnit : 
    def __init__(self, name, hp, damage) -> None:
        # 멤버 변수 클래스 내 선언 된 변수. 그 변수를 가지고 초기화를 할수 있습니다.
        self.name = name 
        self.hp = hp 
        self.damage = damage 
    
    '''
    지금 우리가 self를 많이 써 왔는데 self는 자기 자신을 의미하는 겁니다. 그리고 class 내에서 
    method 앞에는 항상 self를 무조건 적어주시면 됩니다. 
    '''

    def attack(self, location) : 
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
        .format(self.name, location, self.damage))
            # 이름과 공격력은 self를 썼죠? 그러면 이 class 자기 자신에 있는 멤버 변수 값을 출력하는 것.
            # location은 전달 받은 값을 쓴다는 얘기입니다.

    def damaged(self, damage) : 
        print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        print("{0} : {1} : 현재 체력은 {1} 입니다." .format(self.name, self.hp))

        if self.hp <= 0 : 
            print("{0} : 파괴되었습니다." .format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기.
firebat = AttackUnit("파이어뱃", 50, 16)
firebat.attack("5시")


# 공격 2번 받는다고 가정한다. 
firebat.damaged(25)
firebat.damaged(25)