# 애완 동물을 소개해주세요! 
""" print("우리집 강아지의 이름은 연탄이예요")
print("얀탄이는 4살이며, 산책을 아주 좋아해요~")
print("연탄이는 어른일까요? True") """

# 우리 집 강아지 이름은 해피인데?! 

my_pet_name = "연탄"
animal = "멍뭉이"
age = 2
hobby = "낮잠"
is_adult = (age >= 3)

'''
이렇게 하면 
여러 문장이 
주석처리 됩니다.
'''

print("우리집 " + animal + "의 이름은 " + my_pet_name + " 입니다.")
hobby = "공놀이"
print(my_pet_name + "는 " + str(age) + "살이며, 산책을 아주 좋아합니다.")
print(my_pet_name, "는 ", str(age), "살이며, 산책을 아주 좋아합니다.")
print(my_pet_name + "(이)는 어른일까요? " + str(is_adult))
