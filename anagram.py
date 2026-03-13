def anagram():
    first_word = input("Enter first word: ")
    second_word = input("Enter second word: ")

    first_word_lower = first_word.lower()
    second_word_lower = second_word.lower()

    if len(first_word_lower) != len(second_word_lower):
        print(f"{first_word} and {second_word} are not anagrams!")
    else:
        if sorted(first_word_lower) == sorted(second_word_lower):
            print(f"{first_word} and {second_word} are anagrams!")
        else:
            print(f"{first_word} and {second_word} are not anagrams!")

anagram()
