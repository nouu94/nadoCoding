# import pickle 

# with open("./7.inAndOut/profile.pickle", "rb") as profile_file : 
#     print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file : 
    study_file.write("파이썬을 열심히 공부하고 있어요.\n으라차차")

# 변수 선언없이 with 키워드 하나로 해결이 가능하다. 

with open("study.txt", "r", encoding="utf8") as study_file : 
    print(study_file.read())
    