# src/test.py

from src.main import mask_account_card, get_date

# Тестируем маскировку карт и счетов
card_info_1 = "Visa Platinum 7000792289606361"
masked_card_1 = mask_account_card(card_info_1)
print(masked_card_1)  # Вывод: Visa Platinum ************6361

card_info_2 = "Maestro 7000792289606361"
masked_card_2 = mask_account_card(card_info_2)
print(masked_card_2)  # Вывод: Maestro ************6361

account_info = "Счет 73654108430135874305"
masked_account = mask_account_card(account_info)
print(masked_account)  # Вывод: Счет ****************8305
# Тестируем функцию get_date
date_string = "11-07-2018"
formatted_date = get_date(date_string)
print(formatted_date)  # Вывод: 11.07.2018