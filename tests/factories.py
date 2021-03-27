import factory

from models.share import Share


class ShareFactory(factory.Factory):
    class Meta:
        model = Share

    ticker = factory.Sequence(lambda n: 'TKR%d' % n)
