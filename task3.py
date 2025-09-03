def fibonacci_sequence():
    user_input = input("შეიყვანე რიცხვი (ფიბონაჩის რიგის სიგრძე): ")

    # შემოწმება, რიცხვია თუ არა
    if not user_input.isdigit():
        # თუ ციფრი არ არის, ვამოწმებთ რას ჰგავს
        if user_input.isalpha():
            print(f"შენ შემოიტანე ასო '{user_input}' — არასწორია, მხოლოდ რიცხვი!")
        elif not user_input.strip():
            print("შენ არაფერი არ შემოიტანე — მხოლოდ რიცხვი შეიყვანე!")
        else:
            print(f"შენ შემოიტანე სიმბოლო '{user_input}' — არასწორია, მხოლოდ რიცხვი!")
        return

    n = int(user_input)

    # ფიბონაჩის რიგი
    fib = [0, 1]
    while len(fib) < n:
        #წინა რიცხვს ვუმატებთ იმის წინა რიცხვს
        fib.append(fib[-1] + fib[-2])

    print(f"ფიბონაჩის რიგი ({n} სიგრძით): {fib[:n]}")


# --- main ---
fibonacci_sequence()
