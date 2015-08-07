#codeacademy create function the returns reversed string without using reversed or [::-1]
def reverse(text):
    new_text = ""
    for c in text:
        new_text = c + new_text
    return new_text

print reverse("abcd!")