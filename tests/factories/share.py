import factory

from models import share
from schemas.share import ShareCreate
from tests.factories.base import AsyncFactory, BaseFactory


class ShareDocumentFactory(AsyncFactory):
    class Meta:
        model = share.Share

    ticker = factory.Sequence(lambda n: 'TKR%d' % n)


class ShareFactory(BaseFactory):
    ticker = factory.Sequence(lambda n: 'TKR%d' % n)

    class Meta:
        model = ShareCreate
