import collections 

def isPalindrome(s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s :
        if char.isalnum():
            strs.append(char.lower())

    while len(strs)>1 :
        if strs.popleft() != strs.pop():
            return False
        return True 

if __name__ == "__main__" :
     input = input("문자열을 입력하세요 :")
     print(isPalindrome(input))