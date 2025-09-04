sentence = input("შეიყვანეთ წინადადება: ")

words = sentence.split()
word_lengths = {word: len(word) for word in words}

print(word_lengths)