python = "Python is Amazing"
print(python.lower()) # 소문자
print(python.upper()) # 대문자
print(python[0].isupper()) # 대문자니? True, 소문자니? False

print(len(python)) # str의 길이를 출력한다.
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))

print(python.find("Java"))
# print(python.index("Java"))

print(python.count("n"))
