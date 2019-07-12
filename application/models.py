from application.app import db
from datetime import datetime
import re


def slugify(string: str) -> str:
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', string)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    costs = db.Column(db.Float)
    spending_money_obj = db.Column(db.String(140))
    comments = db.Column(db.Text)
    created_date = db.Column(db.DateTime, default=datetime.now())
    slug = db.Column(db.String(140), unique=True)

    def __init__(self, *args, **kwargs):
        super(Data, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.spending_money_obj:
            self.slug = slugify(self.spending_money_obj)

    def __repr__(self):
        return f'< Data id: {self.id}, title: {self.spending_money_obj} >'


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(100))
    tag_slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.tag_slug = slugify(self.tag_name)

    def __repr__(self):
        return f'<Tag id: {self.id}, name: {self.tag_name} >'


# TODO add new db model for costs
