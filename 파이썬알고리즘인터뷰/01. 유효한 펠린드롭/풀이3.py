import re

def isPalindrome(s: str) -> bool :
    s=s.lower()
    # 정규식으로 불필요한 문자 필터링 ( sub()의 두번째 파라미터를 통해 아예 없애버리는 작업)
    s= re.sub('[^a-z0-9]', '', s)

    return s==s[::-1] # 슬라이싱

if __name__ == "__main__" :
     input = input("문자열을 입력하세요 :")
     print(isPalindrome(input))