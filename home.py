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
    summary = 'Software engineer with strong communication and teamwork skills along with an excellent technical background. Seeking an internship May 2022 - August 2022.'
    education = {
        "college": {
            'name': 'Rochester Institute of Technology, Rochester, NY',
            'finished': 'Expected Graduation Date: May 2023',
            'type': 'Bachelor of Science: Software Engineering',
            'classes': 'Classes taken: Computer Science 1 (Python) and 2 (Java), Intro to Software Engineering, Math Models of Software Engineering, '
                       'Process and Project Management, Engineering of Software Subsystems, Engineering Secure Software, Human Centered Requirements and Design, '
                       'Analysis of Algorithms, Design for Computing Systems, Linear Algebra, Calculus 1 and 2, Public Speaking, '
                       'Intercultural Communications, Game Theory, Organizational Behavior.'
            },
        "high_school": {
            'name': 'Gateway High School, Monroeville, PA',
            'finished': 'Graduated May 2018',
            'type': 'High School Diploma',
            'classes': ''
            }
        }
    return render_template('resume.html', summary=summary, education=education)


def run():
    app.run(host='localhost', port=5000, debug=False)


if __name__ == '__main__':
    run()