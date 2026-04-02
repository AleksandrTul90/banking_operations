"""Конфигурация для pytest."""

import sys
from pathlib import Path

# Добавляем корневую папку проекта в путь Python
sys.path.insert(0, str(Path(__file__).parent.parent))
