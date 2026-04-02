"""
Модуль для обработки банковских операций.

Содержит функции для фильтрации и сортировки данных о банковских операциях.
"""

from typing import Any, Dict, List


def filter_by_state(
    operations: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по статусу.

    Принимает список словарей с данными о банковских операциях и фильтрует
    их по значению ключа 'state'. Возвращает новый список, содержащий только
    те словари, у которых ключ state соответствует указанному значению.

    Args:
        operations: Список словарей с данными о банковских операциях.
        state: Статус для фильтрации (по умолчанию 'EXECUTED').

    Returns:
        Новый список словарей, отфильтрованных по статусу.

    Example:
        >>> data = [
        ...     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03'},
        ...     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12'},
        ... ]
        >>> filter_by_state(data)
        [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03'}]
        >>> filter_by_state(data, 'CANCELED')
        [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12'}]
    """
    return [
        operation
        for operation in operations
        if operation.get("state") == state
    ]


def sort_by_date(
    operations: List[Dict[str, Any]], reverse: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует список операций по дате.

    Принимает список словарей и сортирует их по значению ключа 'date'.
    По умолчанию сортирует в порядке убывания (новые операции в начале).

    Args:
        operations: Список словарей с данными о банковских операциях.
        reverse: Порядок сортировки (True для убывания, False для возрастания).
                 По умолчанию True (убывание).

    Returns:
        Новый список словарей, отсортированных по дате.

    Example:
        >>> data = [
        ...     {
        ...         'id': 41428829,
        ...         'state': 'EXECUTED',
        ...         'date': '2019-07-03T18:35:29',
        ...     },
        ...     {
        ...         'id': 939719570,
        ...         'state': 'EXECUTED',
        ...         'date': '2018-06-30T02:08:58',
        ...     },
        ... ]
        >>> sort_by_date(data)[0]['id']
        41428829
        >>> sort_by_date(data, False)[0]['id']
        939719570
    """
    return sorted(operations, key=lambda x: x.get("date", ""), reverse=reverse)
