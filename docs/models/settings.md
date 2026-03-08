# ITDpy

# Модели `PrivacySettings`, `NotificationSettings`

## Модель `PrivacySettings`

### Пример ответа `PrivacySettings`
```json
{
    "isPrivate": true,
    "wallAccess": "mutual",
    "likesVisibility": "everyone",
    "showLastSeen": false
}
```
### Поля 
|Поле | Тип | Описание |
|--|--|--|
|is_private |bool|Закрыт ли профиль|
|wall_access|str|Кто может писать на стене|
|likes_visibility|str|Кто видит лайки|
|show_last_seen|bool|Показывать ли время последнего входа|

### Возможные значения `wall_access` и `likes_visibility`
|Значение|Описание|
|--|--|
|`everyone`|Все пользователи|
|`followers`|Только подписчики|
|`mutual`|Взаимные подписки|
|`nobody`|Никто|

## Модель `NotificationSettings`

### Пример ответа `NotificationSettings`
```json
{
    "enabled": true,
    "sound": true,
    "follows": true,
    "wallPosts": true,
    "likes": true,
    "comments": true,
    "mentions": true
}
```
### Поля 
| Поле | Тип | Описание |
|--|--|--|
|enabled|bool|Включены ли уведомления|
|comments|bool|Уведомления о комментариях|
|follows|bool|Уведомления о подписках|
|likes|bool|Уведомления о лайках|
|mentions|bool|Уведомления об упоминаниях|
|sound|bool|Воспроизводить звук|
|wall_posts|bool|Уведомления о постах на стене|

← [Назад к документации](../index.md)