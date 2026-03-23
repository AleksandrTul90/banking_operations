# src/main.py

from src.masks import mask_card_number, mask_account_number


def mask_account_card(input_string: str) -> str:
    """
    Маскирует номер карты или счета на основе типа (Visa, Maestro или Счет).
    Пример входных строк:
    - "Visa Platinum 7000792289606361"
    - "Maestro 7000792289606361"
    - "Счет 73654108430135874305"

    Возвращает строку с маскированным номером.
    """
    parts = input_string.split()  # Разбиваем строку на части
    account_type = parts[0]  # Первый элемент — тип карты или счета
    account_number = parts[-1]  # Последний элемент — номер карты или счета

    # В зависимости от типа используем соответствующую функцию маскировки
    if account_type in ['Visa', 'Maestro']:
        return f"{account_type} {mask_card_number(account_number)}"
    elif account_type == 'Счет':
        return f"Счет {mask_account_number(account_number)}"
    else:
        raise ValueError("Неизвестный тип карты или счета")


import re


def get_date(date_string: str) -> str:
    """
    Принимает строку с датой в формате "dd-mm-yyyy" или "dd/mm/yyyy",
    и возвращает дату в формате "dd.mm.yyyy".

    Пример:
    "11-07-2018" -> "11.07.2018"
    "11/07/2018" -> "11.07.2018"
    """
    # Применяем регулярное выражение для поиска даты в различных разделителях
    match = re.match(r"(\d{2})[-/](\d{2})[-/](\d{4})", date_string)
    if match:
        day, month, year = match.groups()
        return f"{day}.{month}.{year}"
    else:
        raise ValueError("Неверный формат даты")