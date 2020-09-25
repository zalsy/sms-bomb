# sms-bomb
Библиотека для создания своих смс-бомберов.
# Установка
Для установки у вас должен быть python3.7 или выше; 
Установка на Линукс/Termux - этой командой:

```pip3.7 install sms-bomb```

На Windows:

```pip install sms-bomb```

# Использование
Вот самый простой пример использования библиотеки:
```
from sms_bomb import bomber
services = bomber.loadservices("services.txt")
bomber.run(services, "7123456789")
```
В файле `services.txt` должны находится сервисы, на которые будут отправлятся запросы. Вы поймёте это по ходу работы.
