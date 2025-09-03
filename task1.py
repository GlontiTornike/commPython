import random
import string

# პაროლის სიგრძე
length = int(input("შეიყვანე პაროლის სიგრძე: "))

#სანამ y ან n არ იქნება, მანამდე შეეკითხება

def ask_choice(question):

    choice = input(question).lower()
    while choice not in ("y", "n"):
        print("გთხოვ, შეიყვანე მხოლოდ y ან n!")
        choice = input(question).lower()
    return choice == "y"

# მომხმარებლის არჩევანი
use_lower = ask_choice("გამოვიყენოთ პატარა ასოები? (y/n): ")
use_upper = ask_choice("გამოვიყენოთ დიდი ასოები? (y/n): ")
use_digits = ask_choice("გამოვიყენოთ ციფრები? (y/n): ")
use_symbols = ask_choice("გამოვიყენოთ სიმბოლოები? (y/n): ")

# სიმბოლოების შესაგროვებელი

characters = ""

if use_lower:
    characters += string.ascii_lowercase
if use_upper:
    characters += string.ascii_uppercase
if use_digits:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

# თუ მომხმარებელმა შეიყვანა ქართული ან არატექნიკური სიმბოლოები
if any("ა" <= ch <= "ჰ" for ch in characters):
    print("შეიყვანე მხოლოდ ლათინური ასოები")
else:
    if not characters:
        print("უნდა აირჩიო მაინც ერთი სიმბოლოთა ჯგუფი!")
    else:
        # პაროლის გენერაცია
        password = "".join(random.choice(characters) for _ in range(length))
        print(f"შენი პაროლია: {password}")
