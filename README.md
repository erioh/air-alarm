# air-alarm
Уведомляет о воздушной тревоге, реагируя на сообщения в соответствующем Telegram канале

## Информация для пользователей Windows
Так как многим оказалось тяжелова-то использовать этот бот, то было принято волевое решение собрать его в виде простого exe файла.
К сожалению, его работа не гарантируется на всех системах, так как тестировал я только на своём домашнем компьютере.
Для работы бота требуется:
1. Обязательно подписываемся на Telegram канал, где публикуется информация о начале/окончании тревоги. Для Днепра это `sirena_dp`.
2. Скачать и разархивировать архив [air-alarm.zip](https://github.com/erioh/air-alarm/raw/main/air-alarm.zip)
3. отредактировать файл `app-config.properties` как указано ниже и сохранить этот файл. (Для Днепра уже всё настроено.)
4. запустить `main.exe`.
<br>В результате будет открыто консольное окно. Закрывать его не стоит. Пока оно открыто - программа будет радотать.<br/>
5. Вводим свой номер телефона в формате +380 и нажимаем enter.
6. Вводим код, который вы получите на свой Telegram и нажимаем enter.
<br>Если Вам потребуется перезапустить приложение, то вводить больше ничего не потребуется. Просто запускаем `main.exe` и всё.<br/>

## Инсталяция
1. Во первых, обязательно подписаться на телеграмм канал, где постится информация о воздушной тревоге. Для Днепра это `sirena_dp`.
2. вам потребуется установить Python3. Его можно скачать по [ссылке](https://www.python.org/).
3. Запустите консоль. Для этого необходимо нажать Win+R и в появившемся окошке написать cmd и нажать enter.
4. Далее выполняем следующие команды
```
git clone https://github.com/erioh/air-alarm.git
cd air-alarm
pip install -r requirements.txt
```
4. Переходим по ссылке [https://my.telegram.org/](https://my.telegram.org/), вводим свой номер телефона (в формате +380) и код авторизации, который вы получите в Telegram.
5. Кликаем по ссылке "API development tools" и в появившемся окне пишем любой App title и Short name, какой вам понравится.
6. Переходим далее, и в качестве результата мы получим api_id и api_hash
<br><h2>Передавать кому-либо их строго возбраняется! С помощью этой информации можно полностью контролировать ваш Telegram</h2></br>

## Использование
1. Открываем файл `app-config.properties` в текстовом редакторе и указываем свои api_id и api_hash в соответствующие поля. Все остальные значения, как `channel`, `turn_on` и `turn_off` сейчас настроены на оповещение Днепра. Если вы находитесь в каком-либо другом городе - укажите свой канал и свои шаблоны.
2. Сохраняем файл и запускаем бота командой `python main.py` в той же командной строке.
3. Вводим свой номер телефона и нажимаем enter.
4. Вводим код, который вы получите в свой Telegram и вновь нажимаете enter.
<br>Шаги 1, 3 и 4 надо будет выполнить только при первом запуске бота.</br>
<br>Чтобы использовать другой аккаунт, вам потребуется удалить session_name.session и перезапустить бота. В этом случае шаги 1, 3 и 4 придётся снова пройти.</br>
<br>Приложение будет слушать канал, который содержится в переменной  `channel` в файле `app-config.properties` , и ожидать конкретные сообщения.</br>
<br>Правильно работающее приложение будет проигрывать аудиофайл `audio.wav` в цикле при получении сообщения содержащее текст из проперти `turn_on` и выключать его при получении сообщения содержащее текст из проперти `turn_off`.</br>
## Безопасность Telegram аккаунта
Во время настройки бота вам потребуется указать код входа в Telegram дважды. Один раз на [https://my.telegram.org/](https://my.telegram.org/) и второй раз для модуля [telethon](https://github.com/LonamiWebs/Telethon).

