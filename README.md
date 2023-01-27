
# itmo-dh-web-dev

Проект по Основам Веб Разработки Луговских Савелия и Юдаевой Оксаны.
Цель - визуализировать количества мероприятий в честь 350-летия Петра 1 в виде календаря

Основано на [открытых данных Министерства Культуры РФ](https://opendata.mkrf.ru/opendata/7705851331-events)

Чтобы запустить бэкенд необходимо запустить файл test.py в папке Backend (предварительно нужно установить Bottle, BeautifulSoup, Colour)

localhost:8081/<год>/<тип_события>
Возвращает словарь с распределением количества мероприятий типа <тип_события> в году <год> по месяцам и дням

localhost:8081/calendar/<год>/<тип_события>/<макс_число>
Возвращает HTML календарь на <год> с днями окрашенными в соответствии с количеством мероприятий типа <тип_события> в этот день. <макс_число> задает число мероприятий для максимально интеснисовной окраски

<год> - опционален, значение по умолчанию - 2022
<тип_события> - опционален, значение по умолчанию - Выставки
<макс_число> - опционален, значение по умолчанию - 300

Доступные категории: 
 - Выставки 
 - Встречи 
 - Экскурсии 
 - Спектакли 
 - Обучение 
 - Праздники 
 - Концерты 
 - Кино
 - Прочие
