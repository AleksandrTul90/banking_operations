"""Модуль для обработки банковских операций."""

from typing import Any, Dict, List


def filter_by_state(
    operations: List[Dict[str, Any]], state: str = 'EXECUTED'
) -> List[Dict[str, Any]]:
    """Фильтрует список операций по статусу."""
    return [
        operation for operation in operations
        if operation.get('state') == state
    ]


def sort_by_date(
    operations: List[Dict[str, Any]], reverse: bool = True
) -> List[Dict[str, Any]]:
    """Сортирует список операций по дате."""
    return sorted(
        operations, key=lambda x: x.get('date', ''), reverse=reverse
    )
