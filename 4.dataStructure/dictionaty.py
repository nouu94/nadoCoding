# # 사전 { key : value }
# cabinet = {3 : "유재석", 100 : "김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# # print(cabinet[5]) # keyError
# print(cabinet.get(5)) # None 출력
# print(cabinet.get(5, "사용 가능"))

# print(3 in cabinet) # True 
# print(5 in cabinet) # False
# print(5 not in cabinet) # True

# cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 새 손님 
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# # 간 손님 
# del cabinet["A-3"]
# print(cabinet)

# # key 들만 출력 
# print(cabinet.keys())

# # value 들만 출력 
# print(cabinet.values())

# # key, value 쌍으로 출력 
# print(cabinet.items())

# # 목욕탕 폐점 
# cabinet.clear()
# print(cabinet)

cabinet = {3 : "유재석", 100 : "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) # KeyError : 5
# print(cabinet.get(5, "사용 가능합니다.")) # None

# print(3 in cabinet) # 3이라는 키가 캐비넷에 있니? 
# print(5 in cabinet) # 5라는 키가 캐비넷에 있니? 
# print(6 in cabinet)

cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님 
print(cabinet)
cabinet["A-30"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님 
del cabinet["A-3"]
print(cabinet)

# key 들만 출력 
print(cabinet.keys())

# value 들만 출력 
print(cabinet.values())

# key, value 쌍으로 출력 
print(cabinet.items())

# 목욕탕 폐점 
cabinet.clear()
print(cabinet)


