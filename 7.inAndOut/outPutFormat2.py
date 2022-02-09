# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보 
print("{0: >10}" .format(100))

# 양수일 땐 +로 표시, 음수일 땐 -로 표시 
print("{0: >+10}" .format(500))
print("{0: >+10}" .format(-500))

# 왼쪽 정렬하고, 빈칸을 _(밑줄)로 채움
print("{0:_<+10}" .format(500))
print("{0:_<+10}" .format(50000000))
# 3자리 마다 콤마를 찍는다. 
print("{0:,}" .format(10000000))

# 3자리 마다 콤마를 찍어주는데 +- 부호 붙이기 
print("{0:+,}" .format(1000000))

# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수도 확보한다. 
# 돈이 많으면 기분이 좋다. 빈 자리는 ^ 로 채워주기 
print("{0:^<+30,}" .format(1000))