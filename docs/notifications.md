# itdirr

## Notifications

Модуль `notifications` позволяет:

- получать список уведомлений
- отмечать уведомление как прочитанное
- отмечать все уведомления как прочитанные

----------

## Получить список уведомлений

```python
client.get_notifications(offset=0, limit=20)
```

### Параметры

- `offset` — смещение (по умолчанию `0`)
- `limit` — сколько уведомлений вернуть (по умолчанию `20`)

Возвращает модель `Notifications` [подробнее](models/notifications.md)

----------

## Отметить уведомление как прочитанное

```python
client.mark_notification_read(notification_id)
```

### Параметры

- `notification_id` — ID уведомления

### Возвращает

`True` при успехе

----------

## Отметить все уведомления как прочитанные

```python
client.mark_all_notification_read()
```

### Возвращает

`True` при успехе

----------

## Типы уведомлений

Поле `type` может содержать:

- `"follow"` — новый подписчик
- `"like"` — лайк
- `"comment"` — комментарий
- `"reply"` — ответ на комментарий

----------

## Пример

```python
notifications = client.get_notifications(limit=20)

print("Всего:", len(notifications))

for n in notifications:
    print(n.type, n.actor.username if n.actor else "?")

# Отметить одно
client.mark_notification_read(notifications[0].id)

# Отметить все сразу
client.mark_all_notification_read()
```

← [Назад к документации](index.md)
