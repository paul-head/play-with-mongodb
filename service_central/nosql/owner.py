from datetime import datetime
import mongoengine


class Owner(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    created = mongoengine.DateTimeField(default=datetime.now)
    #  allows to use $set and $inc
    number_of_visits = mongoengine.IntField(default=0)

    #  many-to-many car -> owners , owner -> cars
    car_ids = mongoengine.ListField(mongoengine.ObjectIdField())

    # for service_app.py use this meta:
    # meta = {
    #     'db_alias': 'core',
    #     'collection': 'cars'
    # }

    meta = {
        'db_alias': 'dealership',
        'collection': 'owners',
    }
