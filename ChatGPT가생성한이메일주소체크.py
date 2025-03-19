import re  # re 모듈을 가져옵니다. 이 모듈은 정규 표현식을 사용하여 문자열을 검사할 수 있게 해줍니다.

def is_valid_email(email):
    # 이메일 주소가 유효한지 확인하는 패턴을 정의합니다.
    # 이 패턴은 이메일 주소가 올바른 형식인지 검사합니다.
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    # 이메일 주소가 패턴과 일치하는지 확인합니다.
    return re.match(pattern, email) is not None

# 테스트할 이메일 샘플을 리스트로 만듭니다.
email_samples = [
    "valid.email@example.com",  # 올바른 이메일 주소
    "user.name+tag@sub.domain.co.uk",  # 올바른 이메일 주소
    "invalid-email@.com",  # 잘못된 이메일 주소 (도메인 부분이 잘못됨)
    "no_at_symbol.com",  # 잘못된 이메일 주소 (@ 기호가 없음)
    "@missingusername.com",  # 잘못된 이메일 주소 (사용자 이름이 없음)
    "user@domain",  # 잘못된 이메일 주소 (도메인 부분이 잘못됨)
    "user@domain..com",  # 잘못된 이메일 주소 (도메인 부분에 점이 두 개 있음)
    "user@-domain.com",  # 잘못된 이메일 주소 (도메인 부분이 잘못됨)
    "valid_123@test.net",  # 올바른 이메일 주소
    "name@company.io"  # 올바른 이메일 주소
]

# 이메일 검증을 실행합니다.
for email in email_samples:
    # 이메일 주소가 유효한지 검사하고 결과를 출력합니다.
    print(f"{email}: {'Valid' if is_valid_email(email) else 'Invalid'}")
