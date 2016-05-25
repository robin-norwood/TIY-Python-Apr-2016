from bottle import route, run, template, request, response
import json

from access_data import get_by_min_height

@route('/')
@route('/hello')
@route('/hello/<name>')
def index(name="Pardner"):
    return template('<div>Hello, {{person}}!</div>', person=name)

@route('/<thing>/<id:int>')
def thing(thing, id):
    return template('Are you looking for {{object}} with id {{man}}?',
                    object=thing, man=id)

@route('/data/hello')
def data_hello():
    response.content_type = 'application/json; charset=UTF-8'
    resp_data = { 'noun': 'world', 'thing': "Hello" }
    return json.dumps(resp_data)


@route('/data/2.5/forecast')
def get_forecast():
    lat = request.query.boy
    lon = request.query.lon

    return template('<div>Lat: {{lat}}, lon: {{lon}}',
                    lat=lat, lon=lon)

@route('/waves')
def get_waves():
    min_height = float(request.query.min_height)
    return json.dumps(get_by_min_height(min_height))

run(host='localhost', port=8080)
