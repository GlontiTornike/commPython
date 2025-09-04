text = input("შეიყვანე ტექსტი: ")

result = ""
for symbol in text:
    if symbol.isalpha() or symbol.isspace():
        result += symbol

print("ტექსტი:", result)
