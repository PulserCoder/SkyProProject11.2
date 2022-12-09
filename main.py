from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_skill, get_candidates_by_name

app = Flask(__name__, template_folder='templates')


# the main route with list candidates
@app.route('/')
def main():
    return render_template('index.html', candidates=load_candidates_from_json('candidates.json'))


# profile route with information about person whose ID the user entered
@app.route('/candidate/<int:x>')
def profile(x):
    return render_template('profile.html', candidate=get_candidate(x))


# list on the page with candidates who have name, which user entered
@app.route('/search/<x>')
def search(x):
    return render_template('search.html', candidates=get_candidates_by_name(x), ll=len(get_candidates_by_name(x)))


# list on the page with candidates who have skill, which user entered
@app.route('/skill/<skill_name>')
def skill(skill_name):
    return render_template('skill.html', ss=get_candidates_by_skill(skill_name),
                           ll=len(get_candidates_by_skill(skill_name)), name_skill=skill_name)


# the start of our program
if __name__ == '__main__':
    app.run()
