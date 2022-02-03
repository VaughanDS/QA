# Given a string, return the boolean True if it ends in "py", and False if not ignore case

def stringcheck(phrase):
    if phrase.lower().endswith("py"):
        return True
    else:
        return False


phrase = input("Input phrase: ")
print(stringcheck(phrase))