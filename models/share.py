from umongo import Document, fields

from app.database import motor_instance


@motor_instance.register
class Share(Document):
    ticker = fields.StrField(unique=True)

    class Meta:
        collection_name = 'shares'
