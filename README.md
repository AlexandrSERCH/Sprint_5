# Sprint_5

## Автоматизированные E2E тесты для учебного сервиса «Доска»
### Реализованные тест-кейсы:
- Регистрация пользователя
- Регистрация пользователя c email не по маске  *****@\*****.\*****
- Регистрация уже существующего пользователя
- Login пользователя
- Logout пользователя
- Создание объявления неавторизованным пользователем
- Создание объявления авторизованным пользователем

## Инструменты:
- pytest
- selenium
- faker

## Запуск автотестов
1. Установить зависимости:
`pip install -r requirements.txt`
2. Запустить тесты
`pytest`



### Результаты прогона
===== short test summary info ===== 
FAILED tests/test_login_user.py::TestLoginUser::test_login_user - AssertionError: assert 'https://qa-d...-services.ru/' == 'https://qa-d...ices.ru/login'
FAILED tests/test_register_user.py::TestRegisterUser::test_register_user - AssertionError: assert 'https://qa-d...-services.ru/' == 'https://qa-d.../regiatration'
===== 2 failed, 5 passed in 65.23s (0:01:05) ======