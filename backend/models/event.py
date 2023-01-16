import datetime
from dataclasses import dataclass, field
from typing import Optional, Any, TypedDict, Self

from bson import ObjectId

from models.data import Data

from ._shared import BaseModel

COLLECTION_NAME = "event_docs"


class EventImage(TypedDict):
    name: str
    type: str
    size: int
    dims: tuple[int, int]
    content: bytes


@dataclass
class Event(BaseModel):
    image: "EventImage"
    meta: dict[str, Any]
    create_time: str = field(
        default_factory=lambda: datetime.datetime.utcnow().isoformat()
    )

    def __post_init__(self):
        self._collection = COLLECTION_NAME

    @classmethod
    async def get_by_uid(cls, *, uid: str) -> Self:
        curosr = await Data.find(
            collection=COLLECTION_NAME, query=[{"_id": {"$eq": ObjectId(uid)}}]
        )
        try:
            doc = await curosr.next()
            return Event.from_doc(doc)
        except StopAsyncIteration as e:
            raise Exception(f"No event found with UID '{uid}'") from e

    @classmethod
    async def count(cls, *, create_time: Optional[str] = None) -> int:
        query = []

        if create_time is not None:
            query.append({"create_time": {"$gt": create_time}})

        return await Data.count(collection=COLLECTION_NAME, query=query)

    @classmethod
    async def find_paginated_by_create_time_optional(
        cls, *, page: int, create_time: Optional[str] = None
    ) -> list[Self]:
        query = []

        if create_time is not None:
            query.append({"create_time": {"$gt": create_time}})

        events = []
        curosr = await Data.find(
            collection=COLLECTION_NAME,
            query=query,
            skip=(page - 1) * 10,
            limit=10,
        )

        for doc in curosr:
            events.append(Event.from_doc(doc))

        return events
