# ITDpy

Python SDK для социальной сети итд.com.
> ⚠️ Неофициальный API-клиент.  
>SDK предназначен для разработки клиентских приложений и тестирования API в рамках действующих правил платформы.

## Установка pip
```bash
pip install itdpy
```

### Через git

```bash
git clone https://github.com/Gam5510/ITDpy
cd itdpy
pip install -r requirements.txt
pip install -e .
```

## Документация  

- [Документация](documentation/index.md)  
- [Быстрый старт](documentation/quickstart.md)  
- [Навигация](documentation/NAVIGATION.md)
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


## Быстрый старт

> Blockquote ![Получение токена](https://i.ibb.co/DH1m8GL7/Assistant.png)
Как получить токен

```python
from  itdpy.client  import  ITDClient

client  =  ITDClient(refresh_token="Ваш refresh token")

me  =  client.get_me()
print(me.id)
print(me.username)
```

### Скрипт на обновление имени

```python
from  itdpy.client  import  ITDClient
from  datetime  import  datetime
import  time

client = ITDClient(refresh_token="Ваш_токен")

while  True:
	client.update_profile(display_name=f"Фазлиддин |{datetime.now().strftime('%m.%d %H:%M:%S')}|")
	time.sleep(1)
```

### Скрипт на обновление баннера 
```python
from  itdpy.client  import  ITDClient

client  =  ITDClient(refresh_token="Ваш_токен")

file  =  client.upload_file(client,  "matrix-rain-effect-animation-photoshop-editor.gif")
print(file.id)
update  =  update_profile(client,  banner_id=file.id)
print(update.banner)
```

# Костомные запросы  

## ✅ Базовый пример кастомного GET
```python
response = client.get("/api/users/me")
data = response.json() 
print(data)
```
### Можно добавить любой эндпоинт
----------

## ✅ POST с JSON
```python
response = client.post( 
		"/api/posts",
    json={ "content": "Привет из кастомного запроса" }
) 
print(response.status_code) 
print(response.json())
```
----------

## ✅ PUT / PATCH
```python
response = client.patch( "/api/profile",
    json={ "displayName": "Фазлиддин 😎" }
)
```
----------

## ✅ DELETE
```python
client.delete("/api/posts/POST_ID") 
```
----------

## ✅ Передача query-параметров
```python
response = client.get( "/api/posts",
    params={ "limit": 50, "sort": "popular" }
)
```

## Планы

- Асинхронная версия библиотеки (`aioitd`)
- Улучшенная обработка и форматирование ошибок
- Логирование (через `logging`)
- Расширение объектной модели (Post, Comment, User и др.)
- Дополнительные API-эндпоинты по мере появления
- Улучшение документации и примеров


## Прочее

Проект активно развивается.
Если у вас есть идеи или предложения — создавайте issue или pull request.