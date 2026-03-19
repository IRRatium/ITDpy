# itdirr

## Portal

Модуль `portal` позволяет:

- получать информацию о текущем ивенте на платформе
- получать ссылку для верификации аккаунта через Telegram

----------

## Получить текущий ивент

```python
client.get_portal()
```

Возвращает модель `Portal` [подробнее](models/portal.md)

### Пример

```python
portal = client.get_portal()

if portal.active:
    print("Идёт ивент:", portal.title)
    print("Ссылка:", portal.url)
else:
    print("Активных ивентов нет")
```

----------

## Получить ссылку для верификации

```python
client.get_verification_link()
```

Возвращает строку с ссылкой на Telegram-бота для верификации аккаунта.

### Пример

```python
link = client.get_verification_link()
print("Верифицируй аккаунт:", link)
# https://t.me/itd_verification_bot?start=ваш-user-id
```

----------

## Автоматическая обработка ошибки верификации

Если аккаунт не верифицирован, при любом действии (создание поста, комментария и т.д.) автоматически выбрасывается исключение `NotVerifiedException` со ссылкой на верификацию.

```python
from itdpy import ITDClient, NotVerifiedException

client = ITDClient(refresh_token="...")

try:
    client.create_post("Привет!")
except NotVerifiedException as e:
    print(e)
    # Аккаунт не верифицирован. Подтвердите через Telegram: https://t.me/...

    print(e.verification_link)  # только ссылка
    print(e.user_id)            # ваш user id
```

← [Назад к документации](index.md)
