import factory

from models import share
from tests.factories.base import AsyncFactory


class ShareFactory(AsyncFactory):
    class Meta:
        model = share.Share

    ticker = factory.Sequence(lambda n: 'TKR%d' % n)
