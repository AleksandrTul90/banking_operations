"""Тесты для модуля обработки операций."""

from src.processing.operations import filter_by_state, sort_by_date


TEST_DATA = [
    {
        'id': 41428829,
        'state': 'EXECUTED',
        'date': '2019-07-03T18:35:29.512364'
    },
    {
        'id': 939719570,
        'state': 'EXECUTED',
        'date': '2018-06-30T02:08:58.425572'
    },
    {
        'id': 594226727,
        'state': 'CANCELED',
        'date': '2018-09-12T21:27:25.241689'
    },
    {
        'id': 615064591,
        'state': 'CANCELED',
        'date': '2018-10-14T08:21:33.419441'
    },
]


class TestFilterByState:
    """Тесты для функции filter_by_state."""

    def test_filter_by_state_default(self) -> None:
        """Тест фильтрации со статусом по умолчанию."""
        result = filter_by_state(TEST_DATA)
        assert len(result) == 2
        assert all(op['state'] == 'EXECUTED' for op in result)

    def test_filter_by_state_canceled(self) -> None:
        """Тест фильтрации по статусу CANCELED."""
        result = filter_by_state(TEST_DATA, 'CANCELED')
        assert len(result) == 2
        assert all(op['state'] == 'CANCELED' for op in result)

    def test_filter_by_state_empty(self) -> None:
        """Тест фильтрации при пустом результате."""
        result = filter_by_state(TEST_DATA, 'PENDING')
        assert len(result) == 0


class TestSortByDate:
    """Тесты для функции sort_by_date."""

    def test_sort_by_date_descending(self) -> None:
        """Тест сортировки по убыванию (по умолчанию)."""
        result = sort_by_date(TEST_DATA)
        assert result[0]['date'] == '2019-07-03T18:35:29.512364'
        assert result[-1]['date'] == '2018-06-30T02:08:58.425572'

    def test_sort_by_date_ascending(self) -> None:
        """Тест сортировки по возрастанию."""
        result = sort_by_date(TEST_DATA, False)
        assert result[0]['date'] == '2018-06-30T02:08:58.425572'
        assert result[-1]['date'] == '2019-07-03T18:35:29.512364'

    def test_sort_by_date_preserves_data(self) -> None:
        """Тест сохранения целостности данных."""
        result = sort_by_date(TEST_DATA)
        assert len(result) == len(TEST_DATA)
        assert set(op['id'] for op in result) == set(
            op['id'] for op in TEST_DATA
        )
