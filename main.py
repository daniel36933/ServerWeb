from wsgiref.simple_server import make_server

HTML = """
<!DOCTYPE html>
<HTML lang="es">
<HEAD>
<meta charset="UTF-8" />
<TITLE>Ejemplo 7</TITLE>
</HEAD>
<BODY>
<H1>Título 1</H1>
<H2>Título 2</H2>
<H3>Título 3</H3>
<H4>Título 4</H4>
<H5>Título 5</H5>
<H6>Título 6</H6>
<H7>Título 7 (como no existe, no supone ningún cambio)</H7>
<P>Además, los títulos pueden recibir indicaciones de alineación, como en los siguientes ejemplos</P>
<H3 align="center">Título centrado</H3>
<H3 align="right">Título a la derecha</H3>
</BODY>
</HTML>
"""

def application(environ, start_response):
    header = [('Content-type','text/html; charset=utf-8')]

    #Response code
    start_response('200 OK', header)

    return [bytes(HTML, 'utf-8')]

server = make_server('localhost', 8000, application)
print("Start server on port 80000")
server.serve_forever()