'''
Quiz ) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다. 
보고서는 항상 아래와 같은 형태로 출력되어야 합니다. 

- X 주차 주간보고 - 
부서 : 
이름 : 
업무 요약 : 

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하세요.

조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다. # 반복문?!
'''

# #with 문 : with open("경로/파일명", "w", encoding="utf8") as open 파일에 대한 변수명 
# for index in range(1, 51) :
#     with open(f"./7.inAndOut/report/{index}주차.txt", 'w', encoding='utf-8') as report_file : 
#         report_file.write(f"- {index} 주차 주간보고 -\n부서 :\n이름 :\n업무 요약 :")
#         report_file.close()

# with문 없이 쓰는 문장
# 참고로 .write() 함수는 print와 다르게 default 개행이 없습니다. 개행을 하고 싶다면 꼭 \n 작성 
# for index in range(1, 51) : 
#     report_file = open(f"./7.inAndOut/report2/{index}주차.txt", 'w', encoding='utf-8')
#     report_file.write(f"- {index} 주차 주간보고 -\n")
#     report_file.write("부서 : \n")
#     report_file.write("이름 : \n")
#     report_file.write("업무 요약 : \n")

#     report_file.close()

report_file_first = open(f"./7.inAndOut/report2/1주차.txt", 'r', encoding='utf-8')
report_file_list = report_file_first.read()
print(report_file_list)

# for report_file in report_file_list : 
#     print(report_file, end="") # print문을 작성한다면 end parameter default가 \n이므로 ""로 바꿈

# report_file_first.close()