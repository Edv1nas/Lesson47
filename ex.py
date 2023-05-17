"#CodeWars"
"# Reverse words from sentence with 5 or more letters"


def reverse_long_words(sentence):
    return " ".join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])


reversed_words = reverse_long_words("Hello how are you my friend")
print(reversed_words)

"# Capitalize first letter in all words"


def capitalize_words_first_letter(sentence):
    # new = []
    # words = sentence.split()
    # for word in words:
    #     new.append(word.capitalize())
    # return " ".join(new)

    return " ".join([(word.capitalize()) for word in sentence.split()])


capitalized_words = capitalize_words_first_letter(
    "Hello how are you my friend")
print(capitalized_words)
