from flask import Flask, render_template, request
import json

app = Flask(__name__)


# from gevent.pywsgi import WSGIServer

# http_server = WSGIServer(('', 5000), app)
# http_server.serve_forever()


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')


def run():
    app.run(host='localhost', port=5000, debug=False)


if __name__ == '__main__':
    run()