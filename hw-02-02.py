
from collections import deque
 
 
def is_palindrome(text: str) -> bool:
    """Повертає True, якщо рядок є паліндромом (без урахування регістру та пробілів)."""
    if not isinstance(text, str):
        raise TypeError("Вхідний параметр має бути рядком")
 
    # Нормалізація: casefold() — коректне зведення регістру (у т.ч. для кирилиці),
    # isspace() — відкидає пробіли, табуляції, переноси рядків
    chars = deque(ch.casefold() for ch in text if not ch.isspace())
 
    # Порівнюємо символи з обох кінців черги
    while len(chars) > 1:
        if chars.popleft() != chars.pop():
            return False
    return True
 
 
if __name__ == "__main__":
    examples = [
        "А роза упала на лапу Азора",      # класичний паліндром, непарна довжина
        "Я несу гусеня",                   # непарна довжина
        "abba",                            # парна довжина
        "Was it a car or a cat I saw",     # регістр + пробіли
        "Never odd or even",
        "racecar",
        "Python",                          # не паліндром
        "Hello World",                     # не паліндром
        "a",                               # один символ
        "",                                # порожній рядок
        "   ",                             # лише пробіли
    ]
 
    for s in examples:
        result = "так ✓" if is_palindrome(s) else "ні  ✗"
        print(f"{result} | {s!r}")
 
    print()
    user_input = input("Введіть рядок для перевірки (Enter — вихід): ")
    if user_input:
        verdict = "є" if is_palindrome(user_input) else "не є"
        print(f"Рядок {verdict} паліндромом.")
        