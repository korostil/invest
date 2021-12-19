from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from motor.motor_asyncio import AsyncIOMotorCollection
from pydantic import BaseModel

CollectionType = TypeVar('CollectionType', bound=AsyncIOMotorCollection)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


class CRUDBase(Generic[CollectionType, CreateSchemaType, UpdateSchemaType]):
    search_field = 'id'

    def __init__(self, collection: Type[CollectionType]):
        self.collection = collection

    async def get(self, id: Any) -> Optional[CollectionType]:
        query = {self.search_field: id}
        return await self.collection.find_one(query)  # type: ignore

    async def get_list(
        self, *, filter: dict = None, sort: list = None, skip: int = 0, limit: int = 100
    ) -> List[CollectionType]:
        documents = self.collection.find(filter, skip=skip)
        if sort:
            documents = documents.sort(sort)
        return await documents.to_list(length=limit)  # type: ignore

    async def create(self, *, document: CreateSchemaType) -> CollectionType:
        return await self.collection.insert_one(document)  # type: ignore

    async def update(
        self, *, db_obj: CollectionType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> CollectionType:
        result = await self.collection.update_one({'_id': db_obj._id}, {'$set': obj_in})
        return result  # type: ignore

    async def remove(self, *, id: Any) -> CollectionType:
        result = await self.collection.delete_many({'_id': id})
        return result  # type: ignore
