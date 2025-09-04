import random

word = input("შეიყვანეთ ერთი სიტყვა: ").strip()

if len(word.split()) > 1:
    print("მხოლოდ ერთი სიტყვა!")

else:
    add = ['იჩი', 'ოვნა', 'ზე', 'ელა']

    print(f" ზედმეტსახელები '{word}'-სთვის:")
    print(f"1. {word.lower()}{random.choice(add)}")
    print(f"2. პატარა {word}")
    print(f"3. {word[:3].lower()}{random.choice(add)}")
    print(f"4. {word.lower()}-{word.lower()}")
    print(f"5. {word.lower()}იკო")