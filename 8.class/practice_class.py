class Unit : 
    def __init__(self) : 
        print("Unit 생성자")


class Flyable : 
    def __init__(self) : 
        print("Flyable 생성자")


class FlyableUnit(Unit, Flyable) : 
    def __init__(self) : 
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽 
dropship = FlyableUnit()

# 두개 이상의 클래스를 다중 상속 받을 때 super() 키워드를 쓰면 
# 순서 상에 첫 번째 부모 클래스에 대해서 상속받는다. 
# 그러니까 왠만하면 하나의 부모 클래스를 상속 받았을 때만 super() 키워드를 씁시다.
