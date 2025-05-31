📱 sm_pr — Предсказание цен на смартфоны

📁 Структура проекта
sm_pr/
├── predictor_app/             # Основное приложение
│   ├── __init__.py
│   ├── models.py              # Определение моделей
│   ├── routes.py              # Маршруты приложения
│   └── templates/             # Шаблоны HTML
├── migrations/                # Миграции базы данных
├── mobile_price_model_job.pkl # Сериализованная модель
├── scaler.pkl                 # Сериализованный скейлер
├── alembic.ini                # Конфигурация Alembic
├── req.txt                    # Зависимости проекта
└── .env                       # Переменные окружения

🚀 Быстрый старт
Клонируй репозиторий:
git clone https://github.com/raiheeo/sm_pr.git
cd sm_pr
Создай виртуальное окружение и активируй его:
python -m venv venv
source venv/bin/activate  # Для Unix или MacOS
venv\Scripts\activate     # Для Windows

Установи зависимости:
pip install -r req.txt

⚙️ Используемые технологии
Языки программирования: Python
Фреймворки и библиотеки:
SQLAlchemy
Alembic
scikit-learn

📈 Описание модели
Модель машинного обучения обучена на датасете цен на смартфоны и способна предсказывать стоимость устройства на основе входных данных.
                                                       
