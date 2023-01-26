from bottle import route, run, abort
import json
with open('peter_web_data.json', encoding="utf-8") as json_file:
    date_dict = json.load(json_file)

@route('/')
@route('/<year>')
@route('/<year>/<event_type>')
def base(year = "2022", event_type = "Выставки"):
    try:
        return date_dict[event_type][year]
    except KeyError:
        abort(404, f"Запись не найдена. Доступные категории:  {' '.join(date_dict.keys())} ") 

run(host='localhost', port=8081, debug=True)