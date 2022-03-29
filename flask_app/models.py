from flask_app.app import db


class sessions(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(2000))
    political_group = db.Column("political_group", db.String(1000))
    for_ = db.Column("for_", db.String(20))
    against = db.Column("against_", db.String(20))
    abstained = db.Column("abstained", db.String(20))
    voted = db.Column("voted", db.String(20))

    def __init__(self, name, political_group, for_, against, abstained, voted):
        self.name = name
        self.political_group = political_group
        self.for_ = for_
        self.against = against
        self.abstained = abstained
        self.voted = voted


class registrations(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(2000))
    political_group = db.Column("political_group", db.String(1000))
    present = db.Column("present", db.String(20))
    by_list = db.Column("by_list", db.String(20))
    plus_online = db.Column("plus_online", db.String(20))

    def __init__(self, name, political_group, present, by_list, plus_online):
        self.name = name
        self.political_group = political_group
        self.present = present
        self.by_list = by_list
        self.plus_online = plus_online

    def as_dict(self):
        return  { c.name: getattr(self, c.name) for c in self.__table__.columns }