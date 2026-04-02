# Banking Operations Widget

Проект для управления и анализа банковских операций клиента.

## 📋 Описание

Этот проект предоставляет функции для обработки данных о банковских операциях, включая фильтрацию по статусу и сортировку по датам. Проект разработан с соблюдением лучших практик Python и PEP 8.

## 🎯 Функциональность

### Функция `filter_by_state`

Фильтрует список операций по статусу.

```python
from src.processing.operations import filter_by_state

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
]

# Получить все выполненные операции (по умолчанию)
executed = filter_by_state(data)
# Результат: 2 операции со статусом 'EXECUTED'

# Получить все отменённые операции
canceled = filter_by_state(data, 'CANCELED')
# Результат: 2 операции со статусом 'CANCELED'
```

**Параметры:**
- `operations` (List[Dict[str, Any]]): Список словарей с данными о операциях
- `state` (str): Статус для фильтрации, по умолчанию `'EXECUTED'`

**Возвращает:**
- List[Dict[str, Any]]: Новый список отфильтрованных операций

### Функция `sort_by_date`

Сортирует список операций по дате.

```python
from src.processing.operations import sort_by_date

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
]

# Сортировка по убыванию (новые операции в начале)
sorted_desc = sort_by_date(data)
# Результат: операции отсортированы от новых к старым

# Сортировка по возрастанию (старые операции в начале)
sorted_asc = sort_by_date(data, False)
# Результат: операции отсортированы от старых к новым
```

**Параметры:**
- `operations` (List[Dict[str, Any]]): Список словарей с данными о операциях
- `reverse` (bool): Порядок сортировки, по умолчанию `True` (убывание)

**Возвращает:**
- List[Dict[str, Any]]: Новый список отсортированных операций

## 💻 Установка

### Требования
- Python 3.9+
- pip

### Шаги установки

1. Клонируйте репозиторий:
```bash
git clone https://github.com/AleksandrTul90/banking_operations.git
cd banking_operations
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate
```

3. Установите зависимости для разработки:
```bash
pip install pytest mypy flake8 isort black
```

## 🧪 Тестирование

Запустите тесты:

```bash
pytest tests/ -v
```

## 🔍 Проверка кода

### Проверка типов (mypy)
```bash
mypy src/
```

### Проверка стиля (flake8)
```bash
flake8 src/ tests/
```

### Сортировка импортов (isort)
```bash
isort src/ tests/
```

## 📁 Структура проекта

```
banking_operations/
├── .git/                  # Git репозиторий
├── .gitignore            # Файл для игнорирования файлов
├── README.md             # Документация проекта
├── src/
│   ├── __init__.py
│   └── processing/
│       ├── __init__.py
│       └── operations.py # Функции обработки операций
└── tests/
    ├── __init__.py
    └── test_operations.py # Тесты
```

## 🔀 GitFlow

Проект использует GitFlow для управления версиями:

- **main** - основная ветка с финальной версией проекта
- **develop** - ветка для разработки
- **feature/** - ветки для новых функций

### Процесс разработки

1. Создайте ветку для функции:
```bash
git checkout -b feature/your-feature develop
```

2. Внесите изменения и создайте коммиты:
```bash
git add .
git commit -m "feat: description of your feature"
```

3. Отправьте на GitHub:
```bash
git push origin feature/your-feature
```

4. Создайте Pull Request из feature ветки в develop

## 📝 Примеры использования

### Комбинированное использование

```python
from src.processing.operations import filter_by_state, sort_by_date

data = [...]

# Получить выполненные операции, отсортированные по дате (новые первыми)
executed_sorted = sort_by_date(filter_by_state(data))

# Получить отменённые операции, отсортированные по дате (старые первыми)
canceled_sorted = sort_by_date(filter_by_state(data, 'CANCELED'), False)
```

## 👨‍💻 Автор

**AleksandrTul90**

## 📄 Лицензия

MIT License

## 🤝 Вклад

Приветствуются Pull Requests! Пожалуйста, сначала создайте issue для обсуждения предлага��мых изменений.