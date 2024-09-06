letter = str(input("Enter a letter: "))

if letter in "aeiouAEIOU":
    print("vowel")
elif letter == 'y':
    print("sometimes one or the other")
else:
    print("consonant")
