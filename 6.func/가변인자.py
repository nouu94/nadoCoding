# def profile(name, age, lang1, lang2, lang3, lang4, lang5) : 
#     print("이름 : {0}\t나이 : {1}\t" .format(name, age), end=" ") # end 키워드 print default는 \n
#     print(lang1, lang2, lang3, lang4, lang5)

# 가변 인자 : parameter의 수를 고정적으로 부여하는게 아닌 가변적으로 부여하는 것이다.
# *(asterisk)와 for문을 사용한다.

def profile(name, age, *language) : 
    print("이름 : {0}\t나이 : {1}\t" .format(name, age), end=" ") # end 키워드 print default는 \n
    for lang in language : 
        print(lang, end=" ")
    print()


profile("유재석", 20, "python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")