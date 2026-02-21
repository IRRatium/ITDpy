# ITDpy
## Модель post

### Пример ответа post
```json
{
"id": "1e919573-cb93-42c6-b9c1-7d35d9484d9e",
"content": "Python клиент для API ИТД.com\n\nУдобные модели, refresh токена, кастомные запросы.\nПодходит для ботов и автоматизаций.\n\nhttps://github.com/Gam5510/ITDpy\n\nЭТО НЕ ОФИЦИАЛЬНЫЙ API  \n#api #python #sdk",
"spans": [
{
	"tag": "api",
	"type": "hashtag",
	"length": 4,
	"offset": 178
},
{
	"tag": "python",
	"type": "hashtag",
	"length": 7,
	"offset": 183
},
{
	"tag": "sdk",
	"type": "hashtag",
	"length": 4,
	"offset": 191
}],
"author": {
		"id": "c44d69c2-d35a-4ec0-8128-8e59e41053ba",
		"username": "gam5510",
		"displayName": "Фазлиддин",
		"avatar": "👨‍💻",
		"verified": false,
		"pin": {
				"slug": "kirill67_202602_infected",
				"name": "Переболел вирусом Кирилл-67",
				"description": "Вирус (Февраль, 2026г)"
		}
},
"attachments": [],
"likesCount": 8,
"commentsCount": 0,
"repostsCount": 2,
"viewsCount": 40,
"isLiked": true,
"isViewed": true,
"isReposted": false,
"isOwner": true,
"createdAt": "2026-01-31T06:20:32.245Z",
"originalPost": null,
"wallRecipientId": null,
"wallRecipient": null,
"poll": null,
"isPinned": true
},
```
### Поля объекта Post
| Поле | Тип | Описание |
|------|-----|----------|
| id | str | ID поста|
| content| str | Текст поста |
| spans | list[Span] | Форматирование (bold, hashtag и т.д.) |
| likes_count | int | Количество лайков |
| comments_count | int |Количество комментариев|
| reposts_count | int | Количество репостов |
| views_count| int | Количество просмотров |
| is_liked| bool | Лайкнул ли текущий пользователь|
| is_owner| bool| Является ли пользователь владельцем |
| is_pinned | bool | Закреплён ли пост |
| author | [UserLite](user.md)| Автор поста|
| poll | [poll](poll.md)| Опрос (если есть)|

## Пример вывода всех значений

Теперь код, который красиво выводит всё:
```python
post = client.get_post("1e919573-cb93-42c6-b9c1-7d35d9484d9e")

print("ID:", post.id)
print("Текст:", post.content)
print("Создан:", post.created_at)

print("Лайки:", post.likes_count)
print("Комментарии:", post.comments_count)
print("Репосты:", post.reposts_count)
print("Просмотры:", post.views_count)

print("Лайкнут:", post.is_liked)
print("Просмотрен:", post.is_viewed)
print("Репостнут:", post.is_reposted)
print("Владелец:", post.is_owner)
print("Закреплён:", post.is_pinned)

if post.author:
    print("\nАвтор:")
    print("  ID:", post.author.id)
    print("  Username:", post.author.username)
    print("  Display name:", post.author.display_name)
    print("  Verified:", post.author.verified)

if  post.author.pin:
		print("\nПин:")
		print(" Сленг: ",  post.author.pin.slug)
		print(" Название: ",  post.author.pin.name)
		print(" Описание: ",  post.author.pin.description)

if post.spans:
    print("\nSpans:")
    for span in post.spans:
        print(f"  Тип: {span.type}, Offset: {span.offset}, Length: {span.length}, Tag: {span.tag}")

if post.attachments:
    print("\nМедиа:")
    for attachment in post.attachments:
        print("  ID:", attachment.id)

if post.poll:
    print("\nОпрос:")
    print("  Вопрос:", post.poll.question)
    print("  Всего голосов:", post.poll.total_votes)
    print("  Проголосовал:", post.poll.has_voted)

    for option in post.poll.options:
        print(f"	Вариант: {option.text} (голосов: {option.votes_count})")
```

← [Назад к документации](index.md)