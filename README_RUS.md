# Zero-Complex Приложение погоды
- Приложение докеризовано (Можно установку и запуск пропустить)
- Последние места сохраняются
- Также подсказки и автодополнение

В этом проекте я использовал Django 5 и Python, также представлен файл Readme на английском языке.

# Установка & Запуск
- Установить python
- Создать виртуальную среду (venv):
```
python3 - Linux/macOS
python - Windows NT
pip3 - Linux/macOS
pip - Windows NT
```
```
python -m venv venv
```
- Активировать виртуальную среду (venv) - Windows:
```
venv/Scripts/activate 
```
- Активировать виртуальную среду (venv) - Linux / GNU / BSD / Unix / macOS:
```
source venv/bin/activate
```
- Дальше по инструкции:
```
pip install -r requirements.txt
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py runserver
```
- Остановка сервера
```
CTRL + C
```

## Лиценщия

Лицензировано под лицензией:

* MIT license (https://opensource.org/license/mit)

## Целеввые ОС

- Windows NT 10/11
- GNU/Linux - Дистрибутивы
- BSD/Mach - macOS
