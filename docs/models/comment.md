# ITDpy

## Модель Comment

### Пример ответа Comment
```json
{
  "id": "d2602a73-c870-4951-ad53-187aaaefc944",
  "content": "Привет",
  "likesCount": 1,
  "repliesCount": 2,
  "isLiked": false,
  "createdAt": "2026-02-15 15:43:14.807675+03",
  "author": { ... },
  "attachments": [],
  "replies": []
}
```
### Поля объекта Comment

| Поле | Тип | Описание |
|------|-----|----------|
| id | str | ID комментария|
| content| str | Текст комментария |
| likes_count| int| Количество лайков |
| replies_count| int | Количество ответов |
| is_liked| bool| Лайкнул ли пользователь |
| created_at| str| Дата создания |
| author | [UserLite](users.md)| Автор|
| attachments| list| Медиа |
| reply_to|[UserLite](users.md)| Кому отвечает|
| replies| list[Comment] | Ответы |

## Пример использование:
```python
comments = client.get_comments(post_id="6f14ee05-e0c5-4133-8f42-aca16bde154c")

print("Всего комментариев:", len(comments))
print("-" * 50)

for comment in comments:
    print("ID:", comment.id)
    print("Текст:", comment.content)
    print("Создан:", comment.created_at)
    print("Лайков:", comment.likes_count)
    print("Ответов:", comment.replies_count)
    print("Лайкнут:", comment.is_liked)
    
    if comment.author:
        print("Автор ID:", comment.author.id)
        print("Автор username:", comment.author.username)
        print("Автор display:", comment.author.display_name)
        print("Автор verified:", comment.author.verified)
        
    if comment.attachments:
        print("Медиа:")
        for att in comment.attachments:
            print("  ID:", att.id)
            print("  Тип:", att.type_)
            print("  URL:", att.url)

    if comment.replies:
        print("\n  --- Ответы ---")
        for reply in comment.replies:
            print("  ID:", reply.id)
            print("  Текст:", reply.content)
            print("  Создан:", reply.created_at)
            print("  Лайков:", reply.likes_count)

            if reply.author:
                print("  Автор:", reply.author.username)

            if reply.reply_to:
                print("  Ответ пользователю:", reply.reply_to.username)
            print("  -----")

    print("=" * 50)
```

← [Назад к документации](../index.md)