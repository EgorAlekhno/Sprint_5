# генерация случайных данных для регистрации
from faker import Faker
import random


def get_sign_up_data():
    fake = Faker()
    # генерация имени и фамилии
    first_name = fake.first_name().lower()
    last_name = fake.last_name().lower()
    # генерация 3 случайных цифр
    random_digits = ''.join([str(random.randint(0, 9)) for _ in range(3)])
    # формирование email
    email = f"{first_name}_{last_name}_{random_digits}@yandex.com"
    # генерация пароля
    password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return email, password
