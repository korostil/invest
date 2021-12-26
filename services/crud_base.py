from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from motor.motor_asyncio import AsyncIOMotorCollection
from pydantic import BaseModel

CollectionType = TypeVar('CollectionType', bound=AsyncIOMotorCollection)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


def ensure_indexes(func):  # type: ignore
    async def _ensure(*args, **kwargs):  # type: ignore
        self = args[0]
        if not self.indexes_ensured:
            await self.collection.ensure_indexes()
        return await func(*args, **kwargs)

    return _ensure


class CRUDBase(Generic[CollectionType, CreateSchemaType, UpdateSchemaType]):
    search_field = '_id'

    def __init__(self, collection: Type[CollectionType]):
        self.collection = collection
        self.indexes_ensured = False

    @ensure_indexes
    async def get(self, id: Any) -> Optional[CollectionType]:
        query = {self.search_field: id}
        return await self.collection.find_one(query)  # type: ignore

    @ensure_indexes
    async def get_list(
        self, *, filter: dict = None, sort: list = None, skip: int = 0, limit: int = 100
    ) -> List[CollectionType]:
        documents = self.collection.find(filter, skip=skip)
        if sort:
            documents = documents.sort(sort)
        return await documents.to_list(length=limit)  # type: ignore

    @ensure_indexes
    async def create(self, *, document: CreateSchemaType) -> CollectionType:
        new_document = self.collection(**document.dict())
        await new_document.commit()
        return new_document  # type: ignore

    @ensure_indexes
    async def update(
        self, *, db_obj: CollectionType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> CollectionType:
        result = await self.collection.update_one({'_id': db_obj._id}, {'$set': obj_in})
        return result  # type: ignore

    @ensure_indexes
    async def remove(self, *, id: Any) -> CollectionType:
        result = await self.collection.delete_many({'_id': id})
        return result  # type: ignore
