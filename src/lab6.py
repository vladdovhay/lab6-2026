"""
Головна програма, яка використовує пакет temperature_converter.
"""
import math
import requests

from src.celsius_fahrenheit import celsius_to_fahrenheit, fahrenheit_to_celsius
from src.celsius_kelvin import celsius_to_kelvin, kelvin_to_celsius

if __name__ == "__main__":
    print(f"25 °C у Фаренгейтах: {celsius_to_fahrenheit(25)}")
    print(f"100 °F у Цельсіях: {fahrenheit_to_celsius(100):.2f}")
    print(f"0 °C у Кельвінах: {celsius_to_kelvin(0)}")
    print(f"300 K у Цельсіях: {kelvin_to_celsius(300):.2f}")

    # модуль зі стандартної бібліотеки
    print(f"25.3 °C у Фаренгейтах (округлено вгору): {math.ceil(celsius_to_fahrenheit(25.3))}")

    # сторонній пакет, встановлений через pip
    try:
        response = requests.get("https://www.google.com", timeout=5)
        print(f"Статус код запиту до Google: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Помилка при виконанні запиту: {e}")