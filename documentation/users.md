# ITDpy

## Users

Модуль `users` позволяет:

-   получать текущего пользователя
-   получать профиль по username
-   подписываться / отписываться
-   получать список подписчиков
-   получать список подписок
    
----------

## Получить текущего пользователя
```python
client.get_me()
```

Возвращает модель `Me`  [подробнее](models/user)

### Пример:
```python
me  =  client.get_me()  
  
print("ID:", me.id)  
print("Username:", me.username)  
print("Имя:", me.display_name)  
print("Подписчиков:", me.followers_count)  
print("Приватный профиль:", me.is_private)
```
----------

## Получить пользователя по username
```python
client.get_user("gam5510")
```
### Параметры:

-   `username` — username пользователя

Возвращает модель `User`  [подробнее](models/users)

### Пример:
```python
user  =  client.get_user("gam5510")  
  
print("Имя:", user.display_name)  
print("Bio:", user.bio)  
print("Подписчиков:", user.followers_count)  
print("Онлайн:", user.online)
```
----------

## Подписаться на пользователя
```python
client.follow_user("gam5510")
```
### Параметры:

-   `username` — username пользователя
    
Возвращает `True`, если операция выполнена успешно.

### Пример:
```python
success  =  client.follow_user("gam5510")  
  
if  success:  
  print("Вы подписались на пользователя.")
```
----------

## Отписаться от пользователя
```python
client.unfollow_user("gam5510")
```
### Параметры:

-   `username` — username пользователя
    
Возвращает `True`, если операция выполнена успешно.

----------

## Получить подписчиков
```python
client.get_followers("gam5510", page=1, limit=30)
```

### Параметры:

-   `username` — username пользователя
-   `page` — номер страницы
-   `limit` — количество пользователей на странице
    

Возвращает модель `Users`  [подробнее](models/users)

### Пример:
```python
followers  =  client.get_followers("gam5510",  page=1,  limit=10)

for  user  in  followers.users:
	print(f"{user.avatar} @{user.username}")
```
----------

## Получить подписки 
```
client.get_following("gam5510", page=1, limit=30)
```
### Параметры:

-   `username` — username пользователя
-   `page` — номер страницы
-   `limit` — количество пользователей на странице
   
Возвращает модель `Users`  [подробнее](models/users)

### Пример:
```python
following  =  client.get_following("gam5510")  
  
for  user  in  following.users:  
  print(f"{user.avatar} @{user.display_name}")
```
----------

## Особенности

-   Методы `follow_user` и `unfollow_user` возвращают `True` при успешном выполнении.
-   Методы `get_followers` и `get_following` поддерживают пагинацию.

  
← [Назад к документации](index.md)
