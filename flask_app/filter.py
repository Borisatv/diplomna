import app
import models


def filter_registration(party, reg_name):
    result = []
    rows = models.Registrations.query.with_entities(models.Registrations.name, models.Registrations.political_group,
                                                    models.Registrations.present,
                                                    models.Registrations.by_list,
                                                    models.Registrations.plus_online).filter(
        models.Registrations.name.contains(reg_name),
        models.Registrations.political_group == party).all()
    y = 0
    while y < len(rows):
        result.append(rows[y])
        y += 1
    return result


def get_registered_parties():
    names = app.db.session.query(models.Sessions.political_group).distinct()
    result = list(map(lambda e: e[0], names))
    return result


def filter_session(party, name):
    result = [('Заседание:', 'партия', 'за', 'против', 'въздържали се', 'гласували')]
    rows = models.Sessions.query.with_entities(models.Sessions.name, models.Sessions.political_group,
                                               models.Sessions.for_, models.Sessions.against, models.Sessions.abstained,
                                               models.Sessions.voted).filter(models.Sessions.name.contains(name),
                                                                             models.Sessions.political_group
                                                                             == party).all()
    y = 0
    while y < len(rows):
        result.append(rows[y])
        y += 1
    return result
