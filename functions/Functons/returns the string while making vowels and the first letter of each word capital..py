txt = "welcome at codezilla python course we are happy to have you here"
def capitalize_vowels_and_first_letter(txt):
    vowels = "aeiouAEIOU"
    words = txt.split()
    capitalized_words = []  
    for word in words:
        capitalized_word = ""
        for i, char in enumerate(word):
            if char in vowels or i == 0:
                capitalized_word += char.upper()
            else:
                capitalized_word += char.lower()   
        capitalized_words.append(capitalized_word) 
    return ' '.join(capitalized_words)
print(capitalize_vowels_and_first_letter(txt))