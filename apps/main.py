from flask import Flask
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy

#创建一个app对象
app = Flask(__name__)

app.config.from_object(DevelopmentConfig)
#把app对象传给SQLAlchemy来初始化
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'UserTable'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(128))
    password = db.Column(db.String(128))

    def __init__(self, username):
        self.username = username
    
    def __repr__(self):
        return "<User '{}'>".format(self.username)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run()