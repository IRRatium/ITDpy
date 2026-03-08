
# ITDpy

## Модель poll (Опросов)

### Пример ответа Poll
```json
"poll": {
"id": "884e9f83-46bd-4503-9638-3cb7e104eae6",
"postId": "687c8557-ddb5-442c-99f0-a28dd7b307ef",
"question": "Лучший язык?",
"multipleChoice": false,
"options": [
 {
	"id": "757928a6-ddf2-45ca-b555-69acd69e7898",
	"text": "Python",
	"position": 0,
	 "votesCount": 13
},
{
	"id": "0a82eb2a-3ce0-41ed-86af-9b59fa3cb571",
	"text": "Go",
	"position": 1,
	"votesCount": 1
},
{
	"id": "f35fdfeb-ea73-4dc6-86df-f97aa2e33d75",
	"text": "Rust",
	"position": 2,
	"votesCount": 2
},
{
	"id": "1d4169ad-c51c-4622-ac1e-8573eb1b3408",
	"text": "JS",
	"position": 3,
	"votesCount": 1
}
],
"totalVotes": 17,
"hasVoted": true,
"votedOptionIds": ["757928a6-ddf2-45ca-b555-69acd69e7898"],
"createdAt": "2026-02-15 09:27:07.272285+03"
}
```

### Поля объекта Poll

| Поле | Тип | Описание |
|------|-----|----------|
| id | str | ID опроса |
| postId | str | ID поста |
| question | str | Вопрос |
| multipleChoice | bool | Можно выбрать несколько вариантов |
| options | list | Список вариантов |
| totalVotes | int | Общее количество голосов |
| hasVoted | bool | Проголосовал ли текущий пользователь |
| votedOptionIds | list[str] | ID выбранных вариантов |
| createdAt| str | Дата создания опроса|

### Поля объекта PollOption

| Поле | Тип | Описание |
|------|-----|----------|
| id | str | ID варианта |
| text | str | Текст варианта |
| position | int | Позиция в списке |
| votes_count | int | Количество голосов |


## Пример использование:
```python
post = client.get_post("687c8557-ddb5-442c-99f0-a28dd7b307ef")

if post.poll:
    print("\n--- Опрос ---")
    print("ID опроса:", post.poll.id)
    print("ID поста:", post.poll.post_id)
    print("Вопрос:", post.poll.question)
    print("Можно несколько:", post.poll.multiple_choice)
    print("Всего голосов:", post.poll.total_votes)
    print("Вы голосовали:", post.poll.has_voted)
    print("Выбрали варианты:", post.poll.voted_option_ids)
    print("Создан:", post.poll.created_at)

    print("\nВарианты:")
    for option in post.poll.options:
        print("  ID:", option.id)
        print("  Текст:", option.text)
        print("  Позиция:", option.position)
        print("  Голосов:", option.votes_count)
        print("---")
```

← [Назад к документации](../index.md)