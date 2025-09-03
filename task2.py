import string

def password_strength(password: str) -> tuple[int, str]:
    score = 0

    # სიგრძე
    if len(password) >= 8:
        score += 2
    elif len(password) >= 5:
        score += 1

    # ციფრები
    if any(ch.isdigit() for ch in password):
        score += 2

    # სიმბოლოები
    if any(ch in string.punctuation for ch in password):
        score += 2

    # დიდი ასოები
    if any(ch.isupper() for ch in password):
        score += 2

    # პატარა ასოები
    if any(ch.islower() for ch in password):
        score += 1

    # განმეორებადი სიმბოლოების ჯარიმა
    if len(set(password)) < len(password):
        score -= 1

    # საბოლოო შეფასება
    if score <= 5:
        level = "weak"
    elif score <= 8:
        level = "medium"
    else:
        level = "strong"

    return score, level



password = input("შეიყვანე პაროლი: ")
score, level = password_strength(pwd)
print(f"შეფასება: {score}/10 → {level}")
