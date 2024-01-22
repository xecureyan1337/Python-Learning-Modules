import string

# provides concatenation ascii's lowercase and uppercase
def all_alphabet():
    alphabets = string.ascii_letters
    i = 0
    while i < len(alphabets):
        if 0 < i:
            print(",",end=" ")
        
        print(alphabets[i],end="")

        i += 1

def lower_alphabet():
    alphabets = string.ascii_lowercase

    for alphabet in alphabets:
        print(alphabet, end="")
    
    print()

def upper_alphabet():
    alphabets = string.ascii_uppercase

    for alphabet in alphabets:
        print(alphabet, end="")

    print()

def reverse_word(x):
    print (x[::-1])


if __name__ == "__main__":

    all_alphabet()
    lower_alphabet()
    upper_alphabet()
    
    reverse_word("? emit a evah uoy od")
