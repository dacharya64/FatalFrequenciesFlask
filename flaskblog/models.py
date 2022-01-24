from datetime import datetime
from flaskblog import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Post('{self.name}')"

