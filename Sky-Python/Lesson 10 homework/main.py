from functions import load_candidates, get_all, get_by_pk, get_by_skill
from flask import Flask

app = Flask(__name__)

load_candidates()

@app.route('/')
def index():
    result = '<br>'
    candidates = get_all()

    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'

    return f'<pre> {result} </pre>'


@app.route('/candidates/<int:pk>/')
def candidate(pk):

    candidate = get_by_pk(pk)

    if candidate == 'Not found':
        return candidate

    result = '<br>'
    result += candidate['name'] + '<br>'
    result += candidate['position'] + '<br>'
    result += candidate['skills'] + '<br>'
    result += '<br>'

    return f"""
    <img src="{candidate['picture']}">
    '<pre>{result}</pre>'
    """


@app.route('/skills/<skill_name>')
def skills(skill_name):
    candidates = get_by_skill(skill_name)
    result = '<br>'
    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'

    return f'<pre> {result} </pre>'

app.run(debug=True)



