absent = [2, 5] # 결석
no_book = [7] # 출석은 했는데 책을 안가져옴
for student in range(1, 11) : #1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    if student in absent : 
        continue
    elif student in no_book : 
        print(f"오늘 수업 여기까지. {student}학생은 교무실로 따라오세요.")
        break
    print(f'{student}학생, 책 읽으세요.')