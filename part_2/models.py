from sqlite3 import Error
from flask_login import UserMixin
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from part_2 import update_highscores
from part_2.extensions import db
from part_2.extensions import login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    highscore = db.Column(db.Integer)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def update_highscore(self, current_score):
        if current_score > self.highscore:
            try:
                User.query.filter_by(id=self.id).update(dict(highscore=current_score))
                update_highscores(self.id, current_score)
                db.session.commit()
            except Error:
                db.session.rollback()
            return True
        else:
            return False

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Questions(db.Model):
    q_id = db.Column(db.Integer, primary_key=True)
    ques = db.Column(db.String(350), unique=True)
    option_a = db.Column(db.String(100))
    option_b = db.Column(db.String(100))
    option_c = db.Column(db.String(100))
    ans = db.Column(db.String(100))
    hint = db.Column(db.String(100))

    def __init__(self, ques, option_a, option_b, option_c, ans, hint):
        self.ques = ques
        self.option_a = option_a
        self.option_b = option_b
        self.option_c = option_c
        self.ans = ans
        self.hint = hint


class Highscores(db.Model):
    hs_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100))
    value = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __init__(self, user_id, value, date):
        self.user_id = user_id
        self.value = value
        self.date = date

    def prepare_leaderboard(self):
        try:
            user = User.query.filter_by(id=self.user_id).first()
            username = user.username

        except AttributeError:
            return

        curr = (dict(
                    username=username,
                    score=self.value,
                    date=self.date.strftime('%m/%d/%Y')
                ))
        return curr
