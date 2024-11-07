# Ипотечный калькулятор


Это серверное приложение на Flask для управления ипотечным калькулятором. Оно предоставляет функции аутентификации и управления пользователями через структурированные конечные точки, организованные контроллеры и масштабируемую архитектуру.


## Возможности
- Аутентификация пользователей (`/auth`)
- Управление пользователями (`/user`)
- Легкая масштабируемость для добавления новых сервисов

## Установка

### Шаги
1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/holodae/server-mortgage.git
    cd server-mortgage
    ```

2. Создайте виртуальное окружение:
    ```bash
    python -m venv venv
    ```

3. Активируйте виртуальное окружение:
    - **Windows**:
      ```bash
      source venv/Scripts/activate
      ```

      ```CMD
      .\venv\Scripts\activate.bat
      ```

    - **MacOS/Linux**:
      ```bash
      source venv/bin/activate
      ```

4. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    pip install flask
    pip install flask-cors
    ```

5. Настройте переменные окружения. Создайте файл `.env` в корне проекта и добавьте следующие переменные:
    ```plaintext
    FLASK_APP=main.py
    FLASK_ENV=development
    DATABASE_URL=ваш_адрес_базы_данных
    SECRET_KEY=ваш_секретный_ключ
    ```

6. Инициализируйте базу данных:
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

## Использование

1. Запустите приложение:
    ```bash
    python main.py
    ```

2. Откройте конечные точки:
    - Аутентификация пользователя: `http://localhost:5000/auth`
    - Управление пользователем: `http://localhost:5000/user`

## Лицензия
Проект распространяется под лицензией MIT. Подробности смотрите в файл [LICENSE]