import factory

from odm.share import Share
from tests.factories.base import AsyncFactory


class ShareFactory(AsyncFactory):
    class Meta:
        model = Share

    ticker = factory.Sequence(lambda n: 'TKR%d' % n)
