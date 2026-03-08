# ITDpy

## Comments

Модуль `comments` позволяет:
-   получать комментарии    
-   создавать комментарии    
-   отвечать на комментарии    
-   удалять комментарии
-   ставить лайки
-   получать ответы (replies)

## Получить список комментариев
```python
client.get_comments(post_id, limit=20, sort="popular")
```
### Параметры:

- post_id — ID поста
- limit — сколько комментариев вернуть (от 20 до 500)
- sort — сортировка:
	 - "popular" 
	 - "newest" 
	 - "oldest"

Возвращает модель Comments [подробнее](models/comments.md)

## Получить ответы на комментарий
```python
client.get_replies(comment_id, sort="newest")
```
### Параметры:

-   `comment_id` — ID комментария
-   `sort` — сортировка:
    -   `"popular"`     
    -   `"newest"`     
    -   `"oldest"`
        
Возвращает модель Comments [подробнее](models/comments.md)

## Получить ответы на комментарий
```python
client.get_replies(comment_id, sort="newest") 
```
### Параметры:

-   `comment_id` — ID комментария
-   `sort` — сортировка:
    -   `"popular"`
    -   `"newest"`
    -   `"oldest"`
        
Возвращает модель Comments [подробнее](models/comments.md)

## Создать комментарий
```python
client.create_comment(post_id="post_id", content="Отличный пост!" )
```
### Параметры:

-   `post_id` — ID поста
-   `content` — текст комментария
-   `attachment_ids` — список ID медиа файлов [Загрузка файлов](upload.md)

Возвращает модель Comment [подробнее](models/comment.md)

## Ответить на комментарий
```python
client.reply_to_comment(comment_id="comment_id", content="Спасибо!") 
```
### Параметры:

-   `comment_id` — ID комментария
-   `content` — текст ответа
-   `attachment_ids` — список ID медиа файлов [Загрузка файлов](upload.md)
    
Возвращает модель Comment [подробнее](models/comment.md)

## Удалить комментарий
```python
client.delete_comment(comment_id) 
```
Возвращает `True`, если удалён успешно.

## Реакции
```python
client.like_comment(comment_id) # поставить лайк 
client.unlike_comment(comment_id) # убрать лайк 
```
Возвращает `True` при успехе.

← [Назад к документации](index.md)