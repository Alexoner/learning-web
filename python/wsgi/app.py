import cgi
import time

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])

    html = "<h1>Hello World From Python</h1>\n"
    html += "<p>"+ time.asctime() +"</p>"
    html += "<table>\n"
    for k in env:
        html += "<tr><td>{}</td><td>{}</td></tr>\n".format(k, env[k])
    html += "</table>\n"
    html += "<form>\n"
    html += '<input name="txt" />\n'
    html += '<input type="submit" value="Echo" />\n'
    html += "</form>\n"


    form = cgi.FieldStorage(environ=env)
    if 'txt' in form:
        html += "<hr>You said: <b>{}</b>\n".format(form['txt'].value)

    return html
