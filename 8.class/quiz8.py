""" 
Quiz ) 주어진 코드를 활용하여 부동산 프로그램을 작성하세요. 

(출력 예제)
총 3대의 매물이 있습니다. 
강남 아파트 매매 10억 2010년 
마포 오피스텔 전세 5억 2007년 
송파 빌라 월세 500/50 2000년 

"""
class House : 
    # 매물 초기화 
    def __init__(self, location, house_type, deal_type, price, completion_year) : 
        # 매개변수 5개
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시 
    def show_detail(self) : 
        print(f"{self.location} {self.house_type} {self.deal_type} {self.price}\
 {self.completion_year}")

houses = []
apartment = House("강남", "아파트", "매매", "10억", "2010년")
op = House("강남", "아파트", "매매", "10억", "2007년")
villa = House("송파", "빌라", "월세", "500/50", "2015년")

houses.append(apartment)
houses.append(op)
houses.append(villa)

print("총 {0}대의 매물이 있습니다." .format(len(houses)))

for house in houses : 
    house.show_detail()
