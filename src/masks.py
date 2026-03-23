# src/masks.py
def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты, оставляя только последние 4 цифры видимыми.
    Например: 7000792289606361 -> ************6361
    """
    return '*' * (len(card_number) - 4) + card_number[-4:]

def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счета, оставляя только последние 4 цифры видимыми.
    Например: 73654108430135874305 -> ****************8305
    """
    return '*' * (len(account_number) - 4) + account_number[-4:]