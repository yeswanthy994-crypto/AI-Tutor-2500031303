word=input("Enter a word : ") or "Python"

print("Word :",word)
print("Length of the word :",len(word))

characters=list(word)

print("Characters :",characters)
pairs=list(zip(characters,characters[1:]))

print("Adjacent pairs :",pairs)
