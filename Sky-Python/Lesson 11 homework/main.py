from utils import load_candidates,get_candidate,get_candidates_by_skill,get_candidate_by_name
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    candidates = load_candidates()
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:pk>')
def get_candidate_by_pk(pk):
    candidate = get_candidate(pk)
    return render_template('candidate.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def get_candidate_by_name_(candidate_name):
    candidates = get_candidate_by_name(candidate_name)
    candidates_count = len(candidates)
    return render_template('search.html', candidates=candidates, candidates_count=candidates_count)

@app.route('/skill/<skill_name>')
def get_candidate_by_skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    candidates_count = len(candidates)
    return render_template('skills.html', candidates=candidates, candidates_count=candidates_count, skill = skill_name)

app.run(debug=True)