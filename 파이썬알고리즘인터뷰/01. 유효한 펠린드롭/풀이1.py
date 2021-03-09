# 리스트로 변환하기

def isPalindrome(s: str)->bool:
    strs =[]
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs) > 1 :
        if strs.pop(0) != strs.pop():
            return False

    return True


if __name__ == "__main__" :
     input = input("문자열을 입력하세요 :")
     print(isPalindrome(input))