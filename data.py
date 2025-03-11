import random
import string


class CommonData:
    random_name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(5, 10))).capitalize()
    password = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(5, 10))).capitalize()
    invalid_password = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(1, 5))).capitalize()
    valid_email = 'kokokoko@gmail.com'
    valid_password = 'Qwerty123'
    first_name = ''.join(random.choices(string.ascii_lowercase, k=5))  # 5 случайных букв для имени
    last_name = ''.join(random.choices(string.ascii_lowercase, k=7))  # 7 случайных букв для фамилии
    cohort_number = random.randint(1900, 2100)  # Номер когорты (например, 1999)
    random_digits = ''.join(random.choices(string.digits, k=3))  # 3 случайные цифры
    domain = random.choice(["yandex.ru", "gmail.com", "mail.ru"])  # Случайный домен из списка
    random_email = f"{first_name}_{last_name}_{cohort_number}_{random_digits}@{domain}"

