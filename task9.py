text = input("შეიყვანეთ ტექსტი: ")

words = text.lower().split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

max_count = max(word_count.values())
most_frequent = [word for word, count in word_count.items() if count == max_count]

print(f"ყველაზე ხშირი სიტყვა: {most_frequent}")
