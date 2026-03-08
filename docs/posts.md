# ITDpy
## Posts
Модуль `posts` позволяет:
-   получать посты
-   создавать посты
-   обновлять посты
-   удалять посты
-   ставить лайки
-   делать репосты

## Получить список постов

```python
client.get_posts(limit=20, tab="popular")
```
### Параметры:

-   `limit` — сколько постов вернуть (от 20 до 50)
-   `tab` — сортировка:
    
    -   `"popular"`
    -   `"newest"`
    -   `"oldest"`
        
Возвращает модель `Posts` [Подробнее](models/posts.md).

## Получить один пост
```python
client.get_post(post_id) 
```
Возвращает модель `Post` [Подробнее](models/post.md).

## Создать пост
```python
client.create_post(content="Привет!") 
```
### Параметры:

-   `content` — текст поста
-   `attachment_ids` — список ID медиа файлов [Загрузка файлов](upload.md)
-   `wall_recipient_id` — если пост на стену другого пользователя
-   `poll` — опрос [Структура опроса](models/poll.md)
-   `parse_html=True` — включить HTML форматирование [HTML форматирование](formatting.md)

### Пример с HTML
```python
client.create_post(content="Обновление <b>ITDpy</b>", parse_html=True )
 ```
 
 ### Пример с опросом
```python
client.create_post(
    content="Голосование",
    poll={ "question": "Лучший язык?", "options": ["Python", "Go"]}
)
```
## Обновить пост
```python
client.update_post(post_id, "Новый текст")
```
Возвращает `PostUpdate`, [Модель PostUpdate](models/posts.md).

## Удалить пост
```python
client.delete_post(post_id)
```
Возвращает `True`, если удалён успешно.

## Реакции
```python
client.like_post(post_id) # поставить лайк
client.unlike_post(post_id) # убрать лайк
```
Возвращает `True` при успехе.

## Репост
```python
client.repost_post(post_id, content="Мой комментарий")
```
Возвращает `True` при успехе

## Получить посты пользователя
```python
client.get_user_posts("username")
```
Возвращает модель `Posts` [Подробнее](models/posts.md).

← [Назад к документации](index.md)