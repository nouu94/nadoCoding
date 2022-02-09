def open_account() : 
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money) : # 잔액, 입금되는 돈 
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다." .format(balance + money))
    return balance + money

def withdraw(balance, money) :  # 잔액, 출금되는 돈 
    if balance < money : # 잔액이 출금보다 적으면
        print("출금을 할 수 없습니다. 잔액이 부족합니다.")
    else : # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다.")
        return balance - money

def withdraw_night(balance, money) : # 저녁에 출금 (가지고 있는 금액, 출금 금액)
    commission = int(input('수수료를 입력하세요 : ')) # 수수료 100원 
    return (commission, balance - money - commission)

balance = 0 # 잔액 
balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원 입니다." .format(commission, balance))

