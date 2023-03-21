from data import db_session
from flask import Flask
from data.jobs import Jobs
from data.users import User
from flask import render_template
from flask_login import LoginManager
import datetime


app = Flask(__name__)

def main():
    db_session.global_init("db/jobs.sqlite")
    app.run()

    #db_sess = db_session.create_session()
    #for job in db_sess.query(Jobs).all():
    #    print(job.job)
    #db_sess.add(job)
    #db_sess.commit()

@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    print(jobs[0])
    return render_template("prof.html", jobs=jobs)

'''@app.route("/cookie_test")
def cookie_test():
    visits_count = int(request.cookies.get("visits_count", 0))
    if visits_count:
        res = make_response(
            f"Вы пришли на эту страницу {visits_count + 1} раз")
        res.set_cookie("visits_count", str(visits_count + 1),
                       max_age=60 * 60 * 24 * 365 * 2)
    else:
        res = make_response(
            "Вы пришли на эту страницу в первый раз за последние 2 года")
        res.set_cookie("visits_count", '1',
                       max_age=60 * 60 * 24 * 365 * 2)
    return res

@app.route("/session_test")
def session_test():
    visits_count = session.get('visits_count', 0)
    session['visits_count'] = visits_count + 1
    return make_response(
        f"Вы пришли на эту страницу {visits_count + 1} раз")

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)
'''

if __name__ == "__main__":
    main()