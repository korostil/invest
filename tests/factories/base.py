import asyncio
import inspect

import factory


class AsyncFactory(factory.Factory):
    """
    Copied from
    https://github.com/FactoryBoy/factory_boy/issues/679#issuecomment-673960170
    """

    class Meta:
        abstract = True

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        async def maker_coroutine():
            for key, value in kwargs.items():
                # when using SubFactory, you'll have a Task in the corresponding kwarg
                # await tasks to pass model instances instead
                if inspect.isawaitable(value):
                    kwargs[key] = await value
            # replace as needed by your way of creating model instances
            document = model_class(*args, **kwargs)
            await document.commit()
            return document

        # A Task can be awaited multiple times, unlike a coroutine.
        # useful when a factory and a subfactory must share a same object
        return asyncio.create_task(maker_coroutine())

    @classmethod
    async def create_batch(cls, size, **kwargs):
        return [await cls.create(**kwargs) for _ in range(size)]


class BaseFactory(factory.Factory):
    class Meta:
        abstract = True
