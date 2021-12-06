from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorDatabase
from pydantic import BaseModel

CollectionType = TypeVar('CollectionType', bound=AsyncIOMotorCollection)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


class CRUDBase(Generic[CollectionType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, collection: Type[CollectionType]):
        self.collection = collection.opts.collection_name

    async def get(self, db: AsyncIOMotorDatabase, id: Any) -> Optional[CollectionType]:
        return await db[self.collection].find_one({'id': id})  # type: ignore

    async def get_list(
        self,
        db: AsyncIOMotorDatabase,
        *,
        filter: dict = None,
        sort: list = None,
        skip: int = 0,
        limit: int = 100,
    ) -> List[CollectionType]:
        documents = db[self.collection].find(filter, skip=skip)
        if sort:
            documents = documents.sort(sort)
        return await documents.to_list(length=limit)  # type: ignore

    async def create(
        self, db: AsyncIOMotorDatabase, *, document: CreateSchemaType
    ) -> CollectionType:
        return await db[self.collection].insert_one(document)  # type: ignore

    async def update(
        self,
        db: AsyncIOMotorDatabase,
        *,
        db_obj: CollectionType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]],
    ) -> CollectionType:
        result = await db[self.collection].update_one(
            {'_id': db_obj._id}, {'$set': obj_in}
        )
        return result  # type: ignore

    async def remove(self, db: AsyncIOMotorDatabase, *, id: Any) -> CollectionType:
        result = await db[self.collection].delete_many({'_id': id})
        return result  # type: ignore
