# score_file = open("score.txt", "w", encoding="utf-8")

# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("./7.inAndOut/score.txt", "a", encoding="utf-8")
# score_file.write("과학 : 80\n")
# score_file.write("코딩 : 100")
# score_file.close()

# score_file = open("./7.inAndOut/score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("./7.inAndOut/score.txt", "r", encoding="utf8")
# #readline 자동으로 줄바꿈 해줌
# print(score_file.readline(), end="") # 줄 별로 읽기 동작을 수행 후 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(),end="") # 줄 별로 읽기 동작을 수행 후 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(),end="") # 줄 별로 읽기 동작을 수행 후 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(),end="") # 줄 별로 읽기 동작을 수행 후 한 줄 읽고 커서는 다음 줄로 이동

# score_file.close()

# score_file = open("./7.inAndOut/score.txt", "r", encoding="utf8")

# while True : 
#     line = score_file.readline()
#     if not line : 
#         break
#     else : print(line, end="")

# score_file.close()

score_file = open("./7.inAndOut/score.txt", "r", encoding="utf8")
print(type(score_file))
# lines = score_file.readlines() # 한 줄, 한 줄, list 형태로 저장한다.

# print(lines)

# for line in lines : 
#     print(line, end="")