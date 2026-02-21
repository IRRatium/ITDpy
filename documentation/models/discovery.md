# ITDpy

## Модели Discovery

## Hashtag
| Поле | Тип | Описание |
|--|--|--|
|id|str|ID хештега|
|name|str|Название|
|posts_count|int|Количество постов|

## HashtagPosts
| Поле | Тип | Описание |
|--|--|--|
|hashtag|Hashtag|Модель `Hashtag`|
|posts|list[[Post](post.md)]|Список постов|
|pagination|[Pagination](pagination.md)|Пагинация|

## TrendingHashtagsResponse
| Поле | Тип | Описание |
|--|--|--|
|hashtags|list[Hashtag]|Список популярных хештегов|

← [Назад к документации](index.md)