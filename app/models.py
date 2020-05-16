from app import login
from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5


participants = db.Table('participants',
                        db.Column('user_id', db.Integer,db.ForeignKey('user.id')),
                        db.Column('post_id', db.Integer, db.ForeignKey('post.id')))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(128),index=True,unique=True,nullable=False)
    email = db.Column(db.String(128), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128),nullable=False)
    user_level = db.Column(db.Integer,nullable= False,default=3)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return '<User{}>'.format(self.username)

    def set_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable = False , index = True)
    body = db.Column(db.String(1000))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    start_time  = db.Column(db.DateTime, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    max_participant = db.Column(db.Integer)
    verified = db.Column(db.BOOLEAN,nullable=False,default = False)
    participants = db.relationship('User',secondary=participants,
                                   primaryjoin =(participants.c.post_id == id),
                                   secondaryjoin =(participants.c.user_id == id),
                                   backref=db.backref('participants',lazy=True),lazy=True)



    def __repr__(self):
        return '<Post {}>'.format(self.title)

    def join(self, user):
        if not self.is_joining(user):
            self.participants.append(user)

    def leave(self, user):
        if self.is_joining(user):
            self.participants.remove(user)

    def is_joining(self, user):
        return self.participants.filter(
            participants.c.user_id == user.id).count() > 0

    def Participant_list(self):
        return User.query.join(participants,(participants.c.user_id == User.id)).\
            filter(participants.c.post_id == self.id)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))



