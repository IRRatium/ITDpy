# ITDpy
## Загрузка файлов 
```python
file = client.upload_file("python.png")

print("\n--- Файл ---")
print("ID:", file.id)
print("Тип:", file.type_)
print("URL:", file.url)
print("Thumbnail:", file.thumbnail_url)
print("Имя файла:", file.filename)
print("MIME тип:", file.mime_type)
print("Размер:", file.size)
print("Ширина:", file.width)
print("Высота:", file.height)
print("Длительность:", file.duration)
print("Порядок:", file.order)
```

Так можно получить такие данные как id которую можно использовать для `аttachment` или чтобы поменять баннер в профиле. Загружать можно любые файлы, только некоторые специфические файлы сайт итд.com не может отображать.

← [Назад к документации](index.md)