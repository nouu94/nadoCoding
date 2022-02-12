'''
Quiz ) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드세요. 

조건 : 모듈 파일명은 byme.py 로 작성 

(모듈 사용 예제)
import byme # 모듈 이름 byme 
byme.sign() # sign() 메소드 생성 

(출력 예제 )
이 프로그램은 Nouu에 의해 만들어졌습니다. 
유튜브 : http://youtube.com
이메일 : nadocoding@gmail.com
'''

import byme  # import는 패키지나 모듈까지만 호출 가능
from byme import sign as sg  # from 모듈이나 패키지 import 클래스나 함수 메서드

# sg()
byme.sign()
