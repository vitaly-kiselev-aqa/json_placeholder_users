# Настройка среды разработки

1. Создайте виртуальную среду Python

    ```shell
    python3 -m venv venv
    ```

2. Активируйте виртуальную среду

    ```shell
    source venv/bin/activate
    ```

3. Установите зависимости

    ```shell
    pip install -r requirements.txt
    ```

4. Запустите тесты

    ```shell
    pytest
    ```

# Линтер

* Проверка форматирования

    ```shell
    ruff format --check
    ```

* Линтер

    ```shell
    ruff check
    ```
