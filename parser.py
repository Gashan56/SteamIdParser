import requests
from bs4 import BeautifulSoup


def parse_id():
    while True:
        try:
            start = int(input("Введите начальный ID: "))
            stop = int(input("Введите конечный ID: "))
            if start > stop:
                print("Ошибка: начальный ID не может быть больше конечного")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число")

    cool_ids = []
    print(f"Парсер запущен, начинаю вывод ID")
    for steam_id in range(start, stop + 1):
        url = f'https://steamcommunity.com/id/{steam_id}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Проверяем наличие ошибки "Указанный профиль не найден"
            error_message = soup.find('h3', class_='custom-cursor-default-hover')
            if error_message and "Указанный профиль не найден" in error_message.text:
                cool_ids.append(steam_id)
                print(steam_id)
            # Дополнительная проверка на страницу с ошибкой
            elif soup.find('div', class_='error_ctn'):
                cool_ids.append(steam_id)
                print(steam_id)

        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе ID {steam_id}: {e}")
    print(f'Доступные ID: {cool_ids}')


parse_id()
input("\nНажмите Enter для выхода...")