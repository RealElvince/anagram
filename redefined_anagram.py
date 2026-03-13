def anagram():
    w1 = input("Enter first word: ").lower()
    w2 = input("Enter second word: ").lower()

    if sorted(w1) == sorted(w2):
        print("They are anagrams!")
    else:
        print("They are not anagrams!")

anagram()
