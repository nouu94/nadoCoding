hyeonje = "940222-1051154"

print("성별 : " + hyeonje[7])
print("년 : " + hyeonje[0:2]) # 0 ~ 2 직전까지 (0, 1)
print("월 : " + hyeonje[2:4])
print("일 : " + hyeonje[4:6])

print("생년월일 : " + hyeonje[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + hyeonje[7:]) # 7번째부터 끝까지

# print(hyeonje[:-1])
print("뒤 7자리 (뒤에부터) : " + hyeonje[-7:]) # 맨 뒤 7번째 부터 끝까지

'''
940222 - 1005517
-14-13-12-11-10-9-8.....-1
음수의 슬라이싱은 음수니까 반대로 생각하면 된다.
'''