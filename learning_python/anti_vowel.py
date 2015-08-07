#Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.

def anti_vowel(text):
    new_text = ""
    vowels = ["a", "e", "i", "o", "u"]
    for c in text:
        if not (c.lower() in vowels):
            new_text += c
    return new_text

print ("Hey You!")