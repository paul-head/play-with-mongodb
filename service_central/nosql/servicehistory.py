import mongoengine
import datetime


class ServiceHistory(mongoengine.EmbeddedDocument):
    date = mongoengine.DateTimeField(default=datetime.datetime.now)
    description = mongoengine.StringField()
    price = mongoengine.FloatField(required=True)
    customer_rating = mongoengine.IntField(required=True)  #  (min_value=1, max_value=5)