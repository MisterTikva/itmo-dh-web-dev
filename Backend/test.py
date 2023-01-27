from bottle import route, run, abort, static_file
import json
import calendar
from bs4 import BeautifulSoup
from colour import Color
import math

with open('peter_web_data.json', encoding="utf-8") as json_file:
    date_dict = json.load(json_file)

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

@route('/<url:re:.*>/<filename>.css')
def send_static(filename, url):
    print(filename)
    return static_file(f"{filename}.css", root='static/')

@route("/calendar")
@route("/calendar/<year>")
@route("/calendar/<year>/<event_type>")
@route("/calendar/<year>/<event_type>/<max_num:int>")
def calendar_page(year = "2022", event_type = "Выставки", max_num = 300):
    color_ramp = list(Color("white").range_to(Color("green"), 10))
    
    try:
        dates = date_dict[event_type][year]
    except KeyError:
        abort(404, f"Запись не найдена. Доступные категории:  {' '.join(date_dict.keys())} ") 
    
    cal = calendar.LocaleHTMLCalendar(locale="ru_RU")
    html = cal.formatyearpage(year, css="styles.css", width=4)
    soup = BeautifulSoup(html)
    for m_idx, month in enumerate(soup.select("table.month")):
        for d_idx, day in enumerate(month.select("td.mon, td.tue, td.wed, td.thu, td.fri, td.sat, td.sun")):
            try:
                color_idx = clamp(math.floor(dates[str(m_idx+1)][str(d_idx+1)] * 10 / max_num), 0, 9)
                day["bgcolor"] = color_ramp[color_idx]
            except KeyError:
                print(f"{m_idx}, {d_idx}")
                day["bgcolor"] = color_ramp[0]

    return str(soup)



@route('/')
@route('/<year>')
@route('/<year>/<event_type>')
def base(year = "2022", event_type = "Выставки"):
    try:
        return date_dict[event_type][year]
    except KeyError:
        abort(404, f"Запись не найдена. Доступные категории:  {' '.join(date_dict.keys())} ") 

run(host='localhost', port=8081, debug=True)