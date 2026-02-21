# ITDpy

## Модели -   `UserLite`, `User`, `Me`, `Users`, `SuggestedUser`

## UserLite

> Базовая модель пользователя.   Используется в постах, комментариях,
> списках пользователей.

### Пример ответа UserLite
```json
{
  "id": "c44d69c2-d35a-4ec0-8128-8e59e41053ba",
  "username": "gam5510",
  "displayName": "Фазлиддин",
  "avatar": "👨‍💻",
  "verified": false,
  "isFollowing": false,
  "pin": {
    "slug": "kirill67_202602_infected",
    "name": "Переболел вирусом Кирилл-67",
    "description": "Вирус (Февраль, 2026г)"
  }
}
```
### Поля объекта UsterLite
|Поле| Тип | Описание|
|--|--|--|
|id|str|ID пользователя|
|username|str|юзернейм|
|display_name|str|Имя|
|avatar|str|Аватар emoji|
|verified|bool|Верифицирован ли|
|is_following|bool|Подписан ли текущий пользователь|
|pin|[Pin](pin.md)|Закреплённый значок|

## User

> Расширенная модель пользователя.   
> Наследуется от `UserLite`.

Используется при получении полного профиля пользователя.
### Дополнительные поля user
|Поле| Тип | Описание|
|--|--|--|
|banner|str|Баннер профиля|
|bio|str|Описание профиля|
|pinned_post_id|str|ID закреплённого поста|
|wall_access|str|Приватность стены|
|likes_visibility|str|Видимость лайков|
|followers_count|int|Подписчики|
|following_count|int|Подписки|
|posts_count|int|Количество постов|
|created_at|str|Дата регистрации|
|online|bool|Онлайн ли|
|last_seen|str|Последний вход|

## Me

> Модель текущего пользователя.   
> Наследуется от `User`.
> 
|Поле| Тип | Описание|
|--|--|--|
|is_private|bool|Закрыт ли профиль|

## Users

> Модель списка пользователей. Используется при поиске или получении
> списка подписчиков.

### Пример ответа Users
```json
{
  "data": {
    "users": [
      {
        "id": "1",
        "username": "user1",
        "displayName": "User 1",
        "avatar": "🙂"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 100,
      "hasMore": true
    }
  }
}
```
| Поле | Тип | 
|------|-----|
|data.users|list[users]|
|data.pagination|[Pagination](pagination.md)|

## Модель SuggestedUser

| Поле | Тип | Описание |
|--|--|--|
|id|str|ID пользователя|
|username|str|Username|
|display_name|str|Отображаемое имя|
|avatar|str|Аватар|
|verified|bool|Верифицирован ли|
|followers_count|int|Количество подписчиков|

← [Назад к документации](index.md)