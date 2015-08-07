#Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks.
#TODO: this looks ugly... can probably be improved
def censor(text, word):
    a = text.split(word)
    new_text = ""
    new_word = ""
    for c in word:
        new_word += "*"
    for n in range(0, len(a) - 1):
        new_text += a[n] + new_word
    new_text += a[len(a) - 1]
    return new_text

print censor("what the fudge is that", "fudge")