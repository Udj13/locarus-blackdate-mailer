# locarus-blackdate-mailer
Простой скрипт предупреждающий на почту о блокировках трекеров на сервере мониторинга Locarus

## Установка

### Скрипт

Создаем каталог, например 
```
mkdir /myvenv/locarus-emailer
```
Копируем туда скрипт main.py.
Открываем и вбиваем настройки.


### Создание виртуального окружения
```
python3 -m venv /myvenv/locarus-emailer
```

Переходим в этот каталог, затем активируем:
```
. bin/activate
```

Устанавливаем зависимости:
```
pip3 install requests
```

Делаем файл исполнимым:
```
chmod +x main.py
```

Выходим из окружения:
```
deactivate
```

## Автоматический запуск

Для того чтобы скрипт запускался автоматически каждое утром,
копируем файлы .service и .timer в /etc/systemd/system/

Затем следует обновить сервисы:
```
systemctl daemon_reload
```

Можно проверить, что всё работает:
```
systemctl start locarus_emailer_bot.service
```

Разовый запуск таймера для проверки:
```
systemctl start locarus_emailer_bot.timer
```

Добавить в автозагрузку:
```
systemctl enable locarus_emailer_bot.timer
```

Всё готово. 
