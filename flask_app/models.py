#   from flask_sqlalchemy import SQLAlchemy
import app


class Sessions(app.db.Model):
    id = app.db.Column("id", app.db.Integer, primary_key=True)
    name = app.db.Column("name", app.db.String(2000))
    political_group = app.db.Column("political_group", app.db.String(1000))
    for_ = app.db.Column("for_", app.db.String(20))
    against = app.db.Column("against_", app.db.String(20))
    abstained = app.db.Column("abstained", app.db.String(20))
    voted = app.db.Column("voted", app.db.String(20))

    def __init__(self, name, political_group, for_, against, abstained, voted):
        self.name = name
        self.political_group = political_group
        self.for_ = for_
        self.against = against
        self.abstained = abstained
        self.voted = voted


class Registrations(app.db.Model):
    id = app.db.Column("id", app.db.Integer, primary_key=True)
    name = app.db.Column("name", app.db.String(2000))
    political_group = app.db.Column("political_group", app.db.String(1000))
    present = app.db.Column("present", app.db.String(20))
    by_list = app.db.Column("by_list", app.db.String(20))
    plus_online = app.db.Column("plus_online", app.db.String(20))

    def __init__(self, name, political_group, present, by_list, plus_online):
        self.name = name
        self.political_group = political_group
        self.present = present
        self.by_list = by_list
        self.plus_online = plus_online
