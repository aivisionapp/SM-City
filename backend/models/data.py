from typing import Any, Optional

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient


class Data:
    _connection: AsyncIOMotorClient = None

    @classmethod
    def connection(cls) -> AsyncIOMotorClient:
        if not cls._connection:
            cls._connection = AsyncIOMotorClient("mongodb://mongo:27017")

        return cls._connection

    @classmethod
    async def insert(cls, *, collection: str, doc: dict[str, Any]):
        conn = Data.connection()
        db = conn.sm_city_data
        results = await db[collection].insert_one(doc)
        return results.inserted_id

    @classmethod
    async def update(cls, *, collection: str, uids: tuple[str], doc: dict[str, Any]):
        conn = Data.connection()
        db = conn.sm_city_data
        results = await db[collection].update_many(
            {"_id": {"$in": [ObjectId(uid) for uid in uids]}}, {"$set": doc}
        )
        return results.modified_count

    @classmethod
    async def find(
        cls,
        *,
        collection: str,
        query: Optional[list[dict[str, dict[str, Any]]]] = None,
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        sort: Optional[dict[str, int]] = None,
    ):
        conn = Data.connection()
        db = conn.sm_city_data

        pipeline: list[dict[str, Any]] = []
        if query:
            pipeline.append({"$match": {"$and": query}})
        if skip:
            pipeline.append({"$skip": skip})
        if limit:
            pipeline.append({"$limit": limit})
        if sort:
            pipeline.append({"$sort": sort})

        cursor = db[collection].aggregate(pipeline)
        return cursor

    @classmethod
    async def count(
        cls, *, collection: str, query: Optional[list[dict[str, dict[str, Any]]]] = None
    ) -> int:
        conn = Data.connection()
        db = conn.sm_city_data

        pipeline: list[dict[str, Any]] = []

        if query:
            pipeline.append({"$match": {"$and": query}})

        pipeline.append({"$count": "__docs_count"})

        cursor = db[collection].aggregate(pipeline)
        try:
            cursor_results = await cursor.next()
        except StopAsyncIteration:
            return 0

        return cursor_results["__docs_count"]
