""" 
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하세요. 

예) http://naver.com 
규칙1 : http:// 부분은 제외 => naver.com 
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver.com 
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성 
                (nav)               (5)             (1)         (!)

ex) 생성된 비밀번호 : nav51! 
"""

site_url = input('url을 입력하세요 : ')
# 아! 부분 문자열 추출은 무조건적으로 인덱싱과 슬라이싱을 이용하자. 
# (find나 index 함수로 해결하려다가 30분 지체했네 ㅋㅋ)
my_str = site_url.replace("http://", "") if site_url[:7] == 'http://' else \
        site_url.replace('https://', "")
print(site_url.find('http://'))
print(my_str)

# naver 글자만 남기기
my_str = my_str[:my_str.index(".")] # 규칙 2
# print(my_str)

password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!' # 규칙 3 비밀번호 생성

print(f"생성된 비밀번호 : {password}")
