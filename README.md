# FastApiMessage
Простой мессенджер на FastAPI с  использованием типизации данных.

## Настройка
Приведено для PyCharm Windows
1. Клонировать
2. Создать виртуальное окружение
3. Установить зависимости

## Запуск приложения
1. Нажать зеленую стрелку у строки if __name__ == '__main__':
2. Открыть браузер и перейти по адресу `http://127.0.0.1:8000/docs`, 
чтобы увидеть документацию Swagger.

## Эндпоинты
### Регистрация пользователя

- **POST** `/register/`
- Тело запроса: `{ "name": "John Doe", "email": "john@example.com" }`

### Отправка сообщения

- **POST** `/send/`
- Тело запроса: `{ "sender": "john@example.com", "receiver": "jane@example.com", "content": "Hello!" }`

### Получение сообщений

- **GET** `/messages/{email}`
- Параметр пути: `email` (строка)