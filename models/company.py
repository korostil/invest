import uuid

from umongo import Document, EmbeddedDocument, fields

from app.database import motor_instance


@motor_instance.register
class Ratio(EmbeddedDocument):
    code = fields.StrField(required=True)
    value = fields.DecimalField(default=0)
    quarter = fields.StrField(required=True)


@motor_instance.register
class FinancialStatement(EmbeddedDocument):
    code = fields.StrField(required=True)
    value = fields.DecimalField(default=0)
    quarter = fields.StrField(required=True)


@motor_instance.register
class Company(Document):
    description = fields.StrField()
    financial_statements = fields.ListField(fields.EmbeddedField(FinancialStatement))
    id = fields.UUIDField(load_default=uuid.uuid4)
    industry = fields.StrField()
    ratios = fields.ListField(fields.EmbeddedField(Ratio))
    sector = fields.StrField()
    title = fields.StrField(required=True)

    class Meta:
        collection_name = 'companies'
