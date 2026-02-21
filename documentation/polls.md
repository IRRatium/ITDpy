# ITDpy
## Pins
Модуль `pins` позволяет:
-  получать пины
-  удалять пины
- ставить пины

# Получить текущие пины
```python
client.get_pins()
```
Возвращает модель `Pins`  [подробнее](models/pins.md)

### Пример:
```python
pins  =  client.get_pins()  
  
print("Активный пин:", pins.active_pin)  
  
print("\nВсе пины:")  
for  pin  in  pins.pins:  
  print("Slug:", pin.slug)  
  print("Название:", pin.name)  
  print("Описание:", pin.description)  
  print("Получен:", pin.granted_at)  
  print("-"  *  30)
```

# Ставить пины

```python 
client.set_pin(slug="kirill67_202602_infected")
```

# Удалять пины

```python 
client.remove_pin()
```

← [Назад к документации](index.md)
