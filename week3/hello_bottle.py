from bottle import route, run, template, response

@route('/<thing>/<id:int>')
def index(thing, id):
    return template('<div>Are you looking for {{object}} with identifier {{id}}?</div>', object=thing, id=id)


run(host='localhost', port=8080)
