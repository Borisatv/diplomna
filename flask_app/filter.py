from flask_sqlalchemy import SQLAlchemy
from flask_app.models import *

db = SQLAlchemy()


def filterRegistration(party, reg_name):
    result = []# [('Регистрация:', 'партия', 'присъстват', 'по списък', 'онлайн')]
    rows = registrations.query.with_entities(registrations.name, registrations.political_group, registrations.present,
                                             registrations.by_list,
                                             registrations.plus_online).filter(
        registrations.name.contains(reg_name),
        registrations.political_group == party).all()
    x = 0
    while x < len(rows):
        result.append(rows[x])
        x += 1
    return result


def getRegisteredParties():
    names = db.session.query(sessions.political_group).distinct()
    result = list(map(lambda e: e[0], names))
    return result


def filterSession(party, name):
    result = [('Заседание:', 'партия', 'за', 'против', 'въздържали се', 'гласували')]
    rows = sessions.query.with_entities(sessions.name, sessions.political_group,
                                        sessions.for_, sessions.against, sessions.abstained,
                                        sessions.voted).filter(sessions.name.contains(name),
                                                               sessions.political_group == party).all()
    y = 0
    while y < len(rows):
        result.append(rows[y])
        y += 1
    return result
