# itdirr

## Модель Portal

### Пример ответа Portal
```json
{
  "active": true,
  "title": "PixelBattle",
  "url": "https://pixel.xn--d1ah4a.com/"
}
```

### Поля объекта Portal

| Поле | Тип | Описание |
|------|-----|----------|
| active | bool | Активен ли ивент сейчас |
| title | str | Название ивента |
| url | str | Ссылка на ивент |

### Пример использования

```python
portal = client.get_portal()

print("Активен:", portal.active)
print("Название:", portal.title)
print("Ссылка:", portal.url)
```

← [Назад к документации](../index.md)
