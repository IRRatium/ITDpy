
# ITDpy

## Установка pip
```bash
pip install itdpy
```
## Через git
```bash
git clone https://github.com/Gam5510/ITDpy
cd itdpy
pip install -r requirements.txt
pip install -e .
```
## Быстрый старт

![Получение токена](https://i.ibb.co/DH1m8GL7/Assistant.png)

```python
from  itdpy.client  import  ITDClient

client  =  ITDClient(refresh_token="Ваш_refresh_token")

me  =  client.get_me()
print(me.id)
print(me.username)
```

### Скрипт на обновление имени

```python
from  itdpy.client  import  ITDClient
from  datetime  import  datetime
import  time

client = ITDClient(refresh_token="Ваш_токен")

while  True:
	client.update_profile(display_name=f"Фазлиддин |{datetime.now().strftime('%m.%d %H:%M:%S')}|")
	time.sleep(1)
```

### Скрипт на обновление баннера 
```python
from  itdpy.client  import  ITDClient

client  =  ITDClient(refresh_token="Ваш_токен")

file  =  client.upload_file("matrix-rain-effect-animation-photoshop-editor.gif")
print(file.id)
update  =  client.update_profile(banner_id=file.id)
print(update.banner)
```

← [Назад к документации](index.md)