# ITDpy

Python SDK для работы с API итд.com.

>SDK предназначен для разработки клиентских приложений и тестирования API в рамках действующих правил платформы.

# Навигация 
## Основное  
- [Главная](index.md)  
- [Быстрый старт](quickstart.md)  
  
---
  
## Модули  
  
- [Clans](documentation/clans.md)
- [Comments](documentation/comments.md)
- [Discovery](documentation/discovery.md)  
- [Formatting](documentation/formatting.md)  
- [Notifications](documentation/notifications.md)
- [Pins](documentation/pins.md) 
- [Polls](documentation/polls.md)  
- [Posts](documentation/posts.md) 
- [Profile](documentation/profile.md) 
- [Settings](documentation/settings.md)
- [Upload](documentation/upload.md)
- [Users](documentation/users.md)   
  
  
---  
  
## Модели  

- [Actor](documentation/models/actor.md)
- [Comment](documentation/models/comment.md)  
- [Comments](documentation/models/comments.md)
- [Discovery](documentation/models/discovery.md)
- [Notification](documentation/models/notification.md)
- [Notifications](documentation/models/notifications.md)
- [Pagination](documentation/models/pagination.md)  
- [Pins](documentation/models/pins.md) 
- [Poll](documentation/models/poll.md)  
- [Post](documentation/models/post.md)  
- [Posts](documentation/models/posts.md)  
- [Settings](documentation/models/settings.md)
- [Users](documentation/models/users.md)  

## Назначение

ITDpy предоставляет удобную Python-обёртку над API итд.com и позволяет:

-   интегрировать функциональность сайта в собственные приложения
-   разрабатывать пользовательские интерфейсы
-   создавать экспериментальные и учебные проекты
-   расширять функциональность платформы в рамках API
    
SDK не модифицирует поведение сервера и использует только официальные API-эндпоинты.

## Возможности

-   Работа с постами, комментариями и опросами
-   Получение статистики 
-   Управление профилем и настройками
-   Поиск пользователей и хештегов
-   Typed Pydantic-модели
-   Строгая типизация и валидация данных
-   Загружать файлы 
-   HTML форматирование текста

## Пример использования
```python
from  itdpy  import  ITDClient  
  
client  =  ITDClient(refresh_token="your_refresh_token")  

me  =  client.get_me()  
print(me.username)
```
## Архитектура

-   Python 3.11+
-   Pydantic v2
-   CamelCase → snake_case
-   Чистая модульная структура

