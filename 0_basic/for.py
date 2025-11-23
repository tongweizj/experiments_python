user_word = input("Please enter a word: ")
user_word = user_word.upper()
word_without_vowels  = ""
for letter in user_word:
    if letter in ["A", "E", "I", "O", "U"]:
        continue
    print(letter)
    word_without_vowels += letter
print(word_without_vowels)
