# itdirr

## Posts

Модуль `posts` позволяет:

- получать посты
- создавать посты
- обновлять посты
- удалять посты
- ставить лайки
- делать репосты
- просматривать посты

----------

## Получить список постов

```python
client.get_posts(limit=20, tab="popular")
```

### Параметры

- `limit` — количество постов (от 20 до 50)
- `tab` — сортировка: `"popular"` / `"newest"` / `"oldest"`
- `cursor` — курсор пагинации

Возвращает модель `Posts` [подробнее](models/posts.md)

----------

## Получить один пост

```python
post = client.get_post(post_id)

print("Лайков:",      post.likes_count)
print("Просмотров:",  post.views_count)
print("Комментариев:", post.comments_count)
print("Репостов:",    post.reposts_count)
```

Возвращает модель `Post` [подробнее](models/post.md)

----------

## Создать пост

```python
post = client.create_post("Привет!")
```

### Параметры

- `content` — текст поста
- `attachment_ids` — список ID медиафайлов
- `wall_recipient_id` — ID пользователя для поста на стену
- `poll` — опрос
- `parse_html=True` — HTML форматирование

### С HTML

```python
post = client.create_post("<b>Жирный</b> и <i>курсив</i>", parse_html=True)
```

### С опросом

```python
post = client.create_post(
    content="Голосуем!",
    poll={"question": "Лучший язык?", "options": ["Python", "Go", "Rust"]}
)
```

### С медиафайлом

```python
file = client.upload_file("photo.jpg")
post = client.create_post("Фото!", attachment_ids=[file.id])
```

----------

## Обновить пост

```python
client.update_post(post_id, "Новый текст")
```

----------

## Удалить пост

```python
client.delete_post(post_id)  # True при успехе
```

----------

## Реакции

```python
client.like_post(post_id)    # лайк
client.unlike_post(post_id)  # убрать лайк
```

----------

## Репост

```python
# content обязателен — API не принимает пустую строку
client.repost_post(post_id, content="Мой комментарий")
```

----------

## Просмотр

```python
client.view_post(post_id)                    # один пост
client.view_posts([id1, id2, id3])           # несколько
```

----------

## Посты пользователя

```python
posts = client.get_user_posts("gam5510", limit=20, sort="new")
```

----------

## Пример

```python
posts = client.get_posts(limit=20, tab="popular")

print("Всего:", len(posts))
for post in posts:
    print(f"@{post.author.username}: {post.content[:50]}")
    print(f"  ❤️ {post.likes_count}  👁 {post.views_count}  💬 {post.comments_count}")
```

← [Назад к документации](index.md)