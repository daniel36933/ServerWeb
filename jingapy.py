from jinja2 import FileSystemLoader, Environment
from wsgiref.simple_server import make_server

def application(environ, start_response):

    # Folder load anf template html
    env = Environment(loader=FileSystemLoader("templates"))

    template = env.get_template('template.html')

    # Generate data
    data = {
        'title':'WSGI template render with Jinga',
        'username': 'Tatakae, Tatakae'
    }

    #Render Template
    html = template.render(data)

    header = [('Content-type','text/html; charset=utf-8')]

    #Response code
    start_response('200 OK', header)

    return [bytes(html, 'utf-8')]

#Releace Resources
with make_server('localhost', 8000, application) as httpd:
    print("Start server on port 80000")
    httpd.serve_forever()