#  [Programming] Palindrome refers to words that have the same results when we read from the 
# beginning and read from the end, such as level, bob, and radar. Write a function that determines if 
# the given word is palindrome or not. Display the results when you put two different words (one is 
# palindrome and the other is not).

def is_palindrom(s: str):
    while len(s) > 1 :
        if s.pop(0) != s.pop():
            return False
    return True


if __name__=='__main__':
    word=list(input('Enter a word : '))
    print("Is word palindrome? Answer: ",is_palindrom(word))
    