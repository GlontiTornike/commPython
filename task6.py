import random

numbers_input = input("შეიყვანეთ რიცხვები (გამოტოვებით): ")
numbers = [int(x) for x in numbers_input.split()]

while True:
    print("სორტირების ვარიანტები:")
    print("1. ზრდადობით")
    print("2. კლებადობით")
    print("3. რანდომად")
    print("4. მხოლოდ უნიკალური")

    choice = input("აირჩიეთ (1-4): ")

    if choice == "1":
        result = sorted(numbers)
    elif choice == "2":
        result = sorted(numbers, reverse=True)
    elif choice == "3":
        result = numbers.copy()
        random.shuffle(result)
    elif choice == "4":
        result = list(set(numbers))
    else:
        result = numbers

    print(f"შედეგი: {result}")
