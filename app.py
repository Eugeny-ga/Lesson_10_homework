from flask import Flask

from utils import get_all, get_by_skill, get_by_pk

app = Flask(__name__)


@app.route("/")
def page_index():
    list_candidates = get_all()
    candidates = "<br>"
    for candidate in list_candidates:
        candidates += candidate['name'] + '<br>'
        candidates += candidate['position'] + '<br>'
        candidates += candidate['skills'] + '<br>'
        candidates += '<br>'
    return f"<pre>{candidates}</pre>"


@app.route("/candidates/<int:x>/")
def candidate_profile(x):
    candidate = get_by_pk(x)
    data_candidate = f'<br> <img src="{candidate["picture"]}"> <br>'
    data_candidate += candidate['name'] + '<br>'
    data_candidate += candidate['position'] + '<br>'
    data_candidate += candidate['skills'] + '<br>'
    data_candidate += '<br>'
    return f"<pre>{data_candidate}</pre>"


@app.route("/skills/<x>/")
def page_skills(x):
    list_candidates = get_by_skill(x)
    candidates = "<br>"
    for candidate in list_candidates:
        candidates += candidate['name'] + '<br>'
        candidates += candidate['position'] + '<br>'
        candidates += candidate['skills'] + '<br>'
        candidates += '<br>'
    return f"<pre>{candidates}</pre>"


if __name__ == "__main__":
    app.run()
