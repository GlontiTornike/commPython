def is_palindrome(s):
    return s == s[::-1]

text = input("შეიყვანე ტექსტი: ")

# შემოწმება
if is_palindrome(text):
    print("ეს ტექსტი პალინდრომია")
else:
    found = False

    # ვცდილობთ თითო სიმბოლოს წაშლას
    for i in range(len(text)):
        candidate = text[:i] + text[i+1:]
        if is_palindrome(candidate):
            print("ეს ტექსტი არაა პალინდრომი")
            print(f"მაგრამ შეგიძლია გახადო პალინდრომი თუ ამოშლი '{text[i]}'-ს  {candidate}")
            found = True
            break

    if not found:
        print("ეს ტექსტი არაა პალინდრომი ")
